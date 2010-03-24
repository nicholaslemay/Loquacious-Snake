from FluentSelenium.SeleniumExecutionContext import SeleniumExecutionContext
from FluentSelenium.helpers.TestMethodDiscoveryHelper import TestMethodDiscoveryHelper
import unittest
from mock import Mock
from selenium import selenium

class SeleniumExecutionContextExpectations(unittest.TestCase):

    def setUp(self):
        self.host    = "localhost"
        self.port    = "8080"
        self.browserStartCommand = "*firefox"
        self.url     = "http://localhost:8080"


    def tearDown(self):
        pass
    
    @staticmethod
    def GetTestSuite():
        suite = unittest.TestSuite()
        suite.addTests(map(SeleniumExecutionContextExpectations, TestMethodDiscoveryHelper.GetTestMethods(SeleniumExecutionContextExpectations, "Selenium")))
        return suite
    

    def SeleniumExecutionContextShouldCreateASeleniumInstanceWithTheRightParameters(self):
        

        
        mockedConstructor = Mock()
        mockedConstructor.return_value = None
        
        selenium.__init__ = mockedConstructor
         
        executionContext = SeleniumExecutionContext(self.host, self.port, self.browserStartCommand, self.url)
         
        self.assertEqual(mockedConstructor.call_args,((self.host, self.port, self.browserStartCommand, self.url),{}), "Selenium called with incorrect arguments")
        
        
    def SeleniumExecutionContextShouldStartSeleniumOnlyOnceWhenAskedToInitializedTwice(self):
        mockedStart = Mock()
        selenium.start = mockedStart
        executionContext = SeleniumExecutionContext(self.host, self.port, self.browserStartCommand, self.url)
        
        executionContext.initialize()
        executionContext.initialize()
        
        self.assertEquals(1, mockedStart.call_count)
    
    def SeleniumExecutionContextShouldRequireToHavenBeenInitiliazedToStopSeleniumWhenDestroyed(self):
        mockedStop = Mock()
        selenium.stop = mockedStop
        
        executionContext = SeleniumExecutionContext(self.host, self.port, self.browserStartCommand, self.url)
        executionContext.isInitialized = False
        executionContext.destroy()
        executionContext.isInitialized = True
        executionContext.destroy()
        self.assertEquals(1, mockedStop.call_count )
        
    def SeleniumExecutionContextShouldBeReinitializableWhenContextWasPreviouslyDestroyed(self):
        mockedStart = Mock()
        selenium.start = mockedStart
        
        mockedStop = Mock()
        selenium.stop = mockedStop
        
        executionContext = SeleniumExecutionContext(self.host, self.port, self.browserStartCommand, self.url)
        executionContext.initialize() 
        executionContext.destroy()
        executionContext.initialize() 
        
        self.assertEquals(2, mockedStart.call_count )
        
        
if __name__ == "__main__":
    suite = SeleniumExecutionContextExpectations.GetTestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
