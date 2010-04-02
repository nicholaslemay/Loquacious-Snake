from FluentSelenium.helpers.Decorators import chainable,\
    requiresPresenceOfLocator

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
    def withThis(self, filling):
        if self.seleniumExecutionContext.lastVisitedLocation is None:
            raise SeleniumDrivenUserActionsException("Nowhere to type. Specify where to type with fillsOut.")
        self.getSeleniumInstance().type(self.seleniumExecutionContext.lastVisitedLocation, filling)
    
    @chainable
    def selects(self, option):
        self.seleniumExecutionContext.setOptionBeingHandled(option)
    
    @chainable
    @requiresPresenceOfLocator 
    def comingFrom(self, locator):
        option = self.seleniumExecutionContext.optionBeingHandled
        if option not in self.getSeleniumInstance().get_select_options(locator):
            raise SeleniumDrivenUserActionsException(option + " option could not be found in " + locator )
        
        self.getSeleniumInstance().select(locator, option)
        self.seleniumExecutionContext.lastVisitedLocation = None