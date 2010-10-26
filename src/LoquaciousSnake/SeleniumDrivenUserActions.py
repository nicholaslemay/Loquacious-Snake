from LoquaciousSnake.helpers.Decorators import chainable,\
    requiresPresenceOfLocator, requiresAPreviouslySelectedOption,\
    resetsLastVisitedLocator, requiresAPreviouslyVisitedLocator
from LoquaciousSnake.helpers.JavascriptHelper import JavascriptHelper

class SeleniumDrivenUserActionsException(Exception):
    pass

class SeleniumDrivenUserActions:
    
    def __init__(self, seleniumExecutionContext):
        self.seleniumExecutionContext = seleniumExecutionContext
        self.chainingElement = self
    
    def getSeleniumInstance(self):
        return self.seleniumExecutionContext.seleniumInstance
    
    @chainable
    def goesTo(self, url):        
        self.getSeleniumInstance().open(url)
        
    @chainable
    def andThen(self):
        return self.chainingElement
    
    @chainable
    @requiresPresenceOfLocator
    def clicks(self, locator):
        self.getSeleniumInstance().click(locator)
    
    @chainable
    @requiresPresenceOfLocator 
    def checks(self, locator):
        self.getSeleniumInstance().check(locator)
    
    @chainable
    @requiresPresenceOfLocator 
    def unchecks(self, locator):
        self.getSeleniumInstance().uncheck(locator)
    
    @chainable
    def fillsOut(self, locator):
        self.seleniumExecutionContext.setLastVisitedLocation(locator)
    
    @chainable
    @requiresAPreviouslyVisitedLocator
    @resetsLastVisitedLocator
    def withThis(self, filling):
        self.getSeleniumInstance().type(self.seleniumExecutionContext.lastVisitedLocation, filling)
    
    @chainable
    def selects(self, option):
        self.seleniumExecutionContext.setOptionBeingHandled(option)
    
    @chainable
    @requiresPresenceOfLocator 
    @resetsLastVisitedLocator
    def comingFrom(self, locator):
        option = self.seleniumExecutionContext.optionBeingHandled
        if option not in self.getSeleniumInstance().get_select_options(locator):
            raise SeleniumDrivenUserActionsException(option + " option could not be found in " + locator )
        
        self.getSeleniumInstance().select(locator, option)

    @chainable
    def waitsForPageToLoad(self, timeout=30000):
        try:
            self.getSeleniumInstance().wait_for_page_to_load(timeout)
        except:
            raise SeleniumDrivenUserActionsException("Timeout reached")
    
    @chainable
    @requiresPresenceOfLocator
    def drag(self, locator):
        self.seleniumExecutionContext.setItemToDrag(locator)
    
    @chainable
    @requiresPresenceOfLocator
    def andDropsItOn(self, locator):
        if self.seleniumExecutionContext.itemToDrag is None:
            raise SeleniumDrivenUserActionsException("Nothing to drag")
        self.getSeleniumInstance().drag_and_drop(self.seleniumExecutionContext.itemToDrag, locator)
        self.seleniumExecutionContext.setItemToDrag(None)
    
    @chainable
    def waitsForAjax(self, library="jQuery", timeout=30000):
        waitForAjaxCondition = {"jQuery":JavascriptHelper.GetjQueryWaitForAjaxCondition,
                                "Prototype":JavascriptHelper.GetPrototypeWaitForAjaxCondition
                               }
     
        try :  
            condition = waitForAjaxCondition[library]()
            self.getSeleniumInstance().wait_for_condition(condition,timeout)
        except KeyError:
            raise SeleniumDrivenUserActionsException("Specified library : " + library +" is not supported")
    
    