#u can use decorator using annotation
import time
def MyDecorator(fun):
    def wrapper():
        stime=time.time()
        fun()
        etime=time.time()
        return etime - stime
    return wrapper

@MyDecorator
def myfun():
    total = 0
    for i in range(10000000):
        total+= i
    print(total)
    
print(myfun())