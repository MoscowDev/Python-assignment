import java.util.Scanner;

public class SumOfEvenNumbers{
	public static void main(String[] args){
	Scanner input = new Scanner(System.in);

int[] scores = new int[10];

int sumOfEven = 0;
for(int count = 1 ; count < 10; count ++){
System.out.print("Enter an integer: ");
int number = input.nextInt();
if(number % 2 == 0){
sumOfEven+= number;

}
}

System.out.println("The Sum is: " + sumOfEven );
}
}