from FluentSelenium.SharedSeleniumExecutionContext import SharedSeleniumExecutionContext
import unittest
from mock import Mock
from selenium import selenium

class SharedSeleniumExecutionContextExpectations(unittest.TestCase):
       
    def setUp(self):
        self.host    = 'localhost'
        self.port    = 4444
        self.browserStartCommand = '*firefox'
        self.url     = 'http://www.google.com/'
        self.originalSeleniumInit = selenium.__init__
        self.originalSeleniumStart = selenium.start
        self.originalSeleniumStop = selenium.stop
        
    def tearDown(self):
        selenium.__init__ = self.originalSeleniumInit  
        selenium.start = self.originalSeleniumStart  
        selenium.stop = self.originalSeleniumStop  
       
    def SharedSeleniumExecutionContextShouldRevertAllValuesWhenResetAllIsCalled(self):
        SharedSeleniumExecutionContext.port = 666
        SharedSeleniumExecutionContext.url = "http://google.com"
        SharedSeleniumExecutionContext.resetAll()
        self.assertEquals((SharedSeleniumExecutionContext.port,SharedSeleniumExecutionContext.url),(None,None))
        
    def SharedSeleniumExecutionContextShouldCreateASeleniumInstanceWithTheRightParameters(self):
        
        mockedConstructor = Mock()
        mockedConstructor.return_value = None
        
        selenium.__init__ = mockedConstructor
        SharedSeleniumExecutionContext.resetAll()
        SharedSeleniumExecutionContext(self.host, self.port, self.browserStartCommand, self.url)
        
        self.assertEqual(mockedConstructor.call_args,((self.host, self.port, self.browserStartCommand, self.url),{}), "Selenium called with incorrect arguments")
        
        
    def SharedSeleniumExecutionContextShouldStartSeleniumOnlyOnceWhenAskedToInitializeTwice(self):
        mockedStart = Mock()
        selenium.start = mockedStart
        SharedSeleniumExecutionContext.resetAll()
        executionContext = SharedSeleniumExecutionContext(self.host, self.port, self.browserStartCommand, self.url)
        
        executionContext.initialize()
        executionContext.initialize()
        
        self.assertEquals(1, mockedStart.call_count)
    
    def SharedSeleniumExecutionContextShouldRequireToHavenBeenInitiliazedToStopSeleniumWhenDestroyed(self):
        mockedStart = Mock()
        selenium.start = mockedStart
        
        mockedStop = Mock()
        selenium.stop = mockedStop
        
        SharedSeleniumExecutionContext.resetAll()
        executionContext = SharedSeleniumExecutionContext(self.host, self.port, self.browserStartCommand, self.url)
       
        executionContext.initialize()
        executionContext.destroy()
        executionContext.destroy()
        
        self.assertEquals(1, mockedStop.call_count )
        
    def SharedSeleniumExecutionContextShouldBeReinitializableWhenContextWasPreviouslyDestroyed(self):
        mockedStart = Mock()
        selenium.start = mockedStart
        
        mockedStop = Mock()
        selenium.stop = mockedStop
        SharedSeleniumExecutionContext.resetAll()
        executionContext = SharedSeleniumExecutionContext(self.host, self.port, self.browserStartCommand, self.url)
        
        executionContext.initialize() 
        executionContext.destroy()
        
        executionContext.initialize() 
        
        
        self.assertEquals(2, mockedStart.call_count )
    
        
if __name__ == "__main__":
    suite = unittest.makeSuite(SharedSeleniumExecutionContextExpectations, prefix="SharedSeleniumExecutionContext")
    unittest.TextTestRunner(verbosity=2).run(suite)
