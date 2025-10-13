#4.3

def cube(x):
	x ** 3

print('The cube of 2 is', cube(2))

# It doesn't have a return statement




#4.4
def mystery(x):
	y = 0
	for value in x:
		y += value ** 2
	return y

# If the list(x) is [1,2,3,4,5] The function will return the sum of the square of the elements(55)


#4.13
def get_product(*numbers):
	counter = 0
	sum = 1
	while counter < len(numbers):
		sum *= numbers[count]
		count += 1
	return sum

print(get_product(2,4,8,10))



#4.7
import datetime

def get_date_and_time():
	print(datetime.datetime.today())

get_date_and_time()



#4.8

def round(number, number):

number = 13.56449

print(round(number))
print(round(number,1))
print(round(number,2))
print(round(number,3))


#4.5
def seconds_since_midnight(hours, minutes, seconds):
	hour_in_seconds = hours * 3600
	minute_in_seconds = minutes * 60
	return hour_in_seconds + minute_in_seconds + seconds

print(seconds_since_midnight(13, 30, 45))



