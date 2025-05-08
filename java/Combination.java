
import java.util.*;
public class Combination {
	public static int combination(int n,int r) {
		if(n==r||r==0) {
			return 1;
		}
		else {
			return combination(n-1,r-1)+combination(n-1,r);
		}
	}
	public static void main (String args[]) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int r=sc.nextInt();
		int comb=combination(n,r);
		System.out.println(comb);
	}
}

