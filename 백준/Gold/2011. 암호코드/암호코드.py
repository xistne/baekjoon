arr = [0]+list(map(int,input()))
n = len(arr)
dp = [0] * (n)
dp[0] = dp[1] = 1
if arr[1] == 0 :
    print(0)
    exit(0)

for i in range(2, n):
    if arr[i] > 0 :
        dp[i] = dp[i-1]
    
    if 10 <= arr[i] + arr[i-1]*10 < 27 :
        dp[i] += dp[i-2]

print(dp[n-1]%1000000)