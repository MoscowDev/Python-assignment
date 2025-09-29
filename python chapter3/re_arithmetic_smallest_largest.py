#3.8

sum = 0
product = 1

number_input = int(input("Enter a number: "))
minimum = number_input
maximum = number_input

for number in range(3):
	number = int(input("Enter a number: "))
	sum = sum + number 
	product = product * number

	if(number < minimum):
		minimum = number
	if(number > maximum):
		maximum = number

sum += number_input
product *= number_input

	
average = sum / 4

print("The sum is: " + str(sum))
print("The average is: " + str(average))
print("The product is: " + str(product))
print("The smallest number is: " + str(minimum))
print("The largest number is: " + str(maximum))

