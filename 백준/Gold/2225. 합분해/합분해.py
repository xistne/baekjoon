n, k = map(int,input().split())
dp = [[0]*201 for _ in range(201)]

for i in range(1,201):
    dp[1][i] = 1
    dp[i][0] = 1

for i in range(2,k+1):
    for j in range(1,n+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000000

print(dp[k][n])