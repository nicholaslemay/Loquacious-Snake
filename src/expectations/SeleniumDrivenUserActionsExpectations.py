from FluentSelenium.SeleniumExecutionContext import SeleniumExecutionContext
from FluentSelenium.helpers.TestMethodDiscoveryHelper import \
    TestMethodDiscoveryHelper
import os
import unittest

class SeleniumDrivenUserActionsExpectations(unittest.TestCase):


    def setUp(self):
        self.testFileName = os.path.dirname(__file__) + "/testWebsite/seleniumTestPage.html"
        self.host    = "localhost"
        self.port    = "8080"
        self.browserStartCommand = "*firefox"
        self.url     = "http://localhost:8080"
        self.seleniumExecutionContext = SeleniumExecutionContext(self.host, self.port, self.browserStartCommand, self.url)
        
    def tearDown(self):
        pass

    @staticmethod
    def GetTestSuite():
        suite = unittest.TestSuite()
        suite.addTests(map(SeleniumDrivenUserActionsExpectations, TestMethodDiscoveryHelper.GetTestMethods(SeleniumDrivenUserActionsExpectations, "Selenium")))
        return suite 
    
