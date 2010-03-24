from FluentSelenium.SeleniumDrivenUserActions import SeleniumDrivenUserActions
from FluentSelenium.SeleniumDrivenUserExpectations import SeleniumDrivenUserExpectations


class UnknownMethodException(Exception):
    pass

class SeleniumDrivenUser:
    
    def __init__(self, seleniumExecutionContext):
        self.actions = SeleniumDrivenUserActions(seleniumExecutionContext)
        self.expectations = SeleniumDrivenUserExpectations(seleniumExecutionContext)

    def __getattr__(self, name):
        if hasattr(self.actions, name):
            return getattr(self.actions, name)
            
        elif hasattr(self.expectations, name):
            return getattr(self.expectations, name)
        else:
            raise UnknownMethodException("SeleniumDrivenUser does not support the " + name +  " method")