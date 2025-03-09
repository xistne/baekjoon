n = int(input())
arr = [0]+list(map(int,input().split()))
dp = arr[:]


for i in range(1,n+1):
    for j in range(1,i):
        dp[i] = max(dp[i],dp[j]+dp[i-j])
print(dp[n])