def MyDecorator(function):
    def around():
        print('Doing task before Function')
        function()
        print('Doing task after Function')
    return around   
def myfunction():
    print('Welcome')

call = MyDecorator(myfunction)    
call()


            