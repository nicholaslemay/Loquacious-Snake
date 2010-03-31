from FluentSelenium.helpers.Decorators import chainable

class SeleniumDrivenUserExpectationsException(Exception):
    pass

class SeleniumDrivenUserExpectations:
    
    def __init__(self, seleniumExecutionContext):
        self.seleniumExecutionContext = seleniumExecutionContext
        self.seleniumExecutionContext.initialize()
        self.chainingElement = self
        
    def __getSeleniumInstance(self):
        return self.seleniumExecutionContext.seleniumInstance
    
    @chainable
    def shouldBeOnPage(self, page):
        currentLocation = self.__getSeleniumInstance().get_location()
        if currentLocation != page:
            raise SeleniumDrivenUserExpectationsException("Expected page " + page + "did not match current location " + currentLocation)
    
    @chainable
    def shouldSee(self, locator):
        if not self.__getSeleniumInstance().is_element_present(locator):
            raise SeleniumDrivenUserExpectationsException(locator + " could not be found on page.")
        self.seleniumExecutionContext.setLastVisitedLocation(locator)