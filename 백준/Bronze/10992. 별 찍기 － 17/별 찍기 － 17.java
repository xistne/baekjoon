    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStreamReader;
    public class Main {
        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            int n = Integer.parseInt(br.readLine());
            System.out.println(" ".repeat(n-1) + "*");
            for (int i = 1; i < n-1; i++) {
                System.out.print(" ".repeat(n-i-1));
                System.out.print("*");
                System.out.print(" ".repeat(2*i-1));
                System.out.println("*");
            }
            if(n!=1){
                System.out.println("*".repeat(2*n-1));
            }
        }
    }