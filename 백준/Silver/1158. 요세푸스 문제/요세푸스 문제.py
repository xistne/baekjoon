from collections import deque
n, k = map(int,input().split());
result = [];
arr = deque();
for i in range(1,n+1):
  arr.append(i);

while arr:
  for i in range(k-1):
    arr.append(arr.popleft());
  result.append(arr.popleft());
  
print(str(result).replace('[','<').replace(']','>'));
