
import java.util.*;
public class Array {
	public static void main(String args[]) {
		Scanner sc=new Scanner(System.in);
		int size=sc.nextInt();
		int arr[]=new int[size];
		for(int i=0;i<size;i++) {
			arr[i]=sc.nextInt();
		}
		int rot=sc.nextInt();
		rot=rot%size;
		for(int j=1;j<=rot;j++) {
			int temp=arr[size-1];
			for(int i=size-1;i>0;i--) {
			arr[i]=arr[i-1];
			}
			arr[0]=temp;
	} 
		System.out.print("[");for(int i=0;i<size;i++) {
		System.out.print(arr[i]+" ");
		
}
	System.out.println("]");
}
}

