def iFunction(i,n):
  print('*'*i,end='');
  print(' '*(n-i),end='');
  print(' '*(n-i),end='');
  print('*'*(i));


n = int(input());

for i in range(1,n+1):
    iFunction(i,n);

for i in range(n-1,0,-1):
    iFunction(i,n);

