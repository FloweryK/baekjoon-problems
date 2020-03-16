import java.util.Scanner;

public class n10952 {
    public static void main(String[] ar){
        int a=-1, b=-1;
        Scanner sc = new Scanner(System.in);

        while (true) {
            a = sc.nextInt();
            b = sc.nextInt();
            if (a==0 && b==0){
                break;
            }
            System.out.println(a+b);
        }
    }
}
