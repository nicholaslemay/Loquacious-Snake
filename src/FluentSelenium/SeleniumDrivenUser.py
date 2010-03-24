from FluentSelenium.SeleniumDrivenUserActions import SeleniumDrivenUserActions
from FluentSelenium.SeleniumDrivenUserExpectations import SeleniumDrivenUserExpectations


class UnknownMethodException(Exception):
    pass

class SeleniumDrivenUser:
    
    def __init__(self):
        pass
    

    def __getattr__(self, name):
        if hasattr(SeleniumDrivenUserActions, name):
            return getattr(SeleniumDrivenUserActions,name)
            
        elif hasattr(SeleniumDrivenUserExpectations, name):
            x = SeleniumDrivenUserExpectations()
            return getattr(x,name)
        else:
            raise UnknownMethodException("SeleniumDrivenUser does not support the " + name +  " method")
        