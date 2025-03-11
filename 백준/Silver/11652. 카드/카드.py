import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for i in range(n)]

arr.sort()

max_num = arr[0]
max_count = 0
current_count = 0
for i in range(n):
    if arr[i] != arr[i-1]:
        current_count = 1
    else :
        current_count +=1
    
    if max_count < current_count:
        max_count = current_count
        max_num = arr[i]

print(max_num)