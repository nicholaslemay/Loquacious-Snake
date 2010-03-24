from FluentSelenium.SeleniumExecutionContext import SeleniumExecutionContext
from FluentSelenium.helpers.TestMethodDiscoveryHelper import \
    TestMethodDiscoveryHelper
from FluentSelenium.SeleniumDrivenUserActions import SeleniumDrivenUserActions
from expectations.testWebsite.Locators import Locators
import subprocess
import os
import unittest

class SeleniumDrivenUserActionsExpectations(unittest.TestCase):

    def setUp(self):
        self.testFileName = "file://" + os.path.dirname(__file__) +  "/testWebsite/seleniumTestPage.html"
        self.host    = 'localhost'
        self.port    = 4444
        self.browserStartCommand = '*firefox'
        self.url     = 'http://localhost:6666'
        self.seleniumExecutionContext = SeleniumExecutionContext(self.host, self.port, self.browserStartCommand, self.url)
        self.seleniumExecutionContext.initialize()
       
    def tearDown(self):
        self.seleniumExecutionContext.destroy()
    
    @staticmethod
    def GetTestSuite():
        suite = unittest.TestSuite()
        suite.addTests(map(SeleniumDrivenUserActionsExpectations, TestMethodDiscoveryHelper.GetTestMethods(SeleniumDrivenUserActionsExpectations, "SeleniumDrivenUser")))
        return suite 
    
    def SeleniumDrivenUserActionsGoesToShouldBringTheUserToTheRightPage(self):        
        action = SeleniumDrivenUserActions(self.seleniumExecutionContext)
        action.goesToURL(self.testFileName)
        self.assertEquals(self.testFileName, self.seleniumExecutionContext.seleniumInstance.get_location())

    def SeleniumDrivenUserActionsShouldReturnItselfWhenCalledWithAndThenAndNoSpecificChainingElementHasBeenSpecified(self):
        action = SeleniumDrivenUserActions(self.seleniumExecutionContext)
        self.assertEquals(action.andThen(),action)
    
    def SeleniumDrivenUserActionsShouldReturnChainingElementWhenCalledWithAndThenAndASpecificChainingElementHasBeenSpecified(self):
        action = SeleniumDrivenUserActions(self.seleniumExecutionContext)
        action.chainingElement = "chainingElement"
        self.assertEquals(action.andThen(),"chainingElement")    
        
    def SeleniumDrivenUserActionsShouldLeaveCheckboxClickedwhenAskedToclickOnIt(self):       
        action = SeleniumDrivenUserActions(self.seleniumExecutionContext)
        action.goesToURL(self.testFileName) 
        self.assertFalse(self.seleniumExecutionContext.seleniumInstance.is_checked(Locators.CHECKBOX))
        action.clicks(Locators.CHECKBOX)
        self.assertTrue(self.seleniumExecutionContext.seleniumInstance.is_checked(Locators.CHECKBOX))
    