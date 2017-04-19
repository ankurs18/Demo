def test():
    print('Hello World')
 
test()
print(test)
print(type(test))    

var = test
#this shows that fujnctions are variables in python and can be assigned to another varibale and also called from that variable
var()

def anotherfunc(arg):
    arg()
    
anotherfunc(var)    