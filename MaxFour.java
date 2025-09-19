public class MaxFour {
    public static void main(String[] args) {
        /*int a = 10, b = 14, c = 9, d = 2;*/
        /*int max=a;
        if(b>max){
            max=b;
        }if(c>max){
            max=c;
        }
        if(d>max){
            max=d;
        }
        System.out.println("max is " + max);
    }*/

               /* int max = Math.max(Math.max(a, b), Math.max(c, d));*/
        /*int max = (a > b ? (a > c ? (a > d ? a : d) : (c > d ? c : d))
                : (b > c ? (b > d ? b : d) : (c > d ? c : d)));*/
        int[] arr={10,45,1,78};
        int max = arr[0];
        int min=arr[0];

        for(int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
            if (arr[i] < min) {
                min = arr[i];
            }
        }
                System.out.println("Maximum is: " + max);
        System.out.println("Minimum is: " + min);
    }
}
