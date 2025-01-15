

class MetaSingleton(type):

    __instances = {}

    def __call__(self, *args, **kwds):
        if self not in self.__instances:
            self.__instances[self] = super(MetaSingleton, self).__call__(*args, **kwds)
        return self.__instances[self]
    

class Logger(metaclass=MetaSingleton):
    pass


log1 = Logger()
print(f'Log 1: {id(log1)}')


log2 = Logger()
print(f'Log 2: {id(log2)}')