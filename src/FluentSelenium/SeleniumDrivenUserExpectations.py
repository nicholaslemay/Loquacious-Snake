from FluentSelenium.helpers.Decorators import chainable, requiresPresenceOfLocator, requiresAPreviouslyVisitedLocator,\
    requiresAPreviouslySelectedOption, resetsOptionBeingHandled,\
    resetsLastVisitedLocator

class SeleniumDrivenUserExpectationsException(Exception):
    pass

class SeleniumDrivenUserExpectations:
      
    def __init__(self, seleniumExecutionContext):
        self.seleniumExecutionContext = seleniumExecutionContext
        self.seleniumExecutionContext.initialize()
        self.chainingElement = self
        
    def getSeleniumInstance(self):        
        return self.seleniumExecutionContext.seleniumInstance
    
    @chainable
    @resetsLastVisitedLocator
    def shouldBeOnPage(self, page):
        currentLocation = self.getSeleniumInstance().get_location()
        if currentLocation != page:
            raise SeleniumDrivenUserExpectationsException("Expected page " + page + "did not match current location " + currentLocation)
    
    @chainable
    @requiresPresenceOfLocator
    def shouldSee(self, locator):        
        self.seleniumExecutionContext.setLastVisitedLocation(locator)
    
    @chainable
    def shouldNotSee(self, locator):
        if self.getSeleniumInstance().is_element_present(locator):
            raise SeleniumDrivenUserExpectationsException(locator + " was found on the current page.")
    
    @chainable
    @requiresAPreviouslyVisitedLocator
    @resetsLastVisitedLocator
    def withValue(self, expectedValue): 
        currentValue = self.getSeleniumInstance().get_value(self.seleniumExecutionContext.lastVisitedLocation)
        if expectedValue != currentValue:
            raise SeleniumDrivenUserExpectationsException("Expected value :" + expectedValue + " did not match current value :" + currentValue)
    
    @chainable
    @requiresAPreviouslyVisitedLocator
    @resetsLastVisitedLocator
    def withText(self, expectedText):
        currentText = self.getSeleniumInstance().get_text((self.seleniumExecutionContext.lastVisitedLocation))
        if expectedText != currentText:
            raise SeleniumDrivenUserExpectationsException("Expected text : " + expectedText + " did not match current text : " + currentText)
    
    @chainable
    @requiresAPreviouslyVisitedLocator
    @resetsLastVisitedLocator
    def checked(self):
        location = self.seleniumExecutionContext.lastVisitedLocation
        if not self.getSeleniumInstance().is_checked(location):
            raise SeleniumDrivenUserExpectationsException(location + " is not checked.")
    
    @chainable
    @requiresAPreviouslyVisitedLocator
    @resetsLastVisitedLocator
    def unchecked(self):
        location = self.seleniumExecutionContext.lastVisitedLocation
        if self.getSeleniumInstance().is_checked(location):
            raise SeleniumDrivenUserExpectationsException(location + " is checked.")
    
    @chainable
    @requiresAPreviouslyVisitedLocator
    def withOption(self, option):
        self.seleniumExecutionContext.optionBeingHandled = option
    
    @chainable
    @requiresAPreviouslyVisitedLocator
    @requiresAPreviouslySelectedOption
    @resetsOptionBeingHandled
    def selected(self):
        optionExpectedToBeSelected = self.seleniumExecutionContext.optionBeingHandled
        currentlySelectedOption = self.getSeleniumInstance().get_selected_label(self.seleniumExecutionContext.lastVisitedLocation)
        if not  currentlySelectedOption == optionExpectedToBeSelected:
            raise SeleniumDrivenUserExpectationsException("Currently selected option : " + currentlySelectedOption + " did not match expected option :  " + optionExpectedToBeSelected)
            