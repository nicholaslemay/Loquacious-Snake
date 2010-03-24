class SeleniumDrivenUserActions:
    
    def __init__(self, seleniumExecutionContext):
        self.seleniumExecutionContext = seleniumExecutionContext
        self.chainingElement = self
    
    def __getSeleniumInstance(self):
        return self.seleniumExecutionContext.seleniumInstance
    
    def goesToURL(self, url):
        self.__getSeleniumInstance().open(url)
    
    def andThen(self):
        return self.chainingElement