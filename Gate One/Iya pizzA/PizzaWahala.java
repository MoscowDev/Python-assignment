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

case "sapa"->{System.out.println("you Choose sapa size");
System.out.print("enter number of people:  ");
int people = input.nextInt();


System.out.print("enter number of boxes:  ");
int boxes = input.nextInt();

System.out.print("enter amount:  ");
int pricePerBox = input.nextInt();

pricePerBox = 2500;
int pricePerSlice = pricePerBox /4;

if(pizzaMenu=="sapa" && people == pricePerSlice ){


}

}




case "small money"->{System.out.print(" you Choose small money");

System.out.print("enter number of people:  ");
int people = input.nextInt();

System.out.print("enter number of boxes:  ");
int boxes = input.nextInt();

System.out.print("enter amount:  ");
int PricePerBox = input.nextInt();
PricePerBox = 2900;
int pricePerSlice = PricePerBox /6;

}
case " big boys"->{System.out.print(" you Choose sBig Boys");

System.out.print("enter number of people:  ");
int people = input.nextInt();

System.out.print("enter number of boxes:  ");
int boxes = input.nextInt();

System.out.print("enter amount:  ");
int PricePerBox = input.nextInt();

PricePerBox = 4000;
int PricePerSlice = PricePerBox /8;



}
case "odogwu"->{System.out.println(" you Choose sapa Odogwu");

System.out.print("enter number of people:  ");
int people = input.nextInt();

System.out.print("enter number of boxes:  ");
int boxes = input.nextInt();

System.out.print("enter amount:  ");
int PricePerBox = input.nextInt();

PricePerBox = 5200;
int PricePerSlice = PricePerBox /12;






}
	
}
}
}
