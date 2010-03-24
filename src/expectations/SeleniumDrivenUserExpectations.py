from FluentSelenium.helpers.TestMethodDiscoveryHelper import TestMethodDiscoveryHelper
from mock import Mock
from FluentSelenium.SeleniumDrivenUser import SeleniumDrivenUser
from FluentSelenium.SeleniumDrivenUserActions import SeleniumDrivenUserActions
from FluentSelenium.SeleniumDrivenUserExpectations import SeleniumDrivenUserExpectations
import unittest


class SeleniumDriverUserExpectations(unittest.TestCase):

    
    
    def setUp(self):
        self.originalGoesToMethod = SeleniumDrivenUserActions.goesToURL
        self.originalShouldBeOnPage = SeleniumDrivenUserExpectations.shouldBeOnPage

    def tearDown(self):
        SeleniumDrivenUserActions.goesToURL = self.originalGoesToMethod  
        SeleniumDrivenUserExpectations.shouldBeOnPage = self.originalShouldBeOnPage  


    def testName(self):
        pass

    @staticmethod
    def GetTestSuite():
        suite = unittest.TestSuite()
        suite.addTests(map(SeleniumDriverUserExpectations, TestMethodDiscoveryHelper.GetTestMethods(SeleniumDriverUserExpectations, "Selenium")))
        return suite 
    
    def SeleniumDrivenUserShouldCallAppropriateActionMethodInExpectationWhenCalledWithAnAction(self):
   
            mockedGoesToURL = Mock()
            SeleniumDrivenUserActions.goesToURL = mockedGoesToURL
            
            bob = SeleniumDrivenUser(None)
            bob.goesToURL("http://www.google.ca")
    
            self.assertTrue( mockedGoesToURL.called)
    
    def SeleniumDrivenUserShouldCallAppropriateActionMethodInExpectationWhenCalledWithAnExpectation(self):
            mockedShouldBeOnPage = Mock()
            mockedGoesTo = Mock()
            SeleniumDrivenUserActions.goesTo = mockedGoesTo
            SeleniumDrivenUserExpectations.shouldBeOnPage = mockedShouldBeOnPage
            
            bob = SeleniumDrivenUser(None)
            bob.goesTo("http://www.google.ca")
            bob.shouldBeOnPage("http://www.google.ca")
            self.assertTrue( mockedGoesTo.called)         

    def SeleniumDrivenUserShouldThrowAnExceptionWhenTheMethodIsUnkownToBothActionsAndExpectations(self):
       
        try:
            bob = SeleniumDrivenUser(None)
            bob.unknownMethodCall()
            raise Exception("unknownMethodCall should of raised an exception")
        except Exception, instance:
            pass
          
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()