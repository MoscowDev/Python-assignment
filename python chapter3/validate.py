#3.1

for count in range(2):
	value = int(input('Enter an integer 1 or 2: '))
if value % 2 == 0:
	print(f'{value} is even')
elif value % 1 == 0:
	print(f'{value} is odd')
else:
	print('you entered wrong number')