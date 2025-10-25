from functools import reduce



string_list = ["1", "2", "3"]

def convert_list_of_string(string_list):
	for list in string_list:
		return int(list)
print(list( map(convert_list_of_string,string_list )))



number_list = [0, 5, 10, 15,3,4]


def add_to_element(number_list):
	
	return number_list + 10
print(list( map(add_to_element,number_list)))



celsius = [0, 20, 37, 100]

def convert_temperature(celsius):
	return  celsius * 1.8 + 32

print(list(map(convert_temperature,celsius)))


values  = [1,None, 3, None, 5]

def remove_none_value(values):
	return values 

print(list(filter(remove_none_value,values)))




new_numbers = [1, 3, 4, 6, 9, 12]
def extract_numbers_divisible_by_three(numbers):
	if numbers % 3 == 0:

		return new_numbers

print(list(filter(extract_numbers_divisible_by_three,new_numbers)))




neg_numbers = [-2,-1, 0, 1, 2]
def get_positive_numbers(numbes):

		return int(numbes) >= 0
print(list(filter(get_positive_numbers,neg_numbers)))




student_dic = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 20},{'name': 'Tim', 'age': 34},{'name': 'Ben', 'age': 25}]

def select_element(numbers):
	 return numbers['age'] > 25
print(list(filter(select_element,student_dic)))

		
	

sum_numbers = [1, 2, 3, 4, 5]

def sum_of_numbers(sum,sum1):
	return sum + sum1

print(reduce(sum_of_numbers,sum_numbers))



product_numbers = [1, 2, 3]

def product_of_numbers(product,product1):
	return product * product1

print(reduce(product_of_numbers,product_numbers))



max_numbers = [3,7,2,9,1]

def max_of_numbers(max,max1):
	if max > max1:
		return max
	else:
		return max1

num = reduce(max_of_numbers,max_numbers)

print(num)	


words = ["Hello", " ", "World"]

def concatenate_string(string,string1):

	return string + string1

adder = reduce(concatenate_string,words)

print(adder)



list_of_dic = [{'a': 1}, {'b': 2}, {'c': 3}]

def merge_a_list_of_dic(dic,dic1):

	return {**dic , **dic1}

adde = reduce(merge_a_list_of_dic,list_of_dic)

print(adde)


list_of_num = [1, 2, 3]

def get_cummulative_sum(num2,num3):

	return num2 + num3**2

adde = reduce(get_cummulative_sum,list_of_num)

print(adde)


		