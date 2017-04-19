def getnumber():
	yield 101
	yield 202
	yield 333
	yield 666
	yield 444
	
gen=getnumber()
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))