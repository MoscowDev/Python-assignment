import java.util.Scanner;

public class NokiaOne{
public static void main(String [] args){
String prompt = """
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

""";

System.out.println(prompt);
Scanner scanner = new Scanner(System.in);
int myCollections = scanner.nextInt();

switch(myCollections){
case 1->
	{System.out.print("you entered Phone book");
	String phonebook = """

	1-> Search
	2-> Service Nos.
	3-> Add name
	4-> Erase
	5-> Edit
	6-> Assign tone
	7-> Send b'card
	8-> Options
	9-> Speed dials
	10-> Voice tags
	""";
	System.out.print(phonebook);
	int phoneBookResponse = scanner.nextInt();
	switch(phoneBookResponse){

case 1->{System.out.println("You entered search");}
case 2->{System.out.println(" You entered service number");}
case 3->{System.out.println(" You added name");}
case 4->{System.out.println(" You Erased");}
case 5->{System.out.println(" You can Edit");}
case 6->{System.out.println(" Assign tone");}
case 7->{System.out.println(" Send b'card");}
case 8->{
	String option = """
	1-> Types of view
	2-> Memory Status
	
	""";

	System.out.print(option);
	int optionSelect = scanner.nextInt();
	switch(optionSelect){
		case 1-> {System.out.println("Types of view availabe");}
		case 2-> {System.out.println("check your memory status");}

}
}
	

case 9->{System.out.println("Enter Speed dial");}
case 10->{System.out.println(" Select voice tag");}
}		
}

// phone book done and dusted

/*System.out.println(prompt)
Scanner scanner = new Scanner(System.in);
int messageCollections = scanner.nextInt();

switch(messageCollections){  */

case 2-> {
        {System.out.print("Enter Message");
	String message = """

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

	""";

	System.out.print(message);
	int messageSelect = scanner.nextInt();
	switch(messageSelect){
		case 1-> {System.out.println("write a message");}
		case 2-> {System.out.println(" check inbox");}
		case 3-> {System.out.println("Check outbox");}
		case 4-> {System.out.println("see picture mesages");}
		case 5-> {System.out.println("check templates");}
		case 6-> {System.out.println(" smileys ");}


		case 7-> {System.out.println("go to message settings");
			String settings = """

		1-> Set 1
		2-> Common

		""";

		System.out.print(settings);
		int settingsSelect = scanner.nextInt();
		switch(settingsSelect){

		case 1-> {System.out.println("Set 1 options");

		String setOne = """

		1-> Message Center number
		2-> Messages sent as
		3-> Message validity

		""";
		System.out.print(setOne);
		int setSelect = scanner.nextInt();
		switch(setSelect){
		
		case 1-> {System.out.println("Here is a message centre number");}
		case 2-> {System.out.println(" Message sent as");}
		case 3-> {System.out.println("Message validity");}

}
		
}


		case 2-> {System.out.println(" common info");

		String common = """

		1-> Delivery report
		2-> Reply via same centre
		3-> Character support

		""";
		System.out.print(common);
		int commonSelect = scanner.nextInt();
		switch(commonSelect){
		
		case 1-> {System.out.println(" Delivery report");}
		case 2-> {System.out.println(" Reply via same centre");}
		case 3-> {System.out.println(" Character support");}
}
}

}
}

		case 8-> {System.out.println("check out service info");}
		case 9-> {System.out.println("voice mail box number");}	
		case 10-> {System.out.println("edit service command");}



}
}
}

// Messages done and dusted


case 3->{System.out.println(" Chat");}

// Chats has nothing to nest. Done and dusted

case 4->{System.out.println(" Call register");

		String register = """

		1-> Missed calls
		2-> Received calls
		3-> Dialled numbers
		4-> Erase recent call lists
		5-> Show call duration
		6-> Show call costs
		7-> Call cost settings
		8-> Prepaid credit
		9-> Character support


""";

		System.out.print(register);
		int registerSelect = scanner.nextInt();
		
		switch(registerSelect){

		case 1-> {System.out.println("Missed calls");}
		case 2-> {System.out.println("Received calls");}
		case 3-> {System.out.println("Dialled numbers");} 
		case 4-> {System.out.println( "Erase recent call lists");}

 
		case 5-> {System.out.println( "Show call duration");

		String duration = """
		
		1-> Last call duration
		2-> All calls' duration
		3-> Received calls' duration
		4-> Dialled calls' duration
		5-> Clear timers
		6-> Show call costs
		7-> Call cost settings
		8-> Prepaid credit
""";

		System.out.println(duration);
		int durationSelection = scanner.nextInt();
		
		switch( durationSelection){

		case 1->{System.out.println(" Last call duration");}
		case 2->{System.out.println("All calls' duration");}
		case 3->{System.out.println("Received calls' duration");}
		case 4->{System.out.println("Dialled calls' duration");}
		case 5->{System.out.println("Clear timer");}
		
		


}
}



		case 6-> {System.out.println("Show call costs");
		String costs = """
		
		1-> Last calls
		2-> All calls' cost
		3-> Clear counters
		
""";
		System.out.print(costs);
		int costSelection = scanner.nextInt();
		
		switch(costSelection){

		case 1->{System.out.println(" Last calls ");}
		case 2->{System.out.println("All calls' cost");}
		case 3->{System.out.println("Clear counters");}

}

} 

		
		case 7-> {System.out.println( "Call cost settings");
		
		String costSettings = """

		1-> Call cost limit
		2-> Show costs in
""";

		System.out.print(costSettings);
		int callSettingSelection = scanner.nextInt();
		
		switch(callSettingSelection){

		case 1->{System.out.println("Call cost limit ");}
		case 2->{System.out.println("Show costs in");}
}

}


		case 8-> {System.out.println("Prepaid credit");} 
		case 9-> {System.out.println("Character support");} 




}
}




case 5->{System.out.println("Tones");
	String tones = """
	1-> Ringing tone
	2-> Ringing volume
	3-> Incoming call alert
	4-> Composer
	5-> Message alert tone
	6-> Keypad tones
	7-> Warning and game tones
	8-> Vibrating alert
	9-> Screen saver
""";

	System.out.println(tones);
	int toneSelection = scanner.nextInt();
	
  	switch(toneSelection ){
case 1->{System.out.println("Ringing tone");}
case 2->{System.out.println(" Ringing volume");}
case 3->{System.out.println("Incoming call alert");}
case 4->{System.out.println("Composer");}
case 5->{System.out.println("Message alert tone");}
case 6->{System.out.println("Keypad tones");}
case 7->{System.out.println("Warning and game tones");}
case 8->{System.out.println(" Vibrating alert");}
case 9->{System.out.println("Screen saver");}

}
}


case 6->{System.out.println(" Settings");
String settings = """

	1-> Call settings
	2-> Phone settings
	3-> Security settings
	4-> Restore factory settings
	

""";

	System.out.println(settings);
	int settingsSelection = scanner.nextInt();

	switch(settingsSelection){

case 1->{System.out.println("Call settings");
String callSetting = """
 
	1-> Automatic redial
	2-> Speed dialling
	3-> Call waiting options
	4-> Own number settings
	5-> Phone line in use
	6-> Automatic answer

""";

	System.out.println(callSetting);
	int callSettingSelection = scanner.nextInt();

	switch(callSettingSelection){

case 1->{System.out.println("Automatic redial");}
case 2->{System.out.println(" Speed dialling");}
case 3->{System.out.println("Call waiting options");}
case 4->{System.out.println(" Own number settings");}
case 5->{System.out.println("Phone line in use");}
case 6->{System.out.println("Automatic answer");}
}
}


case 2->{System.out.println("Phone settings");

String phoneSetting = """

	1-> Language
	2-> Cell info display
	3-> Welcome note
	4-> Network selection
	5-> Lights
	6-> Confirm SIM service actions

""";

	System.out.println(phoneSetting);
	int phoneSettingSelection = scanner.nextInt();

	switch(phoneSettingSelection){

case 1->{System.out.println("Language");}
case 2->{System.out.println("  Cell info display");}
case 3->{System.out.println("Welcome note");}
case 4->{System.out.println(" Network selection");}
case 5->{System.out.println("Lights");}
case 6->{System.out.println("Confirm SIM service actions");}
}
}



case 3->{System.out.println("Security settings");

String securitySetting = """
 
	1-> PIN code request
	2-> Call barring service
	3-> Fixed dialling
	4-> Closed user group
	5-> Phone security
	6-> Change access codes

""";

	System.out.println(securitySetting);
	int securitySettingSelection = scanner.nextInt();

	switch(securitySettingSelection){

case 1->{System.out.println(" PIN code request");}
case 2->{System.out.println("Call barring service");}
case 3->{System.out.println("Fixed dialling");}
case 4->{System.out.println(" Closed user group");}
case 5->{System.out.println("Phone security");}
case 6->{System.out.println("Change access codes");}

}


}
case 4->{System.out.println("Restore factory settings");}
}
}




case 7->{System.out.println("Call divert");}
case 8->{System.out.println("Games");}
case 9->{System.out.println("  Calculator");}
case 10->{System.out.println("Reminders");}


case 11->{System.out.println("Clock");
String clock = """
	1-> Alarm clock
	2-> Clock settings
	3-> Date settings
	4-> Stopwatch
	5-> Countdown timer
	6-> Auto update of date and time

""";

System.out.println(clock);

int clockSelection = scanner.nextInt();

switch(clockSelection ){

case 1->{System.out.println(" Alarm clock");}
case 2->{System.out.println("Clock settings");}
case 3->{System.out.println("Date settings");}
case 4->{System.out.println(" Stopwatch");}
case 5->{System.out.println("Countdown timer");}
case 6->{System.out.println("Auto update of date and time");}

}

}
case 12->{System.out.println(" Profiles");}
case 13->{System.out.println(" SIM services");}



}
}
}
