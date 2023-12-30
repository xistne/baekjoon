n = int(input());
arr = [ int(input()) for _ in range(n)];
arr.insert(0,0);
dp = arr[:];
if n > 1:
  dp[2] += dp[1];
for i in range(3,n+1):
  dp[i] += max(dp[i-3] + arr[i-1], dp[i-2]);

print(dp[n]);