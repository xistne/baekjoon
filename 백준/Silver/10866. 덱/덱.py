import sys
input = sys.stdin.readline;

n = int(input());
arr = [];
for i in range(n):
  data = input().split();
  if data[0] == "push_front":
    arr.insert(0,data[1]);
  elif data[0] == "push_back":
    arr.append(data[1]);
  elif data[0] == "pop_front":
    print(-1 if len(arr) == 0 else arr.pop(0));
  elif data[0] == "pop_back":
    print(-1 if len(arr) == 0 else arr.pop());
  elif data[0] == "size":
    print(len(arr));
  elif data[0] == "empty":
    print(1 if len(arr) == 0 else 0);
  elif data[0] == "front":
    print(-1 if len(arr) == 0 else arr[0]);
  elif data[0] == "back":
    print(-1 if len(arr) == 0 else arr[-1]);