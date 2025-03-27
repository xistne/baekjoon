import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = []
result = 0
for i in range(n):
    arr.append(int(input()))

for i in range(n-1,-1,-1):
    if (k // arr[i]) != 0 :
        result += k//arr[i]
        k -= (k // arr[i] * arr[i])
    if k == 0:
        break

print(result)