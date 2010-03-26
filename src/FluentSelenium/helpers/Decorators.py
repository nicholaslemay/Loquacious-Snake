def chainable(functionToExecute):
    def chain(*args,**kwargs):
        self = args[0]
        functionToExecute(*args,**kwargs)
        return self.chainingElement
    return chain
    