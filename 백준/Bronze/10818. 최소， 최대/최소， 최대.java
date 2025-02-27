    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStreamReader;
    public class Main {
        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            int n = Integer.parseInt(br.readLine());
            String[] arr = br.readLine().split(" ");
            int min = 1000001;
            int max = -1000001;

            for (int i = 0; i < n; i++) {
                int num = Integer.parseInt(arr[i]);
                if (min > num) {
                    min = num;
                }
                if (max < num) {
                    max = num;
                }
            }
            System.out.println(min + " " + max);
        }
    }