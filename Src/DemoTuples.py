'''
Created on Mar 31, 2017

@author: ankur.sethi
'''
tup=(10,20,'Max','Ankur')
tup=(10,20,231)
print(tup)
print(len(tup))
print(max(tup))
print('zero value',tup[0])
print('zero value',tup[-1])
print('zero value',tup[0:3])


#value to check
flag=10 in tup
print(flag)

#concat
newtup=tup+tup
print(newtup)
newtup=tup*2
print(newtup)

#deleting
del tup
print(tup)