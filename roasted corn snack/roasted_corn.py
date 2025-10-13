def get_longest_word(values):
	

	longest = ""

	for index in values:
		if len(index) > len(longest):
			longest = index
	length_longest = len(longest)
	
	return longest, length_longest

	
values = ["stan","udeme", "destiny", "Emmanuel"]

print(get_longest_word(values))




def get_minimum_number(numbers):

    minimum = numbers[0]

    for count in range(len(numbers)):
        if numbers[count] < minimum:
            minimum = numbers[count]
    
    return minimum

numbers = [1,2,3,5,6,8,9,45,3]

print(get_minimum_number(numbers))



def get_maximum_number(numbers):

    maximum = numbers[0]

    for count in range(len(numbers)):
        if numbers[count] > maximum:
            maximum = numbers[count]
    
    return maximum

numbers = [1,2,3,5,6,8,9,45,3]

print(get_maximum_number(numbers))




def get_list_square(List):


    for count in range(len(List)):
 
              List[count] = List[count]**2
    
    return List

List = [2,3,4,5,7]

print(get_list_square(List))




def get_sum_square(List):

	sum = 0
	for count in range(len(List)):
 
              	sum += List[count]**2
    
	return sum

List = [2,3,4,5,7]

print(get_sum_square(List))


def get_a_string(string):

	odd = ""
	for count in range(len(string)):
 
		if count % 3 != 0:
			odd += string[count]
    
	return odd

string = ["stan","udeme", "destiny", "Emmanuel"]

print(get_a_string(string))





def square(number):

	return number**2


print(square(10))



def get_two_inputs(string, number):

	odd=""
	for count in range(len(number)):
 
		if number[count] == string :
			odd = string * number[count] 

    
	return odd

string = ["stan",5]

print(get_two_inputs("stan", 5))




