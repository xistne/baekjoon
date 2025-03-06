    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStreamReader;
    import java.util.Arrays;
    import java.util.StringTokenizer;

    public class Main {

        static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        static int[][] dp;
        static StringTokenizer st;
        static int n;
        public static void main(String[] args) throws IOException {
            int t = Integer.parseInt(br.readLine());

            for (int i = 0; i < t; i++) {
                n = Integer.parseInt(br.readLine().trim());
                setDP();
                if (n == 1) {
                    System.out.println(Math.max(dp[0][0],dp[1][0]));
                    continue;
                }
                dp[0][1] += dp[1][0];
                dp[1][1] += dp[0][0];
                for (int j = 2; j < n; j++) {
                    dp[0][j] += Math.max(dp[1][j-1],dp[1][j-2]);
                    dp[1][j] += Math.max(dp[0][j-1],dp[0][j-2]);
                }
                System.out.println(Math.max(dp[0][n-1],dp[1][n-1]));
            }

        }
        static void setDP() throws IOException {
            dp = new int[2][n];
            for (int i = 0; i < 2; i++) {
                st = new StringTokenizer(br.readLine().trim());
                for (int j = 0; j < n; j++) {
                    dp[i][j] = Integer.parseInt(st.nextToken());
                }
            }
        }
    }