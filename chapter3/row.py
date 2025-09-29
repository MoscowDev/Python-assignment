#3.3

#The code prints less than(<) 10 times when the remainder of row is odd and prints greater than (>) 10times when the column is even. the process continues until 10 times.

for row in range(10):
	for column in range(10):
		print('<' if row % 2 == 1 else '>', end='')
	print()