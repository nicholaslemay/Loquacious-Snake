class LocatorNotFoundException(Exception):
    pass

class OptionNotFoundException(Exception):
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

def requiresAPreviouslySelectedOption(functionToExecute):
    def validatePriorToExecution(*args,**kwargs):
        self = args[0]
        if self.seleniumExecutionContext.optionBeingHandled is None:
            raise OptionNotFoundException( "No option was selected for this action to be done upon.")
        return functionToExecute(*args,**kwargs)
    return validatePriorToExecution


def resetsOptionBeingHandled(functionToExecute):
    def decorateFunctionWithOptionReset(*args,**kwargs):
        self = args[0]       
        returnValueFromFunctionToExecute = functionToExecute(*args,**kwargs)
        self.seleniumExecutionContext.setOptionBeingHandled(None)
        return returnValueFromFunctionToExecute
    return decorateFunctionWithOptionReset

def resetsLastVisitedLocator(functionToExecute):
    def decorateFunctionWithLocatorReset(*args,**kwargs):
        self = args[0]       
        returnValueFromFunctionToExecute = functionToExecute(*args,**kwargs)
        self.seleniumExecutionContext.setLastVisitedLocation(None)
        return returnValueFromFunctionToExecute
    return decorateFunctionWithLocatorReset   