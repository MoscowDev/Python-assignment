public class Cakes{
	public static int findSmallest(int array[]){
	
	

int smallest = array[0];

for(int count = 0; count <= (array.length - 1); count++){
	
	if (array[count] < smallest){
	smallest = array[count];
	}
}

return smallest;


} 

public static int average(int array[]){
	

int average = 0;
int sum = 0;
for(int count = 0; count < array.length ; count++){

	sum += array[count];
	average = sum / array.length;
	
}

return average;

}


public static int occurence(int array[], int number){
 
int occurence = 0;	
for(int count = 0; count < array.length ; count++){
	if(number == array[count])
	 occurence += 1;
	 
	
}

return occurence;


}

public static boolean containsElement(int array[], int number){


for(int count = 0; count < array.length; count++){
	
	if (array[count] == number){
	
	return true;
	}
	}

	return false;
}

public static int firstElement(int array[]){
	

for(int count = 0; count <= (array.length); count++){
	
	return array[0];
	
}

return 0;
}

public static int lastElement(int array[]){
	

for(int count = 0; count <= (array.length); count++){

	 return array[8];
		
}

 return 0;
}



public static int arrayLength(int array[]){
	

for(int count = 0; count <= (array.length); count++){

		
}
	 return array[4];	
}
}