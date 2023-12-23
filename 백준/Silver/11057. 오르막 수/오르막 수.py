n = int(input());
dp = [[0 for i in range(10)] for i in range(1001)];

for i in range(10):
    dp[0][i] = 1;

for i in range(n):
    dp[i+1][0] = 1;
    for j in range(1,10):
        dp[i+1][j] = dp[i+1][j-1] + dp[i][j];

print(sum(dp[n-1])%10007);
