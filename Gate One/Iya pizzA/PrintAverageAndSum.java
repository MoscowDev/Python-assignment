import java.util.Scanner;

public class PrintAverageAndSum{
	public static void main(String[] args){
	Scanner input = new Scanner(System.in);

int[] scores = new int[10];
int average = 0;
int sum = 0;
for(int count = 0 ; count < 10; count ++){
System.out.print("Enter an integer: ");
int number = input.nextInt();
sum += number;
scores[count] =+ number;
average = sum/10;
}
System.out.println("The average is: " + average );

System.out.println("The Sum is: " + sum );
}
}