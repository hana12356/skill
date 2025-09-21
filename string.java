public class string {
    public static void main(String args[]){
        String s= "welcome";
        String s2="Welcome";
        String s1="javaprgm";
        {
            System.out.println(s);
            System.out.println(s1.length());
            System.out.println(s1.trim());
            System.out.println(s.concat(s1));
            System.out.println(s.charAt(2));
            System.out.println(s.contains("wel"));
            System.out.println(s.equals(s1));
            System.out.println(s.equals(s2));
            System.out.println(s.equalsIgnoreCase(s2));
            System.out.println(s1.replace('a','b'));
            System.out.println(s.substring(0,3));
            System.out.println(s2.toLowerCase());
            System.out.println(s1.toUpperCase());
        }
    }
}
