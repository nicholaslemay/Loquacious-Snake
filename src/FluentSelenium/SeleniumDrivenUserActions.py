class SeleniumDrivenUserActions:
    
    def __init__(self, seleniumExecutionContext):
        self.seleniumExecutionContext = seleniumExecutionContext
      
    
    def __getSeleniumInstance(self):
        return self.seleniumExecutionContext.seleniumInstance
    
    def goesToURL(self, url):
        self.__getSeleniumInstance().open(url)