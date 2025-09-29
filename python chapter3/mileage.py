#3.11
gallon_used = 0

gallon_sum = 0

miles = 0

while(gallon_used != 0 ):
	gallon = int(input("Enter the gallons used(-1 to end):"))
	gallon_sum += gallon

	miles = int(input("Enter the miles driven: "))
	sum_miles +=miles

	trip = miles // gallon
	print("The miles per gallon for each trip is", trip)

	if(gallon < 0):
		total_trip = sum_gallon // sum_miles 
		print("The total miles per gallon for each trip is", total_trip)

