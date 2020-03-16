import java.util.Scanner;

public class n10871 {
    public static void main(String[] ar){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        String text = "";

        for (int i=0; i<n; i++){
            int value = sc.nextInt();

            if (value < x){
                text += String.format("%d ", value);
            }
        }
        System.out.println(text);
    }
}
