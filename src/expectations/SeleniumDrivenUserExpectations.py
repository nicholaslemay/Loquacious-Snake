from mock import Mock
from FluentSelenium.SeleniumDrivenUser import SeleniumDrivenUser
from FluentSelenium.SeleniumDrivenUserActions import SeleniumDrivenUserActions
from FluentSelenium.SeleniumDrivenUserExpectations import SeleniumDrivenUserExpectations
import unittest


class SeleniumDriverUserExpectations(unittest.TestCase):
    
    def setUp(self):
        self.originalGoesToMethod = SeleniumDrivenUserActions.goesTo
        self.originalShouldBeOnPage = SeleniumDrivenUserExpectations.shouldBeOnPage       
        self.mockedContext = Mock(spec=["initialize"])
    
    def tearDown(self):
        SeleniumDrivenUserActions.goesTo = self.originalGoesToMethod  
        SeleniumDrivenUserExpectations.shouldBeOnPage = self.originalShouldBeOnPage  
        
    def SeleniumDrivenUserShouldCallAppropriateActionMethodInExpectationWhenCalledWithAnAction(self):
   
            mockedGoesToURL = Mock()
            SeleniumDrivenUserActions.goesTo = mockedGoesToURL
            
            bob = SeleniumDrivenUser(self.mockedContext)
            bob.goesTo("http://www.google.ca")
    
            self.assertTrue( mockedGoesToURL.called)
    
    def SeleniumDrivenUserShouldCallAppropriateActionMethodInExpectationWhenCalledWithAnExpectation(self):
            mockedShouldBeOnPage = Mock()
            mockedGoesTo = Mock()
            SeleniumDrivenUserActions.goesTo = mockedGoesTo
            SeleniumDrivenUserExpectations.shouldBeOnPage = mockedShouldBeOnPage
            
            bob = SeleniumDrivenUser(self.mockedContext)
            bob.goesTo("http://www.google.ca")
            bob.shouldBeOnPage("http://www.google.ca")
            self.assertTrue( mockedGoesTo.called)         

    def SeleniumDrivenUserShouldThrowAnExceptionWhenTheMethodIsUnkownToBothActionsAndExpectations(self):
       
        try:
            bob = SeleniumDrivenUser(self.mockedContext)
            bob.unknownMethodCall()
            self.fail("unknownMethodCall should of raised an exception")
        except Exception, instance:
            pass
          
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()