public class CupCakeTest{

	public static void main(String[] args){
		int [] array = {20,5,6,6,7,8,6,1,16};

		System.out.println(Cakes.findSmallest(array));
		System.out.println(Cakes.average(array));
		System.out.println(Cakes.occurence(array, 6));
		System.out.println(Cakes.containsElement(array, 6));
		System.out.println(Cakes.firstElement(array));
		System.out.println(Cakes.lastElement(array));
		System.out.println(Cakes.arrayLength(array));
}
}

