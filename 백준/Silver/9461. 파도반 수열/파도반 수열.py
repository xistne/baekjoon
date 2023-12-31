t = int(input());
for i in range(t):
  n = int(input());
  dp = [0] * 100;
  dp[0] = 1;
  dp[1] = 1;
  dp[2] = 1;
  for i in range(3,n):
    dp[i] = dp[i-2] + dp[i-3];
  print(dp[n-1]);
  