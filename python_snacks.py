def is_even(number):
	if number % 2 == 0:
		return "Even"
	else:
      	 	return "Odd"

print(is_even(4))


def is_prime(number):
	if number % 2 == 0:
		return "Even"
	else:
      	 	return "Odd"

print(is_even(4))


def subtract(number, number1):
	sum = number + number1-number-number
	
	if number - number1 < 1:
		return sum 
	else:
      	 	return number - number1

print(subtract(4,6))



def divide(number, number1):
	if number1 == 0:
        	return 0
	else:
        	return number / number1

print(divide(0,7))



def is_square(number):

	square = number*number
	if number != square:
        	return "true"
	else:
        	return "false"

print(is_square(100))



def is_palindrome(number):

	if number > 10000:
		return "false"
	elif number% 10 == number%10:
		return "true"




def is_factorial_of(number):
    factorial = 1
    while number >= 1:
        factorial = factorial * number
        number -= 1
    return factorial

print(is_factorial_of(10))



def square_of(number):

	square = number*number
	return square

print(square_of(5))