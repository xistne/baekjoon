import sys
input = sys.stdin.readline

n = int(input());
arr = [];
for i in range(n):
  k = input().split();
  if k[0] == 'push':
    arr.append(k[1]);
  elif k[0] == 'pop':
    print( -1 if len(arr) == 0 else arr.pop(0));
  elif k[0] == 'size':
    print(len(arr));
  elif k[0] == 'empty':
    print( 1 if len(arr) == 0 else 0);
  elif k[0] == 'front':
    print( arr[0] if len(arr) != 0 else -1);
  elif k[0] == 'back':
    print( arr[-1] if len(arr) != 0 else -1);