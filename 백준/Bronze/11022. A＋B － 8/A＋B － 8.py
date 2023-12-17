import sys

n = int(sys.stdin.readline());

for i in range(n):
    a,b = map(int, sys.stdin.readline().split());
    sum = a+b;
    print(f'Case #{i+1}: {a} + {b} = {sum}');