n = int(input());
print(' '*(n-1)+'*');
for i in range(2,n+1):
    if(i == n) :
        print('*'*(2*n-1));
        break;
    print(' '*(n-i)+'*'+' '*(2*(i-1)-1)+'*');
