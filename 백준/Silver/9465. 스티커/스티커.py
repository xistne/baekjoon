n = int(input());

for i in range(n):
  m = int(input());
  dp = [list(map(int,input().split())) for _ in range(2)];
  
  if m > 1 :
    dp[0][1] += dp[1][0];
    dp[1][1] += dp[0][0];

  for j in range(2,m):
    dp[0][j] += max(dp[1][j-1],dp[1][j-2]);
    dp[1][j] += max(dp[0][j-1],dp[0][j-2]);

  print(max(dp[0][m-1],dp[1][m-1]));