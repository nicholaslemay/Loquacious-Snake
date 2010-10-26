class JavascriptHelper:
    
    @staticmethod
    def GetjQueryWaitForAjaxCondition():
        return "selenium.browserbot.getCurrentWindow().jQuery.active == 0";
    
    @staticmethod
    def GetPrototypeWaitForAjaxCondition():
        return "selenium.browserbot.getCurrentWindow().Ajax.activeRequestCount == 0"
