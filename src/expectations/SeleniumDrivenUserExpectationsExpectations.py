from FluentSelenium.SharedSeleniumExecutionContext import SharedSeleniumExecutionContext
from FluentSelenium.SeleniumDrivenUserExpectations import SeleniumDrivenUserExpectations,\
    SeleniumDrivenUserExpectationsException
from FluentSelenium.SeleniumDrivenUserActions import SeleniumDrivenUserActions
import os
import unittest


class SeleniumDrivenUserExpectationsExpectations(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super(SeleniumDrivenUserExpectationsExpectations, self).__init__(methodName)
        self.testFileName = "file://" + os.path.dirname(__file__) +  "/testWebsite/seleniumTestPage.html"
        self.host    = 'localhost'
        self.port    = 4444
        self.browserStartCommand = '*firefox'
        self.url     = 'http://localhost:6666'
        self.seleniumExecutionContext = SharedSeleniumExecutionContext(self.host, self.port, self.browserStartCommand, self.url)
        self.seleniumExecutionContext.initialize()
    
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def __del__(self):
        self.seleniumExecutionContext.destroy()  
        
    def SeleniumDrivenUserExpectationsShouldBeOnPageShouldThrowExceptionWhenContextDoesNotReportWeAreOnThatPage(self):
        expectation = SeleniumDrivenUserExpectations(self.seleniumExecutionContext)
        try:
            expectation.shouldBeOnPage("http://www.websitethatdoesnotexist.ca")
            raise Exception("shouldBeOnPage should of raised exception when current location does not match expected page")
        except (SeleniumDrivenUserExpectationsException, ), e:
            pass


    def SeleniumDrivenUserExpectationsShouldBeOnPageShouldNotThrowExceptionWhenContextsCurrentLocationDoesMatchThePageWeExpect(self):
        expectation = SeleniumDrivenUserExpectations(self.seleniumExecutionContext)
        action = SeleniumDrivenUserActions(self.seleniumExecutionContext)
        action.goesTo( self.testFileName)
        expectation.shouldBeOnPage(self.testFileName)
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()