#u can use decorator using annotation
import time
def MyDecorator(fun):
    def wrapper(*arg):
        stime=time.time()
        if len(arg) == 1:
            fun(arg[0])
        else:
            fun()
        etime=time.time()
        return etime - stime
    return wrapper

class MyClass:
    def __init__(self):
        pass
    
    @MyDecorator
    def Myfact(self):
        fact = 1
        for i in range(1, 51):
            fact *=i
        print(fact)    

obj = MyClass()
print(obj.Myfact())
