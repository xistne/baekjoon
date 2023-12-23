n = int(input());
dp = [[0 for j in range(12)] for i in range(n+1)];
result = 0;
for i in range(2,11) : 
    dp[1][i] = 1;
for i in range(2,n+1):
    for j in range(1,11):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1];

for i in range(11) : 
  result += dp[n][i];

print(result%1000000000);