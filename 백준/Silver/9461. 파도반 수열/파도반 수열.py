t = int(input())
dp = [0,1,1,1,2,2] +[0]*100

for i in range(6,101):
    dp[i] = dp[i-1] + dp[i-5]

for i in range(t):
    n = int(input())
    print(dp[n])