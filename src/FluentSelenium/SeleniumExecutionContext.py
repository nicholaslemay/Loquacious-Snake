from selenium import selenium

class SeleniumExecutionContext:
    
    def __init__(self, host, port, browserStartCommand, url):
        print (host, port, browserStartCommand, url)
        self.seleniumInstance = selenium(host, port, browserStartCommand, url)
        self.isInitialized = False
    
    def initialize(self): 
        if not self.isInitialized:
            self.seleniumInstance.start()
            self.isInitialized = True
    
    def destroy(self):
        if self.isInitialized:
            self.seleniumInstance.stop()
            self.isInitialized = False