from _functools import reduce

fun = lambda x: x+1
v= fun(100)
print(v)
print('----------------')

fun1 = lambda x, y: x+y
print(fun1(4,5))
print('----------------')

list1 = [34,56,121,75,21]
print(reduce(lambda x,y: x+y,list1))
print('----------------')

names = ['Ankur', 'sas', 'Accenture']
lenNames = map(lambda s: len(s), names)
result=reduce(lambda s1, s2:s1 +s2 , lenNames)
print(result)

print('----------------')

listnum=[48,11,12,95,36]
newlist=filter(lambda num: num%4==0,listnum)
for v in newlist:
    print(v)