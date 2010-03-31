from FluentSelenium.SharedSeleniumExecutionContext import SharedSeleniumExecutionContext
from FluentSelenium.SeleniumDrivenUserExpectations import SeleniumDrivenUserExpectations,\
    SeleniumDrivenUserExpectationsException
from FluentSelenium.SeleniumDrivenUserActions import SeleniumDrivenUserActions
from expectations.testWebsite.Locators import Locators
from mock import Mock
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
        action = SeleniumDrivenUserActions(self.seleniumExecutionContext)
        action.goesTo( self.testFileName)

    def tearDown(self):
        pass
    
    def __del__(self):
        self.seleniumExecutionContext.destroy()  
        
    def SeleniumDrivenUserExpectationsShouldBeOnPageShouldThrowExceptionWhenContextDoesNotReportWeAreOnThatPage(self):
        expectation = SeleniumDrivenUserExpectations(self.seleniumExecutionContext)
        try:
            expectation.shouldBeOnPage("http://www.websitethatdoesnotexist.ca")
            raise Exception("shouldBeOnPage should of raised exception when current location does not match expected page")
        except SeleniumDrivenUserExpectationsException:
            pass

    def SeleniumDrivenUserExpectationsShouldBeOnPageShouldNotThrowExceptionWhenContextsCurrentLocationDoesMatchThePageWeExpect(self):
        expectation = SeleniumDrivenUserExpectations(self.seleniumExecutionContext)
        expectation.shouldBeOnPage(self.testFileName)
        
    def SeleniumDrivenUserExpectationsShouldSeeShouldUpdateTheLastVisitedLocation(self):
        self.seleniumExecutionContext.setLastVisitedLocation = Mock()
        expectation = SeleniumDrivenUserExpectations(self.seleniumExecutionContext)
        expectation.shouldSee(Locators.INPUT_TEXT)        
        self.assertTrue(self.seleniumExecutionContext.setLastVisitedLocation.called)
    
    def SeleniumDrivenUserExpectationsShouldSeeShouldThrowAnExceptionWhenLocatorDoesNotExistOnPage(self):
        self.seleniumExecutionContext.setLastVisitedLocation = Mock()
        expectation = SeleniumDrivenUserExpectations(self.seleniumExecutionContext)

        try:
            expectation.shouldSee("locator that does not exist")  
            raise Exception("Should see should raise exception when locator does not exist")
        except SeleniumDrivenUserExpectationsException:
            pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()