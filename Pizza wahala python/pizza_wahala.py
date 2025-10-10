

print ("""

			               PIZZA WAHALA
	``````````````````````````````````````````````````````````````````````````````
	| Pizza               Number of Slices 		                Price per box|
        ``````````````````````````````````````````````````````````````````````````````
	| 1->Sapa		        4			                2,500|
        ``````````````````````````````````````````````````````````````````````````````
	| 2->Small Money		6			                2,900|
        ``````````````````````````````````````````````````````````````````````````````
	| 3->Big boys                   8			                4'000|
	``````````````````````````````````````````````````````````````````````````````
	| 4->Odogwu		       12			                5,200|
        ````````````````````````````MAKE YOUR CHOICE``````````````````````````````````



""")

print(prompt)
print("Enter your pizza choice")
number = int(input("enter number of people: "))


match pizza_menu:

case "1" : print("Wow! You Choose sapa size")
print("enter number of Guest:  ")
people = input("enter number of people: ")

 box = people /4;
 totalSlice = 4 * box;
 remainder = 0;
 Amount = box * 2500;
 print("total amount is:" + Amount)
	if(people % 4 != 0):
	box = box + 1;
	
remainder = totalSlice - people

print("Number of boxes to buy " + box + " The total number of guest " + people + " total amount is " + Amount + " Number of leftover slice " + remainder);





case "2":print(" Wow! you Choose small money")

print("enter number of people:  ")
people = input("enter number of people: ")

box = people /6
totalSlice = 6 * box
remainder = 0
Amount = box * 2900
print("total amount is:" + Amount)
if(people % 6 != 0):
box = box + 1
	
remainder = totalSlice - people

print("Number of boxes to buy " + box + " The total number of guest " + people + " total amount is " + Amount + " Number of leftover slice " + remainder)




case " 3":print(" Wow! You Choose Big Boys")

print("enter number of people:  ")
people = input("enter number of people: ")

box = people /8
totalSlice = 8 * box
remainder = 0
Amount = box * 4000
print("total amount is:" + Amount)
if(people % 8 != 0):
box = box + 1
	
remainder = totalSlice - people

print("Number of boxes to buy " + box + " The total number of guest " + people + " total amount is " + Amount + " Number of leftover slice " + remainder)




case "4":print(" Wow! Choose Odogwu")

print("enter number of people:  ")

people = input("enter number of people: ")
box = people /12
totalSlice = 12 * box
remainder = 0
Amount = box * 5200
print("total amount is:" + Amount)
if(people % 12 != 0):
	box = box + 1
	
remainder = totalSlice - people

print("Number of boxes to buy " + box + " The total number of guest " + people + " total amount is " + Amount + " Number of leftover slice " + remainder)








