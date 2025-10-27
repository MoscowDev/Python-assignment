from functools import reduce


numbers = (1,2,3,4,5,6,7,8,9)

another_number = 50

new = numbers + (another_number,)

print(new)


my_number = (1, 2, [3, 4], 5,)

my_number[2][1] = 99

print(my_number)



my_tuple = ('apple', 'banana', 'cherry')

fruits = list( my_tuple )

fruits.append('mango')

new_tuple = tuple(fruits)


print(new_tuple)



def get_even_numbers(even):
    return even % 2== 0
numbers = list(filter(get_even_numbers, range(1,21)))

print(numbers)



words =  ['cat', 'elephant', 'tiger', 'lion']

def extract_five_characters(word):

	return len(word) > 5

new_word = list(filter(extract_five_characters,words))

print(new_word)




tuples = [(1, 'A'), (4, 'B'), (2, 'C')]

def get_values_greater_than_two(number):
	return number[0] > 2


value = list(filter(get_values_greater_than_two,tuples))
print (value)




def get_numbers_divisibe_by_3_and_5(number):
	return number % 3 == 0 and number % 5 == 0
result = list(filter(get_numbers_divisibe_by_3_and_5,range(1,51)))

print(result)





my_words = ['level', 'world', 'madam', 'python']

def filter_all_palindrome(word):
    return word == word[::-1] 

palindromes = list(filter(filter_all_palindrome, my_words))

print(palindromes)




words = ['python', 'java', 'c++'] 

def convert_to_upper_case(word):

	return word.upper()

outcome = list(map(convert_to_upper_case,words))

print(outcome)
	


def square_numbers_1_to_10(numbers):	

	return numbers **2 

check = list(map( square_numbers_1_to_10,range(1,10)))

print (check)



names = ['john', 'mary', 'steve']

def capitalize_first_letters(words):

	return words[0].upper() + words[1:]
info = list(map(capitalize_first_letters,names))
print(info)


prices =  [100, 200, 300]

def add_10_percent_tax(number):

	return number * 1.1
report = list(map(add_10_percent_tax,prices))
print(report)




numbers = list(range(1,50))
def get_sum_of_number_1_to_50(num1,num2):

	return num1 + num2

check = reduce(get_sum_of_number_1_to_50,numbers)
print(check)


numbers = [3, 5, 9, 2, 8]
def get_maximum_mumber(number1,number2):
	if number1 > number2:
		return number1 
	else:
		return number2
check = reduce(get_maximum_mumber,numbers)

print(check)



my_strings =['I', 'love', 'Python']

def concatenate_strings(word1,word2):

	return word1 + " " + word2
answer = reduce( concatenate_strings,my_strings)
print(answer)


numbers =[1, 2, 3, 4]


def square(numb):
	return numb **2

def find_product_of_square_of_numbers(a,b):
	
	return a * b

result = map(square,numbers)


product = reduce(find_product_of_square_of_numbers,result)
print(product)




list_of_tuple =  [(1, 2), (3, 4), (5, 6)]

def get_sum_of_element(num):

	return sum(num)

def get_greater_than_five(num1):
	if num1 > 5:
		return num1

sums = list(map(get_sum_of_element,list_of_tuple ))

den = list(filter(get_greater_than_five, sums ))

print(den)



"""
data = ['123', '456', '789', 'abc', 'def']

def remove_non_numeric_strings(number):
	return number.isdigit()

print (remove_non_numeric_strings,number)
"""