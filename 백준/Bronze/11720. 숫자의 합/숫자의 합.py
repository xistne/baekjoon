import sys
n = int(sys.stdin.readline());

numString = sys.stdin.readline();
result = 0;
for i in range(n):
    result += int(numString[i]);
    
print(result);