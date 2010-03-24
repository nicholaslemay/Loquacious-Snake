from FluentSelenium.helpers.TestMethodDiscoveryHelper import TestMethodDiscoveryHelper
from mock import Mock
from FluentSelenium.SeleniumDrivenUser import SeleniumDrivenUser
from FluentSelenium.SeleniumDrivenUserActions import SeleniumDrivenUserActions
from FluentSelenium.SeleniumDrivenUserExpectations import SeleniumDrivenUserExpectations
import unittest


class SeleniumDriverUserExpectations(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass

    @staticmethod
    def GetTestSuite():
        suite = unittest.TestSuite()
        suite.addTests(map(SeleniumDriverUserExpectations, TestMethodDiscoveryHelper.GetTestMethods(SeleniumDriverUserExpectations, "Selenium")))
        return suite 
    
    def SeleniumDrivenUserShouldCallAppropriateActionMethodInExpectationWhenCalledWithAnAction(self):
   
            mockedGoesTo = Mock()
            SeleniumDrivenUserActions.goesTo = mockedGoesTo
            
            bob = SeleniumDrivenUser()
            bob.goesTo("http://www.google.ca")
    
            self.assertTrue( mockedGoesTo.called)
    
    def SeleniumDrivenUserShouldCallAppropriateActionMethodInExpectationWhenCalledWithAnExpectation(self):
            mockedShouldBeOnPage = Mock()
            mockedGoesTo = Mock()
            SeleniumDrivenUserActions.goesTo = mockedGoesTo
            SeleniumDrivenUserExpectations.shouldBeOnPage = mockedShouldBeOnPage
            
            bob = SeleniumDrivenUser()
            bob.goesTo("http://www.google.ca")
            bob.shouldBeOnPage("http://www.google.ca")
            self.assertTrue( mockedGoesTo.called)         

    def SeleniumDrivenUserShouldThrowAnExceptionWhenTheMethodIsUnkownToBothActionsAndExpectations(self):
       
        try:
            bob = SeleniumDrivenUser()
            bob.unknownMethodCall()
            raise Exception("unknownMethodCall should of raised an exception")
        except Exception, instance:
            pass
          
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()