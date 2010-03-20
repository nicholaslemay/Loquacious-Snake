from FluentSelenium.helpers.TestMethodDiscoveryHelper import TestMethodDiscoveryHelper
import unittest


class SeleniumDriverUserExpectations(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass

    @staticmethod
    def GetTestSuite():
        suite = unittest.TestSuite()
        suite.addTests(map(SeleniumDriverUserExpectations, TestMethodDiscoveryHelper.GetTestMethods(SeleniumDriverUserExpectations, "Selenium")))
        return suite 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()