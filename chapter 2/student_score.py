
first_user = int (input("Enter first number: "))
second_user = int (input("Enter first number: "))
third_user = int (input("Enter first number: "))

highest_score = second_user

if(first_user < highest_score):
 	highest_score = highest_score

if(third_user < highest_score):
	highest_score = highest_score


if(third_user > highest_score):
	highest_score = third_user

if(first_user > highest_score):
	highest_score = first_user


print("highest number is: " , highest_score)



