from FluentSelenium.SeleniumDrivenUserActions import SeleniumDrivenUserActions,\
    SeleniumDrivenUserActionsException
from FluentSelenium.SharedSeleniumExecutionContext import SharedSeleniumExecutionContext
from expectations.testWebsite.Locators import Locators
from mock import Mock
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
        self.locator='//*[@id="Main"]'
    def setUp(self):
        pass
       
    def tearDown(self):
        pass
    
    def __del__(self):
        self.seleniumExecutionContext.destroy()  
            
    def SeleniumDrivenUserActionsGoesToShouldBringTheUserToTheRightPage(self):        
        action = SeleniumDrivenUserActions(self.seleniumExecutionContext)
        action.goesTo(self.testFileName)
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
        action.goesTo(self.testFileName) 
        self.assertFalse(self.seleniumExecutionContext.seleniumInstance.is_checked(Locators.CHECKBOX))
        action.clicks(Locators.CHECKBOX)
        self.assertTrue(self.seleniumExecutionContext.seleniumInstance.is_checked(Locators.CHECKBOX))
    
    def SeleniumDrivenUserActionsShouldUpdateLastVisitedLocationWhenCalledWithFillsOut(self):
        action = SeleniumDrivenUserActions(self.seleniumExecutionContext) 
        self.seleniumExecutionContext.setLastVisitedLocation = Mock()
        action.fillsOut(self.locator)
        
        self.assertTrue(self.seleniumExecutionContext.setLastVisitedLocation.called)
        
    def SeleniumDrivenUserActionsShouldThrowExceptionWhenWithThisIsCalledAndNoPreviousLocationWasSelected(self):
        action = SeleniumDrivenUserActions(self.seleniumExecutionContext) 
        
        try:
            action.withThis("Text")
            raise Exception("withThis should fail when no location was previously selected")
        except (SeleniumDrivenUserActionsException, ), e:
            pass
        
    def SeleniumDrivenUserActionsShouldFillOutTextBoxProperlyWhenItIsTheSelectedLocation(self):
        textToType = "This rocks!"
        action = SeleniumDrivenUserActions(self.seleniumExecutionContext) 
        action.goesTo(self.testFileName).fillsOut(Locators.INPUT_TEXT).withThis(textToType)
        self.assertEquals(self.seleniumExecutionContext.seleniumInstance.get_value(Locators.INPUT_TEXT), textToType)
    
    
    