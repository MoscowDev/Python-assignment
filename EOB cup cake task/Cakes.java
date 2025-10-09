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
	

int average = array[0];
int sum =array[0];
for(int count = 0; count < array.length-1 ; count++){

	sum =+ array[count];
	average = sum / array.length;
	
}

return average;



/*
public static int target(int array[]){
	
for(int count = 0; count < array.length-1 ; count++){

	sum =+ array[count];
	average = sum / array.length;
	
}

return average;
*/
}
}