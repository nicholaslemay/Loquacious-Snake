from selenium import selenium

class SeleniumExecutionContext:
    
    def __init__(self, host, port, browserStartCommand, url):
        self.selenium = selenium(host, port, browserStartCommand, url)
        self.hasBeenInitialized = False
    
    def initialize(self): 
        if not self.hasBeenInitialized:
            self.selenium.start()
            self.hasBeenInitialized = True
