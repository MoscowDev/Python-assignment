first_entry = int (input("Enter first number: "))

second_entry = int (input("Enter second number: "))

third_entry = int (input("Enter third number: "))

fourth_entry = int (input("Enter fourth number: "))



highest_number = second_entry

if(first_entry > highest_number):
 	highest_number = first_entry

if(third_entry > highest_number):
	highest_number = third_entry


if(fourth_entry > highest_number):
	highest_number = fourth_entry


print("highest number is: " , highest_number)


smallest_number = first_entry


if(third_entry < smallest_number):
	smallest_number = third_entry


if(second_entry < smallest_number):
	smallest_number = second_entry

if(fourth_entry < smallest_number):
	smallest_number = fourth_entry


print("smallest number is: " , smallest_number)

sum = first_entry + second_entry + third_entry + fourth_entry

print("The sum is: ", sum)

mean = sum//4

print("mean is" , mean)


median = (sum - smallest_number - highest_number )//2

print ("The median is: ", median)





