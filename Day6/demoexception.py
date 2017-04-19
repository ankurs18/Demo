try:
	open('file', 'r')
	result = 10/3
	
except ZeroDivisionError as err:
	print('Error in division expression: '+ str(err))	
	
except FileNotFoundError as err:
	print('Error in opening file: '+ str(err))	
	
finally:
	print('This will always execute')		