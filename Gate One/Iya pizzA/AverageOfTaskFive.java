import java.util.Scanner;

public class AverageOfTaskFive{
	public static void main(String[] args){
	Scanner input = new Scanner(System.in);

int[] scores = new int[10];

int averageSum = 0;
int average = 0;
int sumOfEven = 0;
for(int count = 1 ; count <= 10; count ++){
System.out.print("Enter an integer: ");
int number = input.nextInt();
if(number % 2 == 0){
sumOfEven+= number;
averageSum+=1;
average =  sumOfEven/averageSum;
}
}

System.out.println("The Average of Task five is: " + average );
}
}