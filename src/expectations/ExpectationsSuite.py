from expectations.SeleniumDrivenUserExpectations import SeleniumDriverUserExpectations
from expectations.SeleniumDrivenUserActionsExpectations import SeleniumDrivenUserActionsExpectations
from expectations.SeleniumDrivenUserExpectationsExpectations import SeleniumDrivenUserExpectationsExpectations

import unittest
from  SeleniumExecutionContextExpectations import SeleniumExecutionContextExpectations

if __name__ == '__main__':
    suite = SeleniumExecutionContextExpectations.GetTestSuite()
    suite.addTests(SeleniumDriverUserExpectations.GetTestSuite())
    suite.addTests(SeleniumDrivenUserActionsExpectations.GetTestSuite())
    suite.addTests(SeleniumDrivenUserExpectationsExpectations.GetTestSuite())
    unittest.TextTestRunner(verbosity=2).run(suite) 