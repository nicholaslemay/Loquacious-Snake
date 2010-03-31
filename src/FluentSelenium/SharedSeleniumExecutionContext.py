from selenium import selenium

class SharedSeleniumExecutionContext:
    
    host =None
    port =None
    browserStartCommand =None
    url = None
    seleniumInstance=None
    isInitialized=False
    lastVisitedLocation=None
    
    def __init__(self, host, port, browserStartCommand, url):
        if SharedSeleniumExecutionContext.seleniumInstance == None:
            SharedSeleniumExecutionContext.seleniumInstance = selenium(host, port, browserStartCommand, url)
        self.seleniumInstance = SharedSeleniumExecutionContext.seleniumInstance
        self.isInitialized = SharedSeleniumExecutionContext.isInitialized
        self.setBrowserStartCommand(browserStartCommand)
        self.setPort(port)
        self.setURL(url)
        self.setHost(host)
        self.setLastVisitedLocation(None)
        
    def setPort(self, port):
        self.port = port
        SharedSeleniumExecutionContext.port = port
        SharedSeleniumExecutionContext.seleniumInstance.port = port
        
    def setHost(self, host):
        self.host = host
        SharedSeleniumExecutionContext.host= host
        SharedSeleniumExecutionContext.seleniumInstance.host = host
        
    def setBrowserStartCommand(self, browserStartCommand):
        self.browserStartCommand = browserStartCommand
        SharedSeleniumExecutionContext.__browserStartCommand = browserStartCommand
        SharedSeleniumExecutionContext.seleniumInstance.browserStartCommand = browserStartCommand
    
    def setURL(self, url):
        self.url = url
        SharedSeleniumExecutionContext.url = url
        SharedSeleniumExecutionContext.seleniumInstance.browserURL = url
        
    def setLastVisitedLocation(self, location):
        self.lastVisitedLocation = location
        SharedSeleniumExecutionContext.lastVisitedLocation = location
        
    def initialize(self):         
        if not SharedSeleniumExecutionContext.isInitialized and self.seleniumInstance:
            self.seleniumInstance.start()
            SharedSeleniumExecutionContext.isInitialized = True
    
    def destroy(self):
        if SharedSeleniumExecutionContext.isInitialized:
            SharedSeleniumExecutionContext.resetAll()
    
    def __del__(self):  
        if self.isInitialized:
            self.seleniumInstance.stop()
            
    @staticmethod
    def resetAll():
        if SharedSeleniumExecutionContext.isInitialized and SharedSeleniumExecutionContext.seleniumInstance:
            SharedSeleniumExecutionContext.seleniumInstance.stop()

        SharedSeleniumExecutionContext.host =None
        SharedSeleniumExecutionContext.port =None
        SharedSeleniumExecutionContext.browserStartCommand =None
        SharedSeleniumExecutionContext.url = None
        SharedSeleniumExecutionContext.seleniumInstance=None
        SharedSeleniumExecutionContext.isInitialized=False