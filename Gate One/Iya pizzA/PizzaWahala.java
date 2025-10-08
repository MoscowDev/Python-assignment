import java.util.Scanner;

public class PizzaWahala{
public static void main(String [] args){
Scanner input = new Scanner(System.in);
String prompt = """

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



""";

System.out.print(prompt);
System.out.println("Enter your pizza choice");
String pizzaMenu = input.nextLine().toLowerCase();


switch(pizzaMenu){

case "sapa"->{System.out.println("Wow! You Choose sapa size");
System.out.print("enter number of Guest:  ");
int people = input.nextInt();

int box = people /4;
int totalSlice = 4 * box;
int remainder = 0;
int Amount = box * 2500;
System.out.println("total amount is:" + Amount);
if(people % 4 != 0){
	box = box + 1;
	}
remainder = totalSlice - people;

System.out.print("Number of boxes to buy " + box + " The total number of guest " + people + " total amount is " + Amount + " Number of leftover slice " + remainder);


}


case "small money"->{System.out.print(" Wow! you Choose small money");

System.out.print("enter number of people:  ");
int people = input.nextInt();

int box = people /6;
int totalSlice = 6 * box;
int remainder = 0;
int Amount = box * 2900;
System.out.println("total amount is:" + Amount);
if(people % 6 != 0){
	box = box + 1;
	}
remainder = totalSlice - people;

System.out.print("Number of boxes to buy " + box + " The total number of guest " + people + " total amount is " + Amount + " Number of leftover slice " + remainder);

}


case " big boys"->{System.out.print(" Wow! You Choose Big Boys");

System.out.print("enter number of people:  ");
int people = input.nextInt();

int box = people /8;
int totalSlice = 8 * box;
int remainder = 0;
int Amount = box * 4000;
System.out.println("total amount is:" + Amount);
if(people % 8 != 0){
	box = box + 1;
	}
remainder = totalSlice - people;

System.out.print("Number of boxes to buy " + box + " The total number of guest " + people + " total amount is " + Amount + " Number of leftover slice " + remainder);



}
case "odogwu"->{System.out.println(" Wow! Choose Odogwu");

System.out.print("enter number of people:  ");

int people = input.nextInt();
int box = people /12;
int totalSlice = 12 * box;
int remainder = 0;
int Amount = box * 5200;
System.out.println("total amount is:" + Amount);
if(people % 12 != 0){
	box = box + 1;
	}
remainder = totalSlice - people;

System.out.print("Number of boxes to buy " + box + " The total number of guest " + people + " total amount is " + Amount + " Number of leftover slice " + remainder);






}
	
}
}
}

