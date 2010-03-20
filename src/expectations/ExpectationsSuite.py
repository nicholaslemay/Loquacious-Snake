
import unittest
from  SeleniumExecutionContextExpectations import SeleniumExecutionContextExpectations

if __name__ == '__main__':
    suite = SeleniumExecutionContextExpectations.GetTestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite) 