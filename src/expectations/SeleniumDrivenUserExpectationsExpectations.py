from FluentSelenium.SharedSeleniumExecutionContext import SharedSeleniumExecutionContext
from FluentSelenium.SeleniumDrivenUserExpectations import SeleniumDrivenUserExpectations,\
    SeleniumDrivenUserExpectationsException
from FluentSelenium.SeleniumDrivenUserActions import SeleniumDrivenUserActions
from expectations.testWebsite.Locators import Locators
from mock import Mock
from FluentSelenium.helpers.Decorators import LocatorNotFoundException,\
    OptionNotFoundException
import os
import unittest


class SeleniumDrivenUserExpectationsExpectations(unittest.TestCase):

    def setUp(self):
        self.testFileName = "file://" + os.path.dirname(__file__) +  "/testWebsite/seleniumTestPage.html"
        self.host    = 'localhost'
        self.port    = 4444
        self.browserStartCommand = '*firefox'
        self.url     = 'http://localhost:6666'
        self.seleniumExecutionContext = SharedSeleniumExecutionContext(self.host, self.port, self.browserStartCommand, self.url)
        self.seleniumExecutionContext.initialize()
        self.action = SeleniumDrivenUserActions(self.seleniumExecutionContext)
        self.action.goesTo( self.testFileName)
        self.expectation = SeleniumDrivenUserExpectations(self.seleniumExecutionContext)
        
    def tearDown(self):
        pass
    
    def __del__(self):
        self.seleniumExecutionContext.destroy()  
        
    def SeleniumDrivenUserExpectationsShouldBeOnPageShouldThrowExceptionWhenContextDoesNotReportWeAreOnThatPage(self):
        try:
            self.expectation.shouldBeOnPage("http://www.websitethatdoesnotexist.ca")
            self.fail("shouldBeOnPage should of raised exception when current location does not match expected page")
        except SeleniumDrivenUserExpectationsException:
            pass

    def SeleniumDrivenUserExpectationsShouldBeOnPageShouldNotThrowExceptionWhenContextsCurrentLocationDoesMatchThePageWeExpect(self):
        self.expectation.shouldBeOnPage(self.testFileName)
        
    def SeleniumDrivenUserExpectationsShouldSeeShouldUpdateTheLastVisitedLocation(self):
        self.seleniumExecutionContext.setLastVisitedLocation = Mock()
        self.expectation.shouldSee(Locators.INPUT_TEXT)        
        self.assertTrue(self.seleniumExecutionContext.setLastVisitedLocation.called)
    
    def SeleniumDrivenUserExpectationsShouldSeeShouldThrowAnExceptionWhenLocatorDoesNotExistOnPage(self):
        self.seleniumExecutionContext.setLastVisitedLocation = Mock()

        try:
            self.expectation.shouldSee("locator that does not exist")  
            self.fail("Should see should raise exception when locator does not exist")
        except LocatorNotFoundException:
            pass
    
    def SeleniumDrivenUserExpectationsShouldNotSeeShouldUpdateTheLastVisitedLocationToNone(self):
        self.seleniumExecutionContext.setLastVisitedLocation = Mock()        
        self.expectation.shouldNotSee("Locator of element that is not present")        
        self.assertEquals(self.seleniumExecutionContext.setLastVisitedLocation.call_args,((None,),{}))
        
    def SeleniumDrivenUserExpectationsShouldNotSeeShouldRaiseExceptionWhenelementIsPresent(self):    
        self.seleniumExecutionContext.setLastVisitedLocation = Mock()
        
        try:
            self.expectation.shouldNotSee(Locators.INPUT_TEXT)  
            self.fail("shouldNotSee should raise exception when locator exists")
        except SeleniumDrivenUserExpectationsException:
            pass
        
        
    def SeleniumDrivenUserExpectationsShouldRaiseExceptionWhenLocatorIsNotFoundWhenWithValueIsCalled(self):
        try:
            self.expectation.withValue("Paul")
            self.fail("WithValue should raise exception when locator does exists")
        except LocatorNotFoundException:
            pass
    
    def SeleniumDrivenUserExpectationsShouldRaiseWhenItDoesNotContainSpecifiedValue(self):
        try:
            self.expectation.shouldSee(Locators.INPUT_TEXT).withValue("Not the right value")
            self.fail("withValue should raise exception when values do not match")
        except SeleniumDrivenUserExpectationsException:
            pass
        
    def SeleniumDrivenUserExpectationsShouldReturnChainingElementWhenValueIsTheOneExpected(self):
        textToType = "Awesome"
        self.action.fillsOut(Locators.INPUT_TEXT).withThis(textToType)
        self.assertTrue(self.expectation.chainingElement is self.expectation.shouldSee(Locators.INPUT_TEXT).withValue(textToType))
    
    def SeleniumDrivenUserExpectationsShouldRaiseExceptionWhenLocatorIsNotFoundWhenWithTextIsCalled(self):
        try:
            self.expectation.withText("Text")
            self.fail("WithText should raise exception when locator does exists")
        except LocatorNotFoundException:
            pass
    
    def SeleniumDrivenUserExpectationsShouldRaiseWhenItDoesNotContainSpecifiedText(self):
        try:
            self.expectation.shouldSee(Locators.SPAN).withText("Text that is not there")
            self.fail("withText should raise exception when values do not match")
        except SeleniumDrivenUserExpectationsException:
            pass
    
    def SeleniumDrivenUserExpectationsShouldReturnChainingElementWhenTextIsTheOneExpected(self):
        expectation = SeleniumDrivenUserExpectations(self.seleniumExecutionContext)
        self.assertTrue(expectation.chainingElement is expectation.shouldSee(Locators.SPAN).withText("Text")) 
        
    def SeleniumDrivenUserExpectationsShouldThrowAnExceptionWhenCheckedIsCalledwithoutAPreviouslyVisitedLocator(self):
        try:
            self.expectation.checked()
            self.fail("Checked should raise exception when locator does exists")
        except LocatorNotFoundException:
            pass
        
    def SeleniumDrivenUserExpectationsShouldThrowAnExceptionWhenCheckedIsCalledOnAnItemThatIsNotChecked(self):
        try:
            self.expectation.shouldSee(Locators.CHECKBOX).checked()
            self.fail("Checked should raise exception when locator is not checked")
        except SeleniumDrivenUserExpectationsException:
            pass
        
    def SeleniumDrivenUserExpectationsShouldReturnChainingElementWhenCheckedSucceeds(self):
        self.action.checks(Locators.CHECKBOX)
        self.assertTrue(self.expectation.shouldSee(Locators.CHECKBOX).checked() is self.expectation.chainingElement)
        
        
    def SeleniumDrivenUserExpectationsShouldThrowAnExceptionWhenUnCheckedIsCalledwithoutAPreviouslyVisitedLocator(self):
        try:
            self.expectation.unchecked()
            self.fail("UnChecked should raise exception when locator does exists")
        except LocatorNotFoundException:
            pass    
        
    def SeleniumDrivenUserExpectationsShouldThrowAnExceptionWhenUnCheckedIsCalledOnAnItemThatIsChecked(self):
        try:
            self.action.checks(Locators.CHECKBOX)
            self.expectation.shouldSee(Locators.CHECKBOX).unchecked()
            self.fail("UnChecked should raise exception when locator is checked")
        except SeleniumDrivenUserExpectationsException:
            pass
        
    def SeleniumDrivenUserExpectationsShouldReturnChainingElementWhenUnCheckedSucceeds(self):
        self.assertTrue(self.expectation.shouldSee(Locators.CHECKBOX).unchecked() is self.expectation.chainingElement)   
        

    
    def SeleniumDrivenUserExpectationsShouldRaiseExceptionWhenWithOptionIsCalledWithNoVisitedLocation(self):
        try:
            self.expectation.withOption(Locators.OPTION3)
            self.fail("withOption should raise exception when locator was not set before hand")
        except LocatorNotFoundException:
            pass    
        
    def SeleniumDrivenUserExpectationsShouldUpdateOptionBeingHandled(self):
        self.expectation.shouldSee(Locators.SELECT).withOption(Locators.OPTION3)
        self.assertEquals(self.seleniumExecutionContext.optionBeingHandled,Locators.OPTION3)
  
    def SeleniumDrivenUserExpectationsShouldRaiseExceptionWhenSelectedIsCalledWithNoVisitedLocation(self):
        try:
            self.expectation.selected()
            self.fail("selected should raise exception when locator does exists")
        except LocatorNotFoundException:
            pass    
        
    def SeleniumDrivenUserExpectationsShouldRaiseAnExceptionWhenSelectedIsCalledWithNoOptionSpecified(self):
        try:
            self.expectation.shouldSee(Locators.SELECT).selected()
            self.fail("selected should throw exception when no option was selected")
        except OptionNotFoundException:
            pass
        
    def SeleniumDrivenUserExpectationsShouldRaiseExceptionWhenSelectedIsCalledWithAnOptionThatIsNotSelected(self):
        try:
            self.expectation.shouldSee(Locators.SELECT).withOption(Locators.OPTION3).selected()
            self.fail("selected should trhow an exception when the expected option is not selected")
        except SeleniumDrivenUserExpectationsException:
            pass
        
    def SeleniumDrivenUserExpectationsShouldResetOptionBeingHandledAndLastVisitedLocation(self):   
        self.expectation.shouldSee(Locators.SELECT).withOption(Locators.OPTION1).selected()
        self.assertTrue(self.seleniumExecutionContext.optionBeingHandled is None)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()