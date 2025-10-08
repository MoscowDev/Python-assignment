import java.util.Scanner;

public class ValidScoresSum{
	public static void main(String[] args){
	Scanner input = new Scanner(System.in);

int[] scores = new int[10];

int sum = 0;
for(int count = 0 ; count < 10; count ++){
System.out.print("Enter an integer between 0 and 100: ");
int number = input.nextInt();
if(number < 0 || number > 100){
break;
}
sum += number;
scores[count] =+ number;

}
System.out.print("The sum is: " + sum);

}
}