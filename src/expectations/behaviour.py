#!/usr/bin/env python
# coding=utf-8
"""
Behaviour driven development façade to the unit testing framework.

Inspiration
===========

This unit was inspired by Dave Astels' paper "A New Look at Test-Driven Development".

In this paper, he describes a behaviour specification framework for Smalltalk (sbSpec)
and Ruby (rSpec). In those languages he describes embedding the specification framework
into the class library.

Behaviour provides a similar framework for Python, but without hacking into the Python
class library. So to extend the table on pages 4 and 5 of his paper, you get:

Java
----

+--------------------------------------+
| jUnit                                |
+======================================+
| ::                                   |
|                                      |
|     assertEquals( expected, actual ) |
+--------------------------------------+
| ::                                   |
|                                      |
|     assertNull( result )             |
+--------------------------------------+
| ::                                   |
|                                      |
|     try {                            |
|         2 / 0;                       |
|         fail();                      |
|     }                                |
|     catch ( DivideByZero ex) {       |
|     }                                |
+--------------------------------------+


Smalltalk
---------

+---------------------------------------+
| sbSpec                                |
+=======================================+
| ::                                    |
|                                       |
|     actual shouldEqual: expected      |
+---------------------------------------+
| ::                                    |
|                                       |
|     result shouldbeNil                |
+---------------------------------------+
| ::                                    |
|                                       |
|     [2 / 0] shouldThrow: DivideByZero |
+---------------------------------------+


Ruby
----

+---------------------------------------+
| rSpec                                 |
+=======================================+
| ::                                    |
|                                       |
|     actual.should_equal expected      |
+---------------------------------------+
| ::                                    |
|                                       |
|     result.should_be_nil              |
+---------------------------------------+
| ::                                    |
|                                       |
|     [2 / 0].should_throw DividebyZero |
+---------------------------------------+


Python
------

+--------------------------------------------------------------------+
| Behaviour                                                          |
+====================================================================+
| ::                                                                 |
|                                                                    |
|     shouldEqual( actual, expected )                                |
+--------------------------------------------------------------------+
| ::                                                                 |
|                                                                    |
|     shouldBeNone( result )                                         |
+--------------------------------------------------------------------+
| ::                                                                 |
|                                                                    |
|     shouldRaise( ZeroDivisionError, ( lambda x, y: x / y ), 2, 0 ) |
+--------------------------------------------------------------------+

I've also included some of the ideas from Trent Hick's recipe "A Better assertRaises()
for unittest.py", posted on the ActiveState Programmer Network. In particular, checking
the exception's arguments, and matching the exception's string against a regular
expression.

"""
__docformat__ = "restructuredtext en"

import decimal
import math
import re
import sys
import types
import unittest


class Behaviour( unittest.TestCase ):
	"""
	A class whose instances represent single behaviours.

	Public Methods
	--------------

	Behaviour provides the following specifications:

	Value Equality
	++++++++++++++

	- actual shouldEqual expected
	- actual shouldNotEqual unexpected
	- actual [number] shouldApproximatelyEqual expected to significantDigits
	- actual [number] shouldNotApproximatelyEqual unexpected to significantDigits
	
	Convenience Value Equality
	''''''''''''''''''''''''''
	
	- actual shouldBeNone
	- actual shouldNotBeNone
	- actual [number] shouldBeZero
	- actual [number] shouldNotBeZero
	- actual [boolean] shouldBeTrue
	- actual [boolean] shouldBeFalse
	- sequence/mapping [string/tuple/list/dictionary] shouldBeEmpty
	- sequence/mapping [string/tuple/list/dictionary] shouldNotBeEmpty

	Object Identity
	+++++++++++++++

	- actual shouldBeSameAs expected
	- actual shouldNotBeSameAs unexpected

	Pattern Matching
	++++++++++++++++

	- actual [string] shouldMatch regular expression
	- actual [string] shouldNotMatch regular expression

	Collection Membership
	+++++++++++++++++++++

	- sequence/mapping [string/tuple/list/dictionary] shouldInclude item
	- sequence/mapping [string/tuple/list/dictionary] shouldNotInclude item

	Exception Handling
	++++++++++++++++++

	- executable( args, keyword args ) shouldRaiseException (of type)

	Behaviour also provides the following utility methods to the test runner:
	
	- shortDescription

	"""


	def shouldEqual( self, actual, expected, exceptionMsg=None ):
		"""
		Verify that the actual and expected values should be equal.

		Acts as a façade over ``unittest.failUnlessEqual``.

		Parameters
		----------

		actual : *any*
			The value which is being produced.

		expected : *any (comparable to actual)*
			The value which should be produced.

		Keyword Parameters
		------------------

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not verified,
			overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited behaviour
			(i.e., actual == expected).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour specified
			(i.e., actual != expected).

		"""

		def _formatShouldEqualMessage( actual, expected, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			actual : *any*
				The value being produced.

			expected : *any*
				The value which should be produced.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the two values.

			"""

			return msg or """Behaviour.shouldEqual: Actual value (%s) should equal expected value (%s).""" % \
						  ( str( actual ), str( expected ) )

		self.failUnlessEqual( actual, expected, _formatShouldEqualMessage( actual, expected, exceptionMsg ) )
		return True


	def shouldNotEqual( self, actual, unexpected, exceptionMsg=None ):
		"""
		Verify that the actual value and the unexpected values are not equal.

		Acts as a façade over ``unittest.failIfEqual``.

		Parameters
		----------

		actual : *any*
			The value which is being produced.

		unexpected : *any (comparable to actual)*
			The value which should be produced.

		Keyword Parameters
		------------------

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not verified,
			overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited behaviour
			(i.e., actual != unexpected).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour specified
			(i.e., actual == unexpected).

		"""

		def _formatShouldNotEqualMessage( actual, unexpected, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			actual : *any*
				The value being produced.

			unexpected : *any*
				The value which should not be produced.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the two values.

			"""

			return msg or """Behaviour.shouldNotEqual: Actual value (%s) should not equal unexpected value (%s).""" % \
						  ( str( actual ), str( unexpected ) )

		self.failIfEqual( actual, unexpected, _formatShouldNotEqualMessage( actual, unexpected, exceptionMsg ) )
		return True


	def _mustBeNumeric( self, value, calledFrom ):
		"""
		Internal utility method to check that the parameter is a number.

		Parameters
		----------

		value : *number*
			The value to check is a number.

		calledFrom : *string*
			The name of the method which is requesting the check.

		Returns
		-------

		boolean
			True if the value is a number.

		Raises
		------

		TypeError
			Indicates the value was not a number.

		"""

		def _failMustBeNumeric( value, calledFrom ):
			"""
			Format an error message and fail.

			Parameters
			----------

			value : *number*
				The value to check is a number.

			calledFrom : *string*
				The name of the method which is requesting the check.

			Raises
			------

			TypeError
				Indicates the value was not a number, generates the exception message.

			"""

			raise TypeError, """Behaviour.%s: Type (%s) value (%s) cannot be used, must be a number.""" % \
							 ( calledFrom, str( type( value ) ), str( value ) )

		# Easy case: it's an actual number

		if isinstance( value, int ) or isinstance( value, long ) or \
		   isinstance( value, float ) or isinstance( value, decimal.Decimal ):
			return True
		else:
			_failMustBeNumeric( value, calledFrom )


	def shouldApproximatelyEqual( self, actual, expected, significantDigits=15, exceptionMsg=None ):
		"""
		Verify that the actual and expected values are approximately equal.

		This is designed to circumvent the small rounding errors that can creep into
		floating point calculations, typified by:

		+-----------------------------+
		| ::                          |
		|                             |
		|     >>> import math         |
		|     >>> math.sqrt( 2 ) ** 2 |
		|     2.0000000000000004      |
		|     >>>                     |
		+-----------------------------+

		which leads to the following:

		+------------------------------------------------------------------------------------------------+
		| ::                                                                                             |
		|                                                                                                |
		|     >>> import math                                                                            |
		|     >>> import behaviour                                                                       |
		|     >>> b = behaviour.Behaviour()                                                              |
		|     >>> b.shouldEqual( math.sqrt( 2 ) ** 2, 2 )                                                |
		|     Traceback (most recent call last):                                                         |
		|       ...                                                                                      |
		|     AssertionError: Behaviour.shouldEqual: Actual value (2.0) should equal expected value (2). |
		|     >>>                                                                                        |
		+------------------------------------------------------------------------------------------------+

		To avoid this use:

		+--------------------------------------------------------------+
		| ::                                                           |
		|                                                              |
		|     >>> import math                                          |
		|     >>> import behaviour                                     |
		|     >>> b = behaviour.Behaviour()                            |
		|     >>> b.shouldApproximatelyEqual( math.sqrt( 2 ) ** 2, 2 ) |
		|     True                                                     |
		|     >>>                                                      |
		+--------------------------------------------------------------+

		Parameters
		----------

		actual : *number (normally a float)*
			The value which is being produced.

		expected : *number (normally a float)*
			The value which should be produced.

		Keyword Parameters
		------------------

		significantDigits : *number (a positive integer)*
			The number of significant digits to which the actual and expected value
			should equal. Negative values make no sense (less than 1 significant
			digit?), nor do non-integer values (3.5 significant digits?).

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not
			verified, overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited behaviour
			(i.e., actual ≠≠ expected).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour specified (i.e., actual !≠ expected).

		TypeError
			Indicates a non-numeric type was passed as a parameter.

		Warning
		-------

		``Behaviour.shouldApproximatelyEqual()`` uses significant digits (i.e., a count
		of the leading decimal digits):

		+------------------------------------------------------------------------------------------+
		| ::                                                                                       |
		|                                                                                          |
		|     >>> import math                                                                      |
		|     >>> import behaviour                                                                 |
		|     >>> b = behaviour.Behaviour()                                                        |
		|     >>> b.shouldApproximatelyEqual( 1000000000000000.0, 1000000000000001.0 )             |
		|     True                                                                                 |
		|     >>> b.shouldApproximatelyEqual( 0.1000000000, 0.1000000001, significantDigits=10 )   |
		|     Traceback (most recent call last):                                                   |
		|     ...                                                                                  |
		|     AssertionError: Behaviour.shouldApproximatelyEqual: Actual value (0.1) should        |
		|         approximately equal expected value (0.1000000001) to 10 significant digits.      |
		|         Allowable difference is 1.000000001e-11, actual difference is 9.99999943962e-11. |
		|     >>>                                                                                  |
		+------------------------------------------------------------------------------------------+

		``unittest.failUnlessAlmostEqual()`` uses decimal places (i.e., a count of the digits after the decimal
		point):

		+------------------------------------------------------------------------------+
		| ::                                                                           |
		|                                                                              |
		|     >>> import unittest                                                      |
		|     >>> class tc( unittest.TestCase ):                                       |
		|     ...     pass                                                             |
		|     ...     def runTest( self ):                                             |
		|     ...         pass                                                         |
		|     ...                                                                      |
		|     >>> u = tc()                                                             |
		|     >>> u.failUnlessAlmostEqual( 0.1000000000, 0.1000000001 )                |
		|     >>> u.failUnlessAlmostEqual( 1000000000000000.0, 1000000000000001.0 )    |
		|     Traceback (most recent call last):                                       |
		|     ...                                                                      |
		|     AssertionError: 1000000000000000.0 != 1000000000000001.0 within 7 places |
		|     >>>                                                                      |
		+------------------------------------------------------------------------------+

		"""

		def _formatShouldApproximatelyEqualMessage( actual, expected, significantDigits, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			actual : *number*
				The value being produced.

			expected : *number*
				The value which should be produced.

			significantDigits : *number*
				The number of significant digits that were compared.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the two values and the precision.

			"""

			return msg or """Behaviour.shouldApproximatelyEqual: Actual value (%s) should approximately equal expected value (%s) to %d significant digits. Allowable difference is %s, actual difference is %s.""" % \
						  ( str( actual ), str( expected ), significantDigits, abs( expected / ( 10.0 ** significantDigits ) ), abs( actual - expected ) )

		self._mustBeNumeric( actual, 'shouldApproximatelyEqual' )
		self._mustBeNumeric( expected, 'shouldApproximatelyEqual' )
		self._mustBeNumeric( significantDigits, 'shouldApproximatelyEqual' )
		self.failIf( abs( actual - expected ) > abs( expected / ( 10.0 ** significantDigits ) ), _formatShouldApproximatelyEqualMessage( actual, expected, significantDigits, exceptionMsg ) )
		return True


	def shouldNotApproximatelyEqual( self, actual, unexpected, significantDigits=15, exceptionMsg=None ):
		"""
		Verify that the actual value and the unexpected values are not equal.

		See the discussion under shouldApproximatelyEqual for the rationale.

		Parameters
		----------

		actual : *number (normally a float)*
			The value which is being produced.

		unexpected : *number (normally a float)*
			The value which should not be produced.

		Keyword Parameters
		------------------

		significantDigits : *number (a positive integer)*
			The number of significant digits to which the actual and expected value
			should equal. Negative values make no sense (less than 1 significant
			digit?), nor do non-integer values (3.5 significant digits?).

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not
			verified, overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited
			behaviour (i.e., actual !≠ expected).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour
			specified (i.e., actual ≠≠ expected).

		TypeError
			Indicates a non-numeric type was passed as a parameter.

		Warning
		-------

		See the discussion under shouldApproximatelyEqual regarding significant
		digits versus decimal places.

		"""

		def _formatShouldNotApproximatelyEqualMessage( actual, unexpected, significantDigits, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			actual : *number*
				The value being produced.

			unexpected : *number*
				The value which should not be produced.

			significantDigits : *number*
				The number of significant digits that were compared.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the two values and the precision.

			"""

			return msg or """Behaviour.shouldNotApproximatelyEqual: Actual value (%s) should not approximately equal unexpected value (%s) to %d significant digits. Allowable difference is %s, actual difference is %s.""" % \
						  ( str( actual ), str( unexpected ), significantDigits, abs( unexpected / ( 10.0 ** significantDigits ) ), abs( actual - unexpected ) )

		self._mustBeNumeric( actual, 'shouldNotApproximatelyEqual' )
		self._mustBeNumeric( unexpected, 'shouldNotApproximatelyEqual' )
		self._mustBeNumeric( significantDigits, 'shouldNotApproximatelyEqual' )
		self.failUnless( abs( actual - unexpected ) > abs( unexpected / ( 10.0 ** significantDigits ) ), _formatShouldNotApproximatelyEqualMessage( actual, unexpected, significantDigits, exceptionMsg ) )
		return True


	def shouldBeSameAs( self, actual, expected, exceptionMsg=None ):
		"""
		Verify that the actual and expected objects are the same objects.

		Parameters
		----------

		actual : *any*
			The object which is being produced.

		expected : *any*
			The object which should be produced.

		Keyword Parameters
		------------------

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not
			verified, overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited
			behaviour (i.e., actual is expected).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour
			specified (i.e., actual is not expected).

		"""

		def _formatShouldBeSameAsMessage( actual, expected, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			actual : *any*
				The object being produced.

			expected : *any*
				The object which should be produced.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the two objects.

			"""

			return msg or """Behaviour.shouldBeSameAs: Actual object id (%s) value (%s) should be the expected object id (%s) value (%s).""" % \
  						  ( str( id( actual ) ), str( actual ), str( id( expected ) ), str( expected ) )

		self.failUnless( actual is expected, _formatShouldBeSameAsMessage( actual, expected, exceptionMsg ) )
		return True


	def shouldNotBeSameAs( self, actual, unexpected, exceptionMsg=None ):
		"""
		Verify that the actual and unexpected objects are not the same objects.

		Parameters
		----------

		actual : *any*
			The object which is being produced.

		unexpected : *any*
			The object which should be produced.

		Keyword Parameters
		------------------

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not
			verified, overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited
			behaviour (i.e., actual is not unexpected).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour
			specified (i.e., actual is unexpected).

		"""

		def _formatShouldNotBeSameAsMessage( actual, unexpected, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			actual : *any*
				The object being produced.

			unexpected : *any*
				The object which should not be produced.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the two objects.

			"""

			return msg or """Behaviour.shouldNotBeSameAs: Actual object id (%s) value (%s) should not be the unexpected object id (%s) value (%s).""" % \
  						  ( str( id( actual ) ), str( actual ), str( id( unexpected ) ), str( unexpected ) )

		self.failIf( actual is unexpected, _formatShouldNotBeSameAsMessage( actual, unexpected, exceptionMsg ) )
		return True


	def _mustBeString( self, value, calledFrom ):
		"""
		Internal utility method to check that the parameter is a string.

		Parameters
		----------

		value : *string*
			The value to check is a string.

		calledFrom : *string*
			The name of the method which is requesting the check.

		Returns
		-------

		boolean
			True if the value is a string.

		Raises
		------

		TypeError
			Indicates the value was not a string.

		"""

		def _failMustBeString( value, calledFrom ):
			"""
			Format an error message and fail.

			Parameters
			----------

			value : *string*
				The value to check is a string.

			calledFrom : *string*
				The name of the method which is requesting the check.

			Raises
			------

			TypeError
				Indicates the value was not a string, generates the exception message.

			"""

			raise TypeError, """Behaviour.%s: Type (%s) value (%s) cannot be used, must be a string.""" % \
			  				 ( calledFrom, str( type( value ) ), str( value ) )

		if isinstance( value, basestring ):
			return True
		else:
			_failMustBeString( value, calledFrom )


	def shouldMatch( self, actual, pattern, exceptionMsg=None ):
		"""
		Verify the actual value matches the regular expression pattern.

		Parameters
		----------

		actual : *string*
			The value which is being produced.

		pattern : *string (regular expression)*
			The pattern which must be matched.

		Keyword Parameters
		------------------

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not
			verified, overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited
			behaviour (i.e., pattern matches actual).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour
			specified (i.e., pattern does not match actual).

		TypeError
			Indicates a non-string type was passed as a parameter.

		"""

		def _formatShouldMatchMessage( actual, pattern, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			actual : *string*
				The string being produced.

			pattern : *string*
				The regular expression string which should be produced.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the string and the regular expression.

			"""

			return msg or """Behaviour.shouldMatch: Actual value (%s) should match the regular expression pattern (%s).""" % \
  						  ( str( actual ), str( pattern ) )

		self._mustBeString( actual, 'shouldMatch' )
		self._mustBeString( pattern, 'shouldMatch' )
		self.failIfEqual( re.match( pattern, actual ), None, _formatShouldMatchMessage( actual, pattern, exceptionMsg ) )
		return True


	def shouldNotMatch( self, actual, pattern, exceptionMsg=None ):
		"""
		Verify the actual value does not match the regular expression pattern.

		Parameters
		----------

		actual : *string*
			The value which is being produced.

		pattern : *string (regular expression)*
			The pattern which should not be matched.

		Keyword Parameters
		------------------

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not
			verified, overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited
			behaviour (i.e., pattern does not match actual).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour
			specified (i.e., pattern matches actual).

		TypeError
			Indicates a non-string type was passed as a parameter.

		"""

		def _formatShouldNotMatchMessage( actual, pattern, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			actual : *string*
				The string being produced.

			pattern : *string*
				The regular expression string which should not be produced.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the string and the regular expression.

			"""

			return msg or """Behaviour.shouldNotMatch: Actual value (%s) should not match the regular expression pattern (%s).""" % \
  						  ( str( actual ), str( pattern ) )

		self._mustBeString( actual, 'shouldNotMatch' )
		self._mustBeString( pattern, 'shouldNotMatch' )
		self.failUnlessEqual( re.match( pattern, actual ), None, _formatShouldNotMatchMessage( actual, pattern, exceptionMsg ) )
		return True


	def shouldBeNone( self, actual, exceptionMsg=None ):
		"""
		Verify the actual value is None.

		``shouldBeNone( actual )`` is equivalent to ``shouldBeEqual( actual, None )``.

		Parameters
		----------

		actual : *any*
			The value which is being produced.

		Keyword Parameters
		------------------

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not
			verified, overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited
			behaviour (i.e., actual is None).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour
			specified (i.e., actual is not None).

		"""

		def _formatShouldBeNoneMessage( actual, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			actual : *any*
				The value being produced.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the value.

			"""

			return msg or """Behaviour.shouldBeNone: Actual value (%s) should be None.""" % \
  						  str( actual )

		self.failUnlessEqual( actual, None, _formatShouldBeNoneMessage( actual, exceptionMsg ) )
		return True


	def shouldNotBeNone( self, actual, exceptionMsg=None ):
		"""
		Verify the actual value is not None.

		``shouldNotBeNone( actual )`` is equivalent to ``shouldNotBeEqual( actual, None )``.

		Parameters
		----------

		actual : *any*
			The value which is being produced.

		Keyword Parameters
		------------------

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not
			verified, overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited
			behaviour (i.e., actual is not None).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour
			specified (i.e., actual is None).

		"""

		def _formatShouldNotBeNoneMessage( actual, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			actual : *any*
				The value being produced.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the value.

			"""

			return msg or """Behaviour.shouldNotBeNone: Actual value (%s) should not be None.""" % \
  						  str( actual )

		self.failIfEqual( actual, None, _formatShouldNotBeNoneMessage( actual, exceptionMsg ) )
		return True


	def shouldBeZero( self, actual, exceptionMsg=None ):
		"""
		Verify the actual value is Zero.

		``shouldBeZero( actual )`` is equivalent to ``shouldBeEqual( actual, 0 )``.

		Parameters
		----------

		actual : *number*
			The value which is being produced..

		Keyword Parameters
		------------------

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not
			verified, overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited
			behaviour (i.e., actual == 0).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour
			specified (i.e., actual != 0).

		TypeError
			Indicates a non-numeric type was passed as a parameter.

		"""

		def _formatShouldBeZeroMessage( actual, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			actual : *number*
				The value being produced.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the number.

			"""

			return msg or """Behaviour.shouldBeZero: Actual value (%s) should be Zero.""" % \
  						str( actual )

		self._mustBeNumeric( actual, 'shouldBeZero' )
		self.failUnlessEqual( actual, 0, _formatShouldBeZeroMessage( actual, exceptionMsg ) )
		return True


	def shouldNotBeZero( self, actual, exceptionMsg=None ):
		"""
		Verify the actual value is not None.

		``shouldNotBeZero( actual )`` is equivalent to ``shouldNotBeEqual( actual, 0 )``.

		Parameters
		----------

		actual : *number*
			The value which is being produced.

		Keyword Parameters
		------------------

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not
			verified, overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited
			behaviour (i.e., actual != 0).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour
			specified (i.e., actual == 0).

		TypeError
			Indicates a non-numeric type was passed as a parameter.

		"""

		def _formatShouldNotBeZeroMessage( actual, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			actual : *number*
				The value being produced.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the number.

			"""

			return msg or """Behaviour.shouldNotBeZero: Actual value (%s) should not be Zero.""" % \
  						str( actual )

		self._mustBeNumeric( actual, 'shouldNotBeZero' )
		self.failIfEqual( actual, 0, _formatShouldNotBeZeroMessage( actual, exceptionMsg ) )
		return True


	def _mustBeBoolean( self, value, calledFrom ):
		"""
		Internal utility method to check that the parameter is a boolean.

		Parameters
		----------

		value : *boolean*
			The value to check is a boolean.

		calledFrom : *string*
			The name of the method which is requesting the check.

		Returns
		-------

		boolean
			True if the value is a boolean.

		Raises
		------


		TypeError
			Indicates the value was not a boolean.

		"""

		def _failMustBeBoolean( value, calledFrom ):
			"""
			Format an error message and fail.

			Parameters
			----------

			value : *boolean*
				The value to check is a string.

			calledFrom : *string*
				The name of the method which is requesting the check.

			Raises
			------

			TypeError
				Indicates the value was not a boolean, generates the exception message.

			"""

			raise TypeError, """Behaviour.%s: Type (%s) value (%s) cannot be used, must be a boolean (True or False).""" % \
			  				 ( calledFrom, str( type( value ) ), str( value ) )

		if value in ( True, False ):
			return True
		else:
			_failMustBeBoolean( value, calledFrom )


	def shouldBeTrue( self, actual, exceptionMsg=None ):
		"""
		Verify the actual value is boolean True.

		``shouldBeTrue( actual )`` is equivalent to ``shouldBeEqual( actual, True )``.

		Parameters
		----------

		actual : *boolean*
			The value which is being produced.

		Keyword Parameters
		------------------

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not
			verified, overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited
			behaviour (i.e., actual == True).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour
			specified (i.e., actual != True).

		TypeError
			Indicates a non-boolean type was passed as a parameter.

		"""

		def _formatShouldBeTrueMessage( actual, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			actual : *boolean*
				The value being produced.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the boolean.

			"""

			return msg or """Behaviour.shouldBeTrue: Actual value (%s) should be True.""" % \
  						str( actual )

		self._mustBeBoolean( actual, 'shouldBeTrue' )
		self.failUnlessEqual( actual, True, _formatShouldBeTrueMessage( actual, exceptionMsg ) )
		return True


	def shouldBeFalse( self, actual, exceptionMsg=None ):
		"""
		Verify the actual value is (exact boolean) False.

		``shouldBeFalse( actual)`` is equivalent to ``shouldBeEqual( actual, False )``.

		Parameters
		----------

		actual : *boolean*
			The value which is being produced.

		Keyword Parameters
		------------------

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not
			verified, overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited
			behaviour (i.e., actual == False).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour
			specified (i.e., actual != False).

		TypeError
			Indicates a non-boolean type was passed as a parameter.

		"""

		def _formatShouldBeFalseMessage( actual, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			actual : *boolean*
				The value being produced.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the boolean.

			"""

			if msg == None:
				return """Behaviour.shouldBeFalse: Actual value (%s) should be False.""" % \
 							str( actual )
			else:
				return msg

		self._mustBeBoolean( actual, 'shouldBeFalse' )
		self.failUnlessEqual( actual, False, _formatShouldBeFalseMessage( actual, exceptionMsg ) )
		return True


	def _isStringType( self, value ):
		"""
		Check whether strings operations can be performed on the parameter.

		Parameters
		----------

		value : *string*
			The value which is being checked for type.

		Returns
		-------

		boolean
			True if the value to be checked is string-compatible, otherwise
			False.

		"""

		return isinstance( value, basestring )


	def _isTupleType( self, value ):
		"""
		Check whether tuple operations can be performed on the parameter.

		Parameters
		----------

		value : *tuple*
			The value which is being checked for type.

		Returns
		-------

		boolean
			True if the value to be checked is tuple-compatible, otherwise
			False.

		"""

		return isinstance( value, tuple )


	def _isListType( self, value ):
		"""
		Check whether list operations can be performed on the parameter.

		Parameters
		----------

		value : *list*
			The value which is being checked for type.

		Returns
		-------

		boolean
			True if the value to be checked is list-compatible, otherwise
			False.

		"""

		return isinstance( value, list )


	def _isDictType( self, value ):
		"""
		Check whether dictionary operations can be performed on the parameter.

		Parameters
		----------

		value : *dictionary*
			The value which is being checked for type.

		Returns
		-------

		boolean
			True if the value to be checked is dictionary-compatible, otherwise
			False.

		"""

		return isinstance( value, dict )


	def _mustBeMemberType( self, value, calledFrom ):
		"""
		Verify the parameter is a sequence or mapping compatible type.

		Parameters
		----------

		value : *string/tuple/list/dictionary*
			The value which is being checked for type.

		calledFrom : *string*
			The name of the method which is requesting the check.

		Returns
		-------

		boolean
			True if the value to be checked is sequence or mapping compatible.

		Raises
		------


		TypeError
			Indicates the value was not sequence or mapping compatible.

		"""

		def _failMustBeMemberType( value, calledFrom ):
			"""
			Format an error message and fail.

			Parameters
			----------

			value : *string/tuple/list/dictionary*
				The value to check is a collection.

			calledFrom : *string*
				The name of the method which is requesting the check.

			Raises
			------

			TypeError
				Indicates the value was not a collection, generates the exception message.

			"""

			raise TypeError, """Behaviour.%s: Type (%s) value (%s) cannot be used, must be a sequence or mapping.""" % \
			  				 ( calledFrom, str( type( value ) ), str( value ) )

		if self._isStringType( value ) or self._isTupleType( value ) or \
   		   self._isListType( value ) or self._isDictType( value ):
			return True
		else:
			_failMustBeMemberType( value, calledFrom )


	def shouldBeEmpty( self, actual, exceptionMsg=None ):
		"""
		Verify the actual value is an empty sequence or mapping.

		- ``shouldBeEmpty( string )`` is equivalent to ``shouldBeEqual( string, '' )``.
		- ``shouldBeEmpty( tuple )`` is equivalent to ``shouldBeEqual( tuple, () )``.
		- ``shouldBeEmpty( list )`` is equivalent to ``shouldBeEqual( list, [] )``.
		- ``shouldBeEmpty( dictionary )`` is equivalent to ``shouldBeEqual( dictionary, {} )``.

		Parameters
		----------

		actual : *string/tuple/list/dictionary*
			The value which is being produced.

		Keyword Parameters
		------------------

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not
			verified, overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited
			behaviour (i.e., actual is empty).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour
			specified (i.e., actual is not empty).

		TypeError
			Indicates a non-sequence, non-mapping type was passed.

		"""

		def _formatShouldBeEmptyMessage( actual, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			actual : *string/tuple/list/dictionary*
				The collection being produced.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the collection.

			"""

			return msg or """Behaviour.shouldBeEmpty: Actual value (%s) should be empty.""" % \
  						  str( actual )

		self._mustBeMemberType( actual, 'shouldBeEmpty' )
		self.failIf( actual, _formatShouldBeEmptyMessage( actual, exceptionMsg ) )  # Empty sequences/mappings are False
		return True


	def shouldNotBeEmpty( self, actual, exceptionMsg=None ):
		"""
		Verify the actual value an sequence or mapping containing some collection.

		- ``shouldNotBeEmpty( string )`` is equivalent to ``shouldNotBeEqual( string, '' )``.
		- ``shouldNotBeEmpty( tuple )`` is equivalent to ``shouldNotBeEqual( tuple, () )``.
		- ``shouldNotBeEmpty( list )`` is equivalent to ``shouldNotBeEqual( list, [] )``.
		- ``shouldNotBeEmpty( dictionary )`` is equivalent to ``shouldNotBeEqual( dictionary, {} )``.

		Parameters
		----------

		actual : *string/tuple/list/dictionary*
			The value which is being produced. Must be a sequence or mapping.

		Keyword Parameters
		------------------

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not
			verified, overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited
			behaviour (i.e., actual is not empty).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour
			specified (i.e., actual is empty).

		TypeError
			Indicates a non-sequence, non-mapping type was passed.

		"""

		def _formatShouldNotBeEmptyMessage( actual, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			actual : *string/tuple/list/dictionary*
				The collection being produced.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the collection.

			"""

			return msg or """Behaviour.shouldNotBeEmpty: Actual value (%s) should be not empty.""" % \
  						str( actual )

		self._mustBeMemberType( actual, 'shouldNotBeEmpty' )
		self.failUnless( actual, _formatShouldNotBeEmptyMessage( actual, exceptionMsg ) )
		return True


	def _mustBe2Tuple( self, item, calledFrom ):
		"""
		Internal utility method to check that the parameter is a tuple with two collection.

		Parameters
		----------

		value : *tuple*
			The value to check is a 2-tuple.

		calledFrom : *string*
			The name of the method which is requesting the check.

		Returns
		-------

		boolean
			True if the value is a 2-tuple.

		Raises
		------

		AssertionError
			Indicates the value was not a 2-tuple.

		"""

		if not self._isTupleType( item ):
			raise TypeError, """Behaviour.%s: Item (%s) type (%s) must be a 2-tuple ( key, data ).""" % \
			  				 ( calledFrom, str( item ), str( type( item ) ) )
		if len( item ) != 2:
			raise TypeError, """Behaviour.%s: Item (%s) must be a 2-tuple ( key, data ).""" % \
			  				 ( calledFrom, str( item ) )
		return True


	def shouldInclude( self, collection, wanted, exceptionMsg=None ):
		"""
		Verify the actual sequence or mapping contains the wanted item.

		Parameters
		----------

		collection : *string/tuple/list/dictionary*
			The object which is being produced.

		wanted : *any/2-tuple*
			The item to check for membership in the collection. If the collection is a
			sequence, this may be any type that can be inserted in the collection. If the
			collection is a dictionary, the item must be a 2-tuple consisting of a key-value
			pair.

		Keyword Parameters
		------------------

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not
			verified, overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited
			behaviour (i.e., wanted is in collection).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour
			specified (i.e., wanted is not in collection).

		TypeError
			Indicates a non-sequence, non-mapping type was passed as the collection,
			or for a dictionary the item was not a 2-tuple.

		"""

		def _formatShouldIncludeSequenceMessage( sequence, wanted, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			sequence : *string/tuple/list*
				The sequence being produced.

			wanted : *any*
				The item to be found.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the sequence and the item.

			"""

			if msg != None:
				return msg
  			else:
				if self._isStringType( sequence ):
					return """Behaviour.shouldInclude: String (%s) should include item (%s).""" % \
						   ( str( sequence ), str( wanted ) )
				elif self._isTupleType( sequence ):
					return """Behaviour.shouldInclude: Tuple (%s) should include item (%s).""" % \
						   ( str( sequence ), str( wanted ) )
				elif self._isListType( sequence ):
					return """Behaviour.shouldInclude: List (%s) should include item (%s).""" % \
						   ( str( sequence ), str( wanted ) )

		def _formatShouldIncludeMappingNoKeyMessage( mapping, wanted, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			mapping : *dictionary*
				The mapping being produced.

			item : *2-tuple*
				The key and data to be found.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the mapping and the key.

			"""

			return msg or """Behaviour.shouldInclude: Dictionary (%s) should include key (%s).""" % \
  						  ( str( collection ), str( wanted[0] ) )

		def _formatShouldIncludeMappingMessage( mapping, wanted, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			mapping : *dictionary*
				The mapping being produced.

			wanted : *2-tuple*
				The key and data to be found.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the dictionary, the key, and the data.

			"""

			return msg or """Behaviour.shouldInclude: Dictionary (%s) should include key (%s) data (%s).""" % \
  						  ( str( mapping ), str( wanted[0] ), str( wanted[1] ) )

		self._mustBeMemberType( collection, 'shouldInclude' )

		# sequences

		if self._isStringType( collection ) or self._isTupleType( collection ) or self._isListType( collection ):
			self.failUnless( wanted in collection, _formatShouldIncludeSequenceMessage( collection, wanted, exceptionMsg ) )

		# mappings

		elif self._isDictType( collection ):
			self._mustBe2Tuple( wanted, 'shouldInclude' )
			self.failUnless( collection.has_key( wanted[0] ), _formatShouldIncludeMappingNoKeyMessage( collection, wanted, exceptionMsg ) )
			self.failUnlessEqual( collection[ wanted[0] ], wanted[1], _formatShouldIncludeMappingMessage( collection, wanted, exceptionMsg ) )

		return True


	def shouldNotInclude( self, collection, unwanted, exceptionMsg=None ):
		"""
		Verify the actual sequence or mapping does not contain the unwanted item.

		Parameters
		----------

		collection : *string/tuple/list/dictionary*
			The object which is being produced.

		unwanted : *any/2-tuple*
			The item to check for membership in the collection. If the collection is a
			sequence, this may be any type that can be inserted in the collection. If the
			collection is a dictionary, the item must be a 2-tuple consisting of a key-value
			pair.

		Keyword Parameters
		------------------

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not
			verified, overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited
			behaviour (i.e., unwanted is not in collection).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour
			specified (i.e., unwanted is in collection).

		TypeError
			Indicates a non-sequence, non-mapping type was passed as the collection,
			or for a dictionary the item was not a 2-tuple.

		"""

		def _formatShouldNotIncludeSequenceMessage( sequence, unwanted, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			sequence : *string/tuple/list*
				The sequence being produced.

			unwanted : *any*
				The item to be found.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the sequence and the item.

			"""

			if msg != None:
				return msg
			else:
				if self._isStringType( sequence ):
					return """Behaviour.shouldNotInclude: String (%s) should not include item (%s).""" % \
						   ( str( sequence ), str( unwanted ) )
				elif self._isTupleType( sequence ):
					return """Behaviour.shouldNotInclude: Tuple (%s) should not include item (%s).""" % \
						   ( str( sequence ), str( unwanted ) )
				elif self._isListType( sequence ):
					return """Behaviour.shouldNotInclude: List (%s) should not include item (%s).""" % \
						   ( str( sequence ), str( unwanted ) )

		def _formatShouldNotIncludeMappingMessage( mapping, unwanted, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			mapping : *dictionary*
				The collection being produced.

			unwanted : *2-tuple*
				The key and data to be found.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the dictionary, the key, and the data.

			"""

			return msg or """Behaviour.shouldInclude: Dictionary (%s) should not include key (%s) data (%s).""" % \
  						  ( str( mapping ), str( unwanted[0] ), str( unwanted[1] ) )

		self._mustBeMemberType( collection, 'shouldNotInclude' )

		# simple sequences

		if self._isStringType( collection ) or self._isTupleType( collection ) or self._isListType( collection ):
			self.failIf( unwanted in collection, _formatShouldNotIncludeSequenceMessage( collection, unwanted, exceptionMsg ) )

		# dictionary

		elif self._isDictType( collection ):
			self._mustBe2Tuple( unwanted, 'shouldNotInclude' )
			if collection.has_key( unwanted[0] ):
				self.failIfEqual( collection[ unwanted[0] ], unwanted[1], _formatShouldNotIncludeMappingMessage( collection, unwanted, exceptionMsg ) )

		return True


	def shouldRaiseException( self, exceptionType, executable, *args, **kwargs ):
		"""
		Verify that executable( args, kwargs ) raises an exception of exceptionType.

		Parameters
		----------

		exceptionType : *Exception*
			The exception type that should be raised.

		executable : *function/method*
			The executable to verify.

		args : *any*
			A list of arguments to pass to executable.

		kwargs : *any*
			A list of keyword arguments to pass to executable. There are three
			keyword arguments, listed below, which are trapped out and not passed.

		Keyword Parameters
		------------------

		exceptionArgs : *any*
			A tuple of arguments to check against the raised exception's arguments
			(i.e., ensure that not only is the correct exception raised, but that
			it receives the right arguments).

		exceptionPattern : *string*
			A regular expression to match against the raised exception's text value
			(i.e., ensure that not only is the correct exception raised, but that it
			raises the correct error message).

		exceptionMsg : *string*
			An option message to be returned if the behaviour is not verified,
			overriding the default generated message (rarely needed).

		Returns
		-------

		boolean
			True if the specified behaviour matched the exhibited behaviour (i.e.,
			the correct exception was raised, optionally with the correct arguments
			and error message).

		Raises
		------

		AssertionError
			Indicates the behaviour exhibited was not the behaviour specified (i.e.,
			no exception was raised, the wrong exception was raised, or optionally
			the right exception was raised with the wrong arguments or the wrong
			error message).

		"""

		def _getExecutableName( executable ):
			"""
			Returns the name of the executable module.

			Parameters
			----------

			executable : *callable*
				The function or method to extract the name from.

			Returns
			-------

			string
				The name of the callable.

			"""

			if hasattr( executable, '__name__' ):
				return executable.__name__
			else:
				return str( executable )


		def _formatNoExceptionMessage( executable, exceptionType, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			executable : *function/method*
				The collection being produced.

			exceptionType : *Exception*
				The exception type that should be raised.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the executable object and the exception type.

			"""

			return msg or """Behaviour.shouldRaiseException: Executable (%s) should raise exception (%s).""" % \
						  ( _getExecutableName( executable.__name__  ), str( type( exceptionType ) ) )


		def _formatWrongExceptionMessage( executable, exceptionType, exception, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			executable : *function/method*
				The collection being produced.

			exceptionType : *Exception*
				The exception type that should be raised.

			exception : *exception*
				The exception that was raised.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the executable object and the exception types.

			"""

			return msg or """Behaviour.shouldRaiseException: Executable (%s) should raise exception (%s), got exception (%s).""" % \
						  ( _getExecutableName( executable.__name__  ), str( exceptionType ), str( type( exception ) ) )


		def _formatWrongArgsMessage( executable, exceptionType, exceptionArgs, exception, args, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			executable : *function/method*
				The collection being produced.

			exceptionType : *Exception*
				The exception type that should be raised.

			exceptionArgs : *any*
				The arguments that should have been passed to the exception.

			exception : *exception*
				The exception that was raised.

			args : *any*
				The arguments to the raised exception.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the executable object and the exception types and arguments.

			"""

			return msg or """Behaviour.shouldRaiseException: Executable (%s) raised exception (%s), args (%s) should be args (%s).""" % \
						  ( _getExecutableName( executable.__name__  ), str( exceptionType ), str( args ), str( exceptionArgs ) )


		def _formatWrongPatternMessage( executable, exceptionType, exceptionPattern, exception, msg=None ):
			"""
			Format an appropriate error message if one isn't provided.

			Parameters
			----------

			executable : *function/method*
				The collection being produced.

			exceptionType : *Exception*
				The exception type that should be raised.

			exceptionPattern : *string*
				A regular expression that the raised exception should match.

			exception : *exception*
				The exception that was raised.

			args : *any*
				The arguments to the raised exception.

			Keyword Parameters
			------------------

			msg : *string*
				A message to override the generated message.

			Returns
			-------

			string
				Either the message passed in, or a formatted message indicating
				the executable object, the exception types and the pattern.

			"""

			return msg or """Behaviour.shouldRaiseException: Executable (%s) raised exception (%s), pattern (%s) should be pattern (%s).""" % \
						  ( _getExecutableName( executable.__name__  ), str( exceptionType ), str( exception ), str( exceptionPattern ) )

		# Trap out keyword arguments meant for shouldRaiseException

		if 'exceptionArgs' in kwargs:
			exceptionArgs = kwargs[ 'exceptionArgs' ]
			del kwargs[ 'exceptionArgs' ]
		else:
			exceptionArgs = None

		if 'exceptionPattern' in kwargs:
			exceptionPattern = kwargs[ 'exceptionPattern' ]
			del kwargs[ 'exceptionPattern' ]
		else:
			exceptionPattern = None

		if 'exceptionMsg' in kwargs:
			exceptionMsg = kwargs[ 'exceptionMsg' ]
			del kwargs[ 'exceptionMsg' ]
		else:
			exceptionMsg = None

		try:
			executable( *args, **kwargs )
		except exceptionType, ex:  # Correct type of exception raised
			if exceptionArgs is not None:  # Check if arguments to the exception are correct
				self.failIf( ex.args != exceptionArgs,
							 _formatWrongArgsMessage( executable, exceptionType, exceptionArgs, ex, ex.args, exceptionMsg ) )
			if exceptionPattern is not None:  # Check if message raised by the exception is correct
				if re.match( exceptionPattern, str( ex ) ) == None:
					self.fail( _formatWrongPatternMessage( executable, exceptionType, exceptionPattern, ex, exceptionMsg ) )
			return True
		except Exception, ex:  # Wrong exception raised
			raise self.failureException, _formatWrongExceptionMessage( executable, exceptionType, ex, exceptionMsg )
		else:  # No exception raised
			raise self.failureException, _formatNoExceptionMessage( executable, exceptionType, exceptionMsg )

		return True


	def runTest( self ):
		"""
		Stub.
		-----

		unittest complains if this  isn't here, even though we don't need/use it.
		"""
		pass
