import java.util.Scanner;

public class PrintSumOfIndexes{
	public static void main(String[] args){
	Scanner input = new Scanner(System.in);

int[] scores = new int[10];

int sumOfCount = 0;
for(int count = 0 ; count < 10; count ++){
System.out.print("Enter an integer: ");
int number = input.nextInt();
if(count % 2 == 0){
sumOfCount+= number;
}

}

System.out.println("The Sum of Even is: " + sumOfCount);
}
}