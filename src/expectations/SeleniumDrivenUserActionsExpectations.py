from FluentSelenium.SeleniumDrivenUserActions import SeleniumDrivenUserActions
from FluentSelenium.SharedSeleniumExecutionContext import SharedSeleniumExecutionContext
from FluentSelenium.helpers.TestMethodDiscoveryHelper import \
    TestMethodDiscoveryHelper
from expectations.testWebsite.Locators import Locators
import os
import unittest

class SeleniumDrivenUserActionsExpectations(unittest.TestCase):

    def __init__(self, methodName='runTest'): 
        super(SeleniumDrivenUserActionsExpectations, self).__init__(methodName)
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
    