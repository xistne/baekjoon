n = int(input());
result = [];
for i in range(n):
    a, b = map(int,input().split());
    result.append(a+b);

for re in result:
    print(re);
