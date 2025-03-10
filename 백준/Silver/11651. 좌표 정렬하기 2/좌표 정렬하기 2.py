import sys
input = sys.stdin.readline
n = int(input())

arr = [tuple(map(int,input().split())) for i in range(n)]

arr.sort(key = lambda x: (x[1],x[0]))

for i in arr:
    print(i[0], i[1])