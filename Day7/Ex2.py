def Parent(num):
    
    def childfun1():
        print('Msg from child 1')
        
    def childfun2():
        print('Msg from child2')
            
    if num>10:
        return childfun1
    else:
        return childfun2
    
child = Parent(11)
print(type(child)) 
child()   
    