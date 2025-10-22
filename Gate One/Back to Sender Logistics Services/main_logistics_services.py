from sender_logistics_services_function import*

while True:
    menu = """
    SENDER LOGISTICS SERVICES
    ____________________________________________________
    |Collection Rate    | Amount per parcel |  Base Pay |
    |___________________|___________________|___________|                                                
    |1 -> Less than 50% |        160        |      5000 | 
    |___________________|___________________|___________|						     	
    |2 -> 50 - 59%      |        200        |      5000 |
    |___________________|___________________|___________|                                                
    |3 -> 60 - 69%      |        250        |      5000 | 
    |___________________|___________________|___________|                                                 
    |4 -> >=70%         |        500        |      5000 |  	
    |___________________|___________________|___________|	
    """
    print(menu)
		
    user = int(input("Enter operation: "))
    print (get_drivers_payment_per_day(user))
 
