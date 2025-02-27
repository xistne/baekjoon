    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStreamReader;
    public class Main {
        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            int n = Integer.parseInt(br.readLine());

            for (int i = 1; i < n + 1; i++) {
                System.out.print("*".repeat(i));
                System.out.print(" ".repeat(2*(n-i)));
                System.out.println("*".repeat(i));
            }
            for (int i = n - 1; i > 0; i--) {
                System.out.print("*".repeat(i));
                System.out.print(" ".repeat(2*(n-i)));
                System.out.println("*".repeat(i));
            }
        }
    }