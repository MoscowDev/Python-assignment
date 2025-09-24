#prompt three users to enter three different scores and store them in different variables.
#add the scores and divide the sum by three to get the average of the scores. store this process in a variable called average.
# use conditional statement to check if the average score meets a condition that qualifies it to print either, A,B,C,D OR F Where A is average score between 90 and 100, B is between 80 and 90, C is between 70 and 80, D is between 60 and 70, and F between 0 and 60.

numerical_score1  = int(input("Enter score: "))
numerical_score2  = int(input("Enter score: "))
numerical_score3  = int(input("Enter score: "))

average = (numerical_score1 + numerical_score2 + numerical_score3)//3
print(average)
if( average <= 100 and sum >= 90):
	print("Grade is:A ")
if(average <= 90 and sum > 80):
	print("Grade is:B ")
if(average <= 80 and sum > 70):
	print("Grade is:C ")
if(average <= 70 and sum > 60):
	print("Grade is:D ")
if(average <= 60 and sum > 0):
	print("Grade is:F ")