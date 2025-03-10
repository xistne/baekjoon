import sys
input = sys.stdin.readline
n = int(input())

arr = [tuple(map(int,input().split())) for i in range(n)]

arr.sort()

for i in arr:
    print(i[0], i[1])