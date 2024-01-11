n = int(input());
for i in range(n):
  data = list(input());
  arr = [];
  for i in range(len(data)):
    if data[i] == '(':
      arr.append(data[i]);
    else:
      if len(arr) == 0:
        print('NO');
        break;
      else : 
        arr.pop();
    if i == len(data)-1:
      if len(arr) == 0 :
        print('YES');
      else :
        print('NO');