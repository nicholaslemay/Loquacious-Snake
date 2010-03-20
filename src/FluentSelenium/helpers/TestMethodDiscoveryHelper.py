class TestMethodDiscoveryHelper:
    @staticmethod
    def GetTestMethods(className, prefix):
        methodNames=[]
        for methodName in dir(className):
            if str(methodName).startswith(prefix):
                methodNames.append(methodName)
        return methodNames