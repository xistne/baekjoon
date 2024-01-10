import sys
input = sys.stdin.readline

n = int(input());
arr = [];
for i in range(n):
  data = input().replace("\n","");
  dataList = data.split(' ');
  if dataList[0] == "push":
    arr.append(dataList[1]);
  elif dataList[0] == "pop":
    if(len(arr) ==0):
      print(-1);
      continue;
    popped = arr.pop();
    print(popped);
  elif dataList[0] == "size":
    print(len(arr));
  elif dataList[0] == "empty":
    if len(arr) == 0:
      print(1);
      continue;
    print(0);
  elif dataList[0] == "top":
    if len(arr) == 0:
      print(-1);
      continue;
    print(arr[-1]);
