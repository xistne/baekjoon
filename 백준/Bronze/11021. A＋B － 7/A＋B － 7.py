import sys

n = int(sys.stdin.readline());

for i in range(n):
    print('Case #' + str(i+1) + ': '+str(sum(map(int,sys.stdin.readline().split()))));
