import sys
n = int(input())
arr = []
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        arr.append(command[1])
    elif command[0] == 'pop':
        print(arr.pop() if len(arr) != 0 else -1)
    elif command[0] == 'size':
        print(len(arr))
    elif command[0] == 'empty':
        print(1 if len(arr) == 0 else 0)
    elif command[0] == 'top':
        print(arr[-1] if len(arr) != 0 else -1)

