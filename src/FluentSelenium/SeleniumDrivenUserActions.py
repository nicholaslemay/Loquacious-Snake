class SeleniumDrivenUserActions:
    
    def __init__(self, seleniumExecutionContext):
        self.seleniumExecutionContext = seleniumExecutionContext
        self.selenium = seleniumExecutionContext.selenium
    
    def goesTo(self, url):
        self.selenium.open(url)