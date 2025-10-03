

print ( """
WELCOME TO NOKIA App

1-> Phone book
2-> Messages
3-> Chat
4-> Call register
5-> Tones
6-> Settings
7-> Call divert
8-> Games
9-> Calculator
10-> Reminders
11-> Clock
12-> Profile
13-> SIM services

""")

user = (input("Enter a number "))

match nokia_phone:
	case "1":
		print("phone book")
		print ("""
		
		PHONE BOOK MENU:
		1-> Search
		2-> Service Nos.
		3-> Add name
		4-> Erase
		5-> Edit
		6-> Assign tone
		7-> Send b'card
		8-> Options
		9-> Speed dials
		10-> Voice tags""")


		phone_book_menu = input("enter a number")



match phone_book_menu:
	case "1": print("You entered search")
	case "2": print(" You entered service number") 
	case "3": print(" You added name")
	case "4": print(" You Erased")
	case "5": print(" You can Edit")
	case "6": print(" Assign tone")
	case "7": print(" Send b'card")
	case "8":

		option = ("""
		1-> Types of view
		2-> Memory Status
	
	""")

		option_select = input("enter a number")

match option_select:

	case "1": print("Types of view availabe")
	case "2": print("check your memory status")


	

	case "9":print("Enter Speed dial")
	case "10":print(" Select voice tag")






	case "2": 
        	
		print("Enter Message")
		message = ("""

		1-> Write messages
		2-> Inbox
		3-> Outbox
		4-> Picture messages
		5-> Templates
		6-> Smileys
		7-> Message settings
		8-> Info service
		9-> Voice mailbox number
		10 -> Service command editor

	""")

		print(message)
		message_select = input("enter a number")

		match message_select:

			case "1": print("write a message")
			case "2": print(" check inbox")
			case "3": print("Check outbox")
			case "4": print("see picture mesages")
			case "5": print("check templates")
			case "6": print(" smileys ")
			case "7": print("go to message settings")

			
		settings =( """

			1-> Set 1
			2-> Common

		""")

		print(settings)
		settings_select = input("enter a number")

		match settings_select:

			case "1": print("Set 1 options")

		setone = ("""

		1-> Message Center number
		2-> Messages sent as
		3-> Message validity

		""")


		print("setone")
		set_select = input("enter a number")


		match set_select:
		
			case "1": print("Here is a message centre number")
			case "2": print(" Message sent as")
			case "3": print("Message validity")




			case "2": print(" common info")

		common = ("""

		1-> Delivery report
		2-> Reply via same centre
		3-> Character support

		""")
		
		print("common")

		common_select = input("enter a number")


		match common_select:
		
			case "1": print(" Delivery report")
			case "2": print(" Reply via same centre")
			case "3": print(" Character support")




			case "8": print("check out service info")
			case "9": print("voice mail box number")	
			case "10": print("edit service command")





	case "3": print(" Chat")



	case "4": 

		print(" Call register")

		register = ("""

		1-> Missed calls
		2-> Received calls
		3-> Dialled numbers
		4-> Erase recent call lists
		5-> Show call duration
		6-> Show call costs
		7-> Call cost settings
		8-> Prepaid credit
		9-> Character support


""")

		print("register")


		register_select = input("enter a number")
		
		match register_select:

			case "1": print("Missed calls")
			case "2": print("Received calls")
			case "3": print("Dialled numbers")
			case "4": print( "Erase recent call lists")

 
	case "5":
		print( "Show call duration")

		duration = ("""
		
		1-> Last call duration
		2-> All calls' duration
		3-> Received calls' duration
		4-> Dialled calls' duration
		5-> Clear timers
		6-> Show call costs
		7-> Call cost settings
		8-> Prepaid credit

""")

		print("duration")
		duration_selection = input("enter a number")
		
		match duration_selection:

			case "1":print(" Last call duration")
			case "2":print("All calls' duration")
			case "3":print("Received calls' duration")
			case "4":print("Dialled calls' duration")
			case "5":print("Clear timer")
			case "6":print("Show call costs")



		costs = ("""
		
		1-> Last calls
		2-> All calls' cost
		3-> Clear counters
		
""")

		print("costs")
		cost_selection = input("enter a number")
		
		match cost_selection:

			case "1": print(" Last calls ")
			case "2": print("All calls' cost")
			case "3": print("Clear counters")



		
	case "7": 
		print( "Call cost settings")
		
		costSettings = ("""

		1-> Call cost limit
		2-> Show costs in
""")


		print("costSettings")

		callSetting_selection = input("enter a number")
		
		match callSetting_selection:

			case "1": print("Call cost limit ")
			case "2": print("Show costs in")



	case "8": print("Prepaid credit") 
	case "9": print("Character support")




	case "5":
		print("Tones")
		tones = ("""

		1-> Ringing tone
		2-> Ringing volume
		3-> Incoming call alert
		4-> Composer
		5-> Message alert tone
		6-> Keypad tones
		7-> Warning and game tones
		8-> Vibrating alert
		9-> Screen saver
""")


		print("Tones")
		tone_selection = input("enter number")
		match tone_selection:
			case "1": print("Ringing tone")
			case "2": print(" Ringing volume")
			case "3": print("Incoming call alert")
			case "4": print("Composer")
			case "5": print("Message alert tone")
			case "6": print("Keypad tones")
			case "7": print("Warning and game tones")
			case "8": print(" Vibrating alert")
			case "9": print("Screen saver")




	case 6:
		print(" Settings")
		settings =( """

		1-> Call settings
		2-> Phone settings
		3-> Security settings
		4-> Restore factory settings
	

""")

		print("settings")
		settings_selection = input("enter a number")
		match settings_election:
		


			case "1":
				print("Call settings")
 						callsetting_selection ("""
						1-> Automatic redial
						2-> Speed dialling
						3-> Call waiting options
						4-> Own number settings
						5-> Phone line in use
						6-> Automatic answer

""")

		print("callSetting")
		callSetting_selection = input("enter a number")

		match = callSetting_selection:

			case "1"->print("Automatic redial")
			case "2"->print(" Speed dialling")
			case "3"->print("Call waiting options")
			case "4"->print(" Own number settings")
			case "5"->print("Phone line in use")
			case "6"->print("Automatic answer")



	case "2":
		 print("Phone settings")

		 phoneSetting = ("""

		1-> Language
		2-> Cell info display
		3-> Welcome note
		4-> Network selection
		5-> Lights
		6-> Confirm SIM service actions

""")

	print("phoneSetting")
	
	phoneSetting_selection = input("enter a number")

	match = phoneSetting_selection:

case "1"-> print("Language")
case "2"-> print("  Cell info display")
case "3"-> print("Welcome note")
case "4"-> print(" Network selection")
case "5"-> print("Lights")
case "6"-> print("Confirm SIM service actions")





case "3"->print("Security settings")

String securitySetting = """
 
	1-> PIN code request
	2-> Call barring service
	3-> Fixed dialling
	4-> Closed user group
	5-> Phone security
	6-> Change access codes

"""

	print(securitySetting)
	securitySetting_selection = input("enter a number")

	match = securitySetting_selection:

case "1"->print(" PIN code request")
case "2"->print("Call barring service")
case "3"->print("Fixed dialling")
case "4"->print(" Closed user group")
case "5"->print("Phone security")
case "6"->print("Change access codes")





case "4"-> println("Restore factory settings")





case "7"->print("Call divert")
case "8"->print("Games")
case "9"->print("  Calculator")
case "10"->print("Reminders")


case "11"->print("Clock")

String clock = """
	1-> Alarm clock
	2-> Clock settings
	3-> Date settings
	4-> Stopwatch
	5-> Countdown timer
	6-> Auto update of date and time

"""

print(clock)

clock_selection = input("enter a number")

match = clock_selection:

case "1"-> print(" Alarm clock")
case "2"-> print("Clock settings")
case "3"-> print("Date settings")
case "4"-> print(" Stopwatch")
case "5"-> print("Countdown timer")
case "6"-> print("Auto update of date and time")



case "12"->print(" Profiles")
case "13"->print(" SIM services")

