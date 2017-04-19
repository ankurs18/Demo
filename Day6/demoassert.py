
num = input('Enter Value')
try:
    assert int(num) > 0, 'Negative value entered'
    print('Square: ' + str(int(num) **2))
    
finally:
    print('Error')    