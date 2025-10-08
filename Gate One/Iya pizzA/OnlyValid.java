import java.util.Scanner;

public class OnlyValid{
	public static void main(String[] args){
	Scanner input = new Scanner(System.in);

int[] scores = new int[10];

int sum = 0;
for(int count = 0 ; count < 10; count ++){
System.out.print("Enter an integer: ");
int number = input.nextInt();
if(number < 0 || number > 100){
continue;
}
sum += number;
scores[count] =+ number;

}
System.out.print("The sum of only valid is: " + sum);

}
}