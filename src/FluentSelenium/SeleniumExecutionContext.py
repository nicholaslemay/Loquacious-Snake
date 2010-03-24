from selenium import selenium

class SeleniumExecutionContext:
    
    def __init__(self, host, port, browserStartCommand, url):
        self.selenium = selenium(host, port, browserStartCommand, url)
        self.isInitialized = False
    
    def initialize(self): 
        if not self.isInitialized:
            self.selenium.start()
            self.isInitialized = True
    
    def destroy(self):
        if self.isInitialized:
            self.selenium.stop()
            self.isInitialized = False