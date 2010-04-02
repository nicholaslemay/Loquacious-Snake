from FluentSelenium.SeleniumDrivenUserActions import SeleniumDrivenUserActions
from FluentSelenium.SeleniumDrivenUserExpectations import SeleniumDrivenUserExpectations


class UnknownMethodException(Exception):
    pass

class SeleniumDrivenUser:
    
    def __init__(self, seleniumExecutionContext):
        self.actions = SeleniumDrivenUserActions(seleniumExecutionContext)
        self.expectations = SeleniumDrivenUserExpectations(seleniumExecutionContext)

        self.actions.chainingElement = self
        self.expectations.chainingElement = self
        
    def __getattr__(self, name):
        if hasattr(self.actions, name):
            return getattr(self.actions, name)
            
        elif hasattr(self.expectations, name):
            return getattr(self.expectations, name)
        try:
            return getattr(self, name)
        except Exception:
            raise UnknownMethodException("SeleniumDrivenUser does not support the " + name +  " method")
    

    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return "SeleniumDrivenUser instance"