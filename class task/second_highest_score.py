first_user = int (input("Enter first number: "))
second_user = int (input("Enter first number: "))
third_user = int (input("Enter first number: "))


#second_highest = second_user


if first_user > second_user and first_user < third_user or first_user > third_user and first_user  < second_user :
	second_highest =  first_user

elif second_user > first_user and second_user < third_user or second_user > third_user and second_user < first_user:
	second_highest = second_user
else:
	second_highest = third_user

print(second_highest)