

public class KKata{


	public static int factorOf(int number){
	
	int factorCount = 0;
	for(int counter = 1; counter <= number; counter++){
		if(number % counter == 0)
		factorCount = factorCount + 1;
	}



	return factorCount;
	
	}

	public static boolean isOdd(int number){
	
	 if(number % 2 == 0){
		return false;
		
	}
	else{
	return true;
	}

	}
	public static boolean isLeapYear(int year){
        
	if(year % 4 == 0 && year % 100 != 0){
	return true;

	}

	 else if(year % 4 == 0 && year % 100 == 0 && year % 400 == 0){

	return true;
	}
	else{
	return false;


	}
        }
	
	public static double isFahrenheit( double number){

	double celcius = 5*(number - 32)/9;
	return celcius;
	}
	
	public static boolean isEven(int number){
	
		
		if(number % 2 == 0){
		return true;
	}
	else{
		return false;
	}
	}


	public static boolean isPrimeNumber(int number){
	
	 if (number <= 1) return false;
   	 for (int i = 2; i <= number / 2; i++) {
        if (number % i == 0)
            return false;
   	 }
    	return true;
	}
	public static int subtract(int num, int num2){
        int add = num + num2;
	if(num + num2 == add || num2 + num == add){
	return add;
	}

	return 0;
	}
        
	
	public static float divide( float number, float number2){
	
	
	
	if(number2 == 0){
	return 0;
	
	}else{

	float div = number/number2;
	return div;

	}
	}

	public static boolean isSquare(int number){
	

	int square = number * number;

	if(number == square){

	return true;
	} else{
	return false;
	}
	}

	public static boolean isPalindrome(int number){
	
	int number2 = number;
	int pal = 0;

	while(number != 0){

	int last = number % 10;
	pal = pal * 10 + last;
	number = number/10;
	}

	if(number2 == pal){
	return true;
  	}else{
   	return false;
	}
	
	}


      public static long factorialOf(int number){

      long factorial = 1;

	for(int counter = number; counter >= 1; counter--){
	factorial = factorial * counter;
	}
	return factorial;

	}
	
 	 public static long squareOf(int number){

	int square = number * number;

	if(number == square){

	return square;
	}
	
	return square;
	}
}
	
	//public static void printStars(int numberOfRows){
	
	
//}


//public static boolean factorOf(int number){


	//for(int count = 0; count <= number; count ++)
	//	if(number % count == 0)
           
	//}