import java.util.*;
public class Evensum {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        int i=0;
        for(i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        int sum=0;
        for(i=0;i<n;i++){
            if(arr[i]%2==0){
                sum+=arr[i];
            }
        }
        System.out.println(sum);
        sc.close();
    }
}
