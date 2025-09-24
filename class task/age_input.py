#prompt two users to enter two different ages for father and son and store them in different variables.
#subtract father age from son age and store in a variable
#subtract the son from the variable to get the difference in years.
#use a conditional statement to print invalid when outcome is less than one or greater than 80.



fathers_age  = int(input("Enter score: "))
sons_age  = int(input("Enter score: "))



age_difference = fathers_age - sons_age
years_difference = age_difference - sons_age

print (years_difference)

if(years_difference < 1 and years_difference > 80 ):
	print("invalid")
