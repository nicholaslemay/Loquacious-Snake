from FluentSelenium.SeleniumExecutionContext import SeleniumExecutionContext
from FluentSelenium.helpers.TestMethodDiscoveryHelper import \
    TestMethodDiscoveryHelper
from FluentSelenium.SeleniumDrivenUserActions import SeleniumDrivenUserActions
import subprocess
import os
import unittest

class SeleniumDrivenUserActionsExpectations(unittest.TestCase):

    def setUp(self):
        self.server = subprocess.Popen("python -m SimpleHTTPServer 6666", shell=True)
        self.testFileName = "/testWebsite/seleniumTestPage.html"
        self.host    = 'localhost'
        self.port    = 4444
        self.browserStartCommand = '*firefox'
        self.url     = 'http://localhost:6666'
        self.seleniumExecutionContext = SeleniumExecutionContext(self.host, self.port, self.browserStartCommand, self.url)
        self.seleniumExecutionContext.initialize()
       
    def tearDown(self):
        self.seleniumExecutionContext.destroy()
        os.kill(self.server.pid, subprocess.signal.SIGKILL)
        
    @staticmethod
    def GetTestSuite():
        suite = unittest.TestSuite()
        suite.addTests(map(SeleniumDrivenUserActionsExpectations, TestMethodDiscoveryHelper.GetTestMethods(SeleniumDrivenUserActionsExpectations, "SeleniumDrivenUser")))
        return suite 
    
    def SeleniumDrivenUserActionsGoesToShouldBringTheUserToTheRightPage(self):        
        action = SeleniumDrivenUserActions(self.seleniumExecutionContext)
        action.goesToURL(self.testFileName)
        self.assertEquals("http://localhost:6666/testWebsite/seleniumTestPage.html", self.seleniumExecutionContext.seleniumInstance.get_location())