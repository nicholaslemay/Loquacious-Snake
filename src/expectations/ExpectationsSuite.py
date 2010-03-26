from SharedSeleniumExecutionContextExpectations import SharedSeleniumExecutionContextExpectations

from expectations.SeleniumDrivenUserActionsExpectations import \
    SeleniumDrivenUserActionsExpectations
from expectations.SeleniumDrivenUserExpectations import \
    SeleniumDriverUserExpectations
from expectations.SeleniumDrivenUserExpectationsExpectations import \
    SeleniumDrivenUserExpectationsExpectations
import unittest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(SeleniumDrivenUserExpectationsExpectations,prefix="SeleniumDrivenUserExpectationsShould"))
    suite.addTests(unittest.makeSuite(SeleniumDrivenUserActionsExpectations,prefix="SeleniumDrivenUser"))
    suite.addTests(unittest.makeSuite(SeleniumDriverUserExpectations,prefix="SeleniumDrivenUser"))
    suite.addTests(unittest.makeSuite(SharedSeleniumExecutionContextExpectations,prefix="SharedSeleniumExecutionContext"))
    unittest.TextTestRunner(verbosity=2).run(suite) 