class SeleniumDrivenUserExpectationsException(Exception):
    pass

class SeleniumDrivenUserExpectations:
    
    def __init__(self, seleniumExecutionContext):
        self.seleniumExecutionContext = seleniumExecutionContext
    
    def __getSeleniumInstance(self):
        return self.seleniumExecutionContext.seleniumInstance
    
    def shouldBeOnPage(self, page):
        currentLocation = self.__getSeleniumInstance().get_location()
        if currentLocation != page:
            raise SeleniumDrivenUserExpectationsException("Expected page " + page + "did not match current location " + currentLocation)
