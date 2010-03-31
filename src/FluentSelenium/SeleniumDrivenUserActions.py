from FluentSelenium.helpers.Decorators import chainable

class SeleniumDrivenUserActionsException(Exception):
    pass

class SeleniumDrivenUserActions:
    
    def __init__(self, seleniumExecutionContext):
        self.seleniumExecutionContext = seleniumExecutionContext
        self.chainingElement = self
    
    def __getSeleniumInstance(self):
        return self.seleniumExecutionContext.seleniumInstance
    
    @chainable
    def goesTo(self, url):
        self.__getSeleniumInstance().open(url)
        
    @chainable
    def andThen(self):
        return self.chainingElement
    
    @chainable
    def clicks(self, locator):
        self.__getSeleniumInstance().click(locator)
        
    @chainable
    def fillsOut(self, locator):
        self.seleniumExecutionContext.setLastVisitedLocation(locator)
    
    @chainable
    def withThis(self, filling):
        if self.seleniumExecutionContext.lastVisitedLocation is None:
            raise SeleniumDrivenUserActionsException("Nowhere to type. Specify where to type with fillsOut.")
        self.__getSeleniumInstance().type(self.seleniumExecutionContext.lastVisitedLocation, filling)