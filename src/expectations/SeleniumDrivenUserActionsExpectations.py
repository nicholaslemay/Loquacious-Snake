from FluentSelenium.SeleniumDrivenUserActions import SeleniumDrivenUserActions,\
    SeleniumDrivenUserActionsException
from FluentSelenium.SharedSeleniumExecutionContext import SharedSeleniumExecutionContext
from expectations.testWebsite.Locators import Locators
from mock import Mock
from FluentSelenium.helpers.Decorators import LocatorNotFoundException
import os
import unittest

class SeleniumDrivenUserActionsExpectations(unittest.TestCase):

    def setUp(self):
        self.testFileName = "file://" + os.path.dirname(__file__) +  "/testWebsite/seleniumTestPage.html"
        self.host    = 'localhost'
        self.port    = 4444
        self.browserStartCommand = '*firefox'
        self.url     = 'http://localhost:6666'
        self.seleniumExecutionContext = SharedSeleniumExecutionContext(self.host, self.port, self.browserStartCommand, self.url)
        self.seleniumExecutionContext.initialize()   
        self.locator='//*[@id="Main"]'
        self.action = SeleniumDrivenUserActions(self.seleniumExecutionContext)
        self.action.goesTo(self.testFileName)
       
    def tearDown(self):
        pass
    
    def __del__(self):
        self.seleniumExecutionContext.destroy()  
    
    def SeleniumDrivenUserActionsGoesToShouldBringTheUserToTheRightPage(self):                
        self.assertEquals(self.testFileName, self.seleniumExecutionContext.seleniumInstance.get_location())

    def SeleniumDrivenUserActionsShouldReturnItselfWhenCalledWithAndThenAndNoSpecificChainingElementHasBeenSpecified(self):
        self.assertEquals(self.action.andThen(), self.action)
    
    def SeleniumDrivenUserActionsShouldReturnChainingElementWhenCalledWithAndThenAndASpecificChainingElementHasBeenSpecified(self):
        self.action.chainingElement = "chainingElement"
        self.assertEquals(self.action.andThen(),"chainingElement")    
        
    def SeleniumDrivenUserActionsShouldLeaveCheckboxClickedwhenAskedToclickOnIt(self):       
        self.assertFalse(self.seleniumExecutionContext.seleniumInstance.is_checked(Locators.CHECKBOX))
        self.action.clicks(Locators.CHECKBOX)
        self.assertTrue(self.seleniumExecutionContext.seleniumInstance.is_checked(Locators.CHECKBOX))
    
    def SeleniumDrivenUserActionsShouldUpdateLastVisitedLocationWhenCalledWithFillsOut(self):
        self.seleniumExecutionContext.setLastVisitedLocation = Mock()
        self.action.fillsOut(self.locator)        
        self.assertTrue(self.seleniumExecutionContext.setLastVisitedLocation.called)
        
    def SeleniumDrivenUserActionsShouldThrowExceptionWhenWithThisIsCalledAndNoPreviousLocationWasSelected(self):
        
        try:
            self.action.withThis("Text")
            self.fail("withThis should fail when no location was previously selected")
        except (SeleniumDrivenUserActionsException, ), e:
            pass
        
    def SeleniumDrivenUserActionsShouldFillOutTextBoxProperlyWhenItIsTheSelectedLocation(self):
        textToType = "This rocks!"
        self.action.goesTo(self.testFileName).fillsOut(Locators.INPUT_TEXT).withThis(textToType)
        self.assertEquals(self.seleniumExecutionContext.seleniumInstance.get_value(Locators.INPUT_TEXT), textToType)
    
    def SeleniumDrivenUserActionsShouldRequireLocatorToExistInOrderToAttemptTocheckIt(self):
        try:
            self.action.checks("unknown locator")
            self.fail("Checks should raise exception when locator is not found")
        except LocatorNotFoundException:
            pass
        
    def SeleniumDrivenUserActionsShouldLeaveLocatorCheckedAfterACheck(self):
        self.assertFalse(self.seleniumExecutionContext.seleniumInstance.is_checked(Locators.CHECKBOX))
        self.action.checks(Locators.CHECKBOX)
        self.assertTrue(self.seleniumExecutionContext.seleniumInstance.is_checked(Locators.CHECKBOX))