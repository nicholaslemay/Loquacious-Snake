from FluentSelenium.SeleniumExecutionContext import SeleniumExecutionContext
from FluentSelenium.helpers.TestMethodDiscoveryHelper import TestMethodDiscoveryHelper
import unittest
from mock import Mock
from selenium import selenium

class SeleniumExecutionContextExpectations(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass
    
    @staticmethod
    def GetTestSuite():
        suite = unittest.TestSuite()
        suite.addTests(map(SeleniumExecutionContextExpectations, TestMethodDiscoveryHelper.GetTestMethods(SeleniumExecutionContextExpectations, "Selenium")))
        return suite
    

    def SeleniumExecutionContextShouldCreateASeleniumInstanceWithTheRightParameters(self):
        
        host    = "localhost"
        port    = "8080"
        browserStartCommand = "*firefox"
        url     = "http://localhost:8080"
        
        mockedConstructor = Mock()
        mockedConstructor.return_value = None
        
        selenium.__init__ = mockedConstructor
         
        executionContext = SeleniumExecutionContext(host, port, browserStartCommand, url)
         
        self.assertEqual(mockedConstructor.call_args,((host, port, browserStartCommand, url),{}), "Selenium called with incorrect arguments")
        

    


if __name__ == "__main__":
    suite = SeleniumExecutionContextExpectations.GetTestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
