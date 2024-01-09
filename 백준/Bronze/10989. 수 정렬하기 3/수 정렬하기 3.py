import sys
input = sys.stdin.readline
array=[0]*10001
for i in range(int(input())):
  array[int(input())] +=1

for i in range(1,len(array)):
  if array[i] != 0:
    for j in range(array[i]):
      print(i)
