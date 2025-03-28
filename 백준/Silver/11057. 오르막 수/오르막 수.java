    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStreamReader;
    import java.util.Arrays;

    public class Main {
        static int mod = 10007;
        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int n = Integer.parseInt(br.readLine());

            int [][] dp = new int[n][10];

            for (int i = 0; i < 10; i++) {
                dp[0][i] = 1;
            }
            for (int i = 1; i < n; i++) {
                dp[i][0]=1;
                for (int j = 1; j < 10; j++) {
                    dp[i][j] = (dp[i][j - 1] + dp[i - 1][j])%mod;
                }
            }
            int answer = 0;
            for (int j = 0; j < 10; j++) {
                answer += dp[n-1][j];
            }
            System.out.println(answer%mod);
        }
    }