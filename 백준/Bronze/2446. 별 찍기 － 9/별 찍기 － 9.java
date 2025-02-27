    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStreamReader;
    public class Main {
        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            int n = Integer.parseInt(br.readLine());

            for (int i = 0; i < n; i++) {
                System.out.print(" ".repeat(i));
                System.out.println("*".repeat(2*(n-i)-1));
            }
            for (int i = 2; i < n+1; i++) {
                System.out.print(" ".repeat(n-i));
                System.out.println("*".repeat(2*i-1));
            }
        }
    }