from FluentSelenium.SeleniumExecutionContext import SeleniumExecutionContext
from FluentSelenium.helpers.TestMethodDiscoveryHelper import TestMethodDiscoveryHelper
from FluentSelenium.SeleniumDrivenUserExpectations import SeleniumDrivenUserExpectations,\
    SeleniumDrivenUserExpectationsException
from FluentSelenium.SeleniumDrivenUserActions import SeleniumDrivenUserActions
import os
import unittest


class SeleniumDrivenUserExpectationsExpectations(unittest.TestCase):


    def setUp(self):
        self.testFileName = "file://" + os.path.dirname(__file__) +  "/testWebsite/seleniumTestPage.html"
        self.host    = 'localhost'
        self.port    = 4444
        self.browserStartCommand = '*firefox'
        self.url     = 'http://localhost:6666'
        self.seleniumExecutionContext = SeleniumExecutionContext(self.host, self.port, self.browserStartCommand, self.url)
        self.seleniumExecutionContext.initialize()


    def tearDown(self):
        pass

    @staticmethod
    def GetTestSuite():
        suite = unittest.TestSuite()
        suite.addTests(map(SeleniumDrivenUserExpectationsExpectations, TestMethodDiscoveryHelper.GetTestMethods(SeleniumDrivenUserExpectationsExpectations, "SeleniumDrivenUserExpectationsShould")))
        return suite 


    def SeleniumDrivenUserExpectationsShouldBeOnPageShouldThrowExceptionWhenContextDoesNotReportWeAreOnThatPage(self):
        expectation = SeleniumDrivenUserExpectations(self.seleniumExecutionContext)
        try:
            expectation.shouldBeOnPage("http://www.websitethatdoesnotexist.ca")
            raise Exception("shouldBeOnPage should of raised excpetion when current location does not match expected page")
        except (SeleniumDrivenUserExpectationsException, ), e:
            pass


    def SeleniumDrivenUserExpectationsShouldBeOnPageShouldNotThrowExceptionWhenContextsCurrentLocationDoesMatchThePageWeExpect(self):
        expectation = SeleniumDrivenUserExpectations(self.seleniumExecutionContext)
        action = SeleniumDrivenUserActions(self.seleniumExecutionContext)
        action.goesToURL( self.testFileName)
        expectation.shouldBeOnPage(self.testFileName)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()