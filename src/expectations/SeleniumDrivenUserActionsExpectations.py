from LoquaciousSnake.SeleniumDrivenUserActions import SeleniumDrivenUserActions,\
    SeleniumDrivenUserActionsException
from LoquaciousSnake.SharedSeleniumExecutionContext import SharedSeleniumExecutionContext
from expectations.testWebsite.Locators import Locators
from mock import Mock
from LoquaciousSnake.helpers.Decorators import LocatorNotFoundException
from LoquaciousSnake.SeleniumDrivenUserExpectations import SeleniumDrivenUserExpectations
from LoquaciousSnake.helpers.JavascriptHelper import JavascriptHelper
from selenium import selenium
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
        self.expectation = SeleniumDrivenUserExpectations(self.seleniumExecutionContext)
        self.originaljquerymethod = JavascriptHelper.GetjQueryWaitForAjaxCondition
        self.originalPrototypeMethod = JavascriptHelper.GetPrototypeWaitForAjaxCondition
        self.originalwaitforcondition = selenium.wait_for_condition
    def tearDown(self):
        JavascriptHelper.GetjQueryWaitForAjaxCondition = self.originaljquerymethod
        JavascriptHelper.GetPrototypeWaitForAjaxCondition = self.originalPrototypeMethod
        selenium.wait_for_condition = self.originalwaitforcondition
        
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
        except (LocatorNotFoundException, ), e:
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
        
    def SeleniumDrivenUserActionsShouldRequireLocatorToExistInOrderToAttemptToUncheckIt(self):
        try:
            self.action.unchecks("unknown locator")
            self.fail("Unchecks should raise exception when locator is not found")
        except LocatorNotFoundException:
            pass
    
    def SeleniumDrivenUserActionsShouldLeaveLocatorUnCheckedAfterAnUnCheck(self):
        self.action.checks(Locators.CHECKBOX)
        self.expectation.shouldSee(Locators.CHECKBOX).checked()
        self.action.unchecks(Locators.CHECKBOX)
        self.expectation.shouldSee(Locators.CHECKBOX).unchecked()
        
    def SeleniumDrivenUserActionsShouldUpdateOptionBeingHandledWhenCalledWithSelects(self):
        myChoice = "hello"
        self.action.selects(myChoice)
        self.assertEquals(self.seleniumExecutionContext.optionBeingHandled, myChoice)
        
    def SeleniumDrivenUserActionsShouldReturnChainingElementwhenCalledWithSelects(self):
        myChoice = "hello"
        self.assertTrue(self.action.selects(myChoice) is self.action.chainingElement)
    
    def SeleniumDrivenUserActionsShouldReturnChainingElementwhenCalledWithComingFrom(self):
        myChoice = Locators.OPTION1
        self.assertTrue(self.action.selects(myChoice).comingFrom(Locators.SELECT) is self.action.chainingElement)
        
    def SeleniumDrivenUserActionsShouldRaiseExceptionWhenComingFromLocatorDoesNotExist(self):
        myChoice = Locators.OPTION1
        try:
            self.action.selects(myChoice).comingFrom("unknown locator")
            self.fail("comingFrom should raise exception when locator does not exist")
        except LocatorNotFoundException:
            pass
    
    def SeleniumDrivenUserActionsShouldRaiseExceptionWhenChoiceDoesNotExist(self):
        myChoice = "hello"
        try:
            self.action.selects(myChoice).comingFrom(Locators.SELECT)
            self.fail("comingFrom should raise exception when selection does not exist")
        except SeleniumDrivenUserActionsException:
            pass    
        
    def SeleniumDrivenUserActionsShouldSelectOptionWhenItIsAvaiable(self):
        self.action.selects(Locators.OPTION1).comingFrom(Locators.SELECT)
        self.expectation.shouldSee(Locators.SELECT).withOption(Locators.OPTION1).selected()
        

    def SeleniumDrivenUserActionsShouldRaiseExceptionWhenWaitsForPageToLoadTimesout(self):
        self.action.clicks(Locators.GOOGLE_LINK)
        try:
            self.action.waitsForPageToLoad(1)
            self.fail("waitsForPageToLoad should raise exception when it times out.")
        except SeleniumDrivenUserActionsException:
            pass
    
    def SeleniumDrivenUserActionsShouldUpdateItemToDragInContextWhenAskedToDrag(self):
        itemToDrag = Locators.SPAN
        self.action.drag(itemToDrag)
        self.assertTrue(self.seleniumExecutionContext.itemToDrag is itemToDrag)
    
    def SeleniumDrivenUserActionsShouldThrowExceptionWhenDragIsCalledOnANonExistingItem(self):
        itemToDrag = "fakeItem"
        try:
            self.action.drag(itemToDrag)
            self.fail("Drag should throw an exception when specified item does not exist")
        except LocatorNotFoundException:
            pass
    
    def SeleniumDrivenUserActionsShouldThrowAnExceptionWhenAskedToDropAnNoItemIsSpecified(self):
        try:
            self.action.andDropsItOn(Locators.SELECT)
            self.fail("andDropsItOn should throw an exception when item to drop was never specified")
        except SeleniumDrivenUserActionsException:
            pass
   
    def SeleniumDrivenUserActionsShouldThrowAnExceptionWhenAskedToWaitForAjaxWithANonSupportedLibrary(self):
        try:
            self.action.waitsForAjax("JSlicious")
            self.fail("waitsForAjax should raise exception when library is no supported")
        except SeleniumDrivenUserActionsException:
            pass
            
    def SeleniumDrivenUserActionsShouldHaveWaitForAjaxShouldGetTheJQueryConditionWhenJQueryIsUsed(self):
        mockedWaitForAjaxCondition = Mock()
        mockedWaitForCondition = Mock()
        selenium.wait_for_condition = mockedWaitForCondition
        JavascriptHelper.GetjQueryWaitForAjaxCondition = mockedWaitForAjaxCondition
        self.action.clicks(Locators.JQUERY_LINK).andThen().waitsForAjax("jQuery")
        self.assertTrue(mockedWaitForAjaxCondition.called)
        
    def SeleniumDrivenUserActionsShouldHaveWaitForAjaxShouldGetThePrototypeConditionWhenPrototypeIsUsed(self):
        mockedWaitForAjaxCondition = Mock()
        mockedWaitForCondition = Mock()
        selenium.wait_for_condition = mockedWaitForCondition
        JavascriptHelper.GetPrototypeWaitForAjaxCondition = mockedWaitForAjaxCondition
        self.action.clicks(Locators.PROTOTYPE_LINK).andThen().waitsForAjax("Prototype")
        self.assertTrue(mockedWaitForAjaxCondition.called)
