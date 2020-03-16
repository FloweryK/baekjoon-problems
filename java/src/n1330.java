import java.util.Scanner;

public class n1330 {
    public static void main(String[] ar){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        if (a>b){
            System.out.println(">");
        }
        else if (a<b){
            System.out.println("<");
        }
        else{
            System.out.println("==");
        }
    }
}
