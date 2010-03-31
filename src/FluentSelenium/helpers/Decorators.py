class LocatorNotFoundException(Exception):
    pass

def chainable(functionToExecute):
    def chain(*args,**kwargs):
        self = args[0]
        functionToExecute(*args,**kwargs)
        return self.chainingElement
    return chain

def requiresPresenceOfLocator(functionToExecute):
    def validatePriorToExecution(*args,**kwargs):
        self = args[0]
        locator = args[1]
        if not self.getSeleniumInstance().is_element_present(locator):
            raise LocatorNotFoundException(locator + " could not be found on the current page.")
        return functionToExecute(*args,**kwargs)
        
    return validatePriorToExecution
    
def requiresAPreviouslyVisitedLocator(functionToExecute):
    def validatePriorToExecution(*args,**kwargs):
        self = args[0]
        if self.seleniumExecutionContext.lastVisitedLocation is None:
            raise LocatorNotFoundException( "No item was selected for this action to be done upon.")
        return functionToExecute(*args,**kwargs)
    return validatePriorToExecution