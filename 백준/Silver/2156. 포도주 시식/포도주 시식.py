import sys

n = int(sys.stdin.readline())

arr = [0,0,0]+[int(sys.stdin.readline().strip()) for i in range(n)]
dp = [0] * (n+3)

for i in range(3,n+3):
  dp[i] += (max(arr[i-1]+dp[i-3]+arr[i],dp[i-2]+arr[i],dp[i-1]))

print(max(dp))
