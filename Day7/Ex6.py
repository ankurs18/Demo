def MyGenerator():
    yield from range(10)
    
li=list(MyGenerator())
print(li)  

#========================

fh = open('test.txt', 'w')
fh.write('sample')  

with open('test2.txt', 'w') as fh1: fh1.write('This is demo')
