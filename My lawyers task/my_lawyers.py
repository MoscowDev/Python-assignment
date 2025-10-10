"""import random
def get_random_number(number1, number2):
	for index in random.sample(range(number1, number2)):
		return index"""


def get_length(number):
	number_element = 0
	for index in number:
		number_element += 1
	return number_element



def even_length(number):
	sum = 0
	length = len(number) - 1
	for count in range(0, len(number), 2):
		sum += number[count]
	return sum




def average(array):
    total = 0
    for count in range(len(array)):
        total += array[count]
    average = total / len(array)
    return average


def find_largest(number):
	largest = number[0]
	for count in range(len(number)):
		if largest < number[count]:
		 largest = number[count]
	return largest




def find_smallest(number):
    smallest = number[0]

    for count in range(len(number)):
        if smallest[count] < smallest:
            smallest = number[count]
    
    return smallest



def get_sequence(number):
	count = 0
	for index in range(len(number)):
		count += 1
	return number

	


	
	
		 

number1 = [1,3,6,8,7,2 ]

print(get_random_number(number1, number2))
print(get_length(number))
print(even_length(number))
print(average(array))
print(find_largest(number))
print(find_smallest(number))
print(get_sequence(number))
