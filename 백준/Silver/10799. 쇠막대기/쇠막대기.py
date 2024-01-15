data = list(input());
result = 0;
arr = [];

for i in range(len(data)):
  if data[i] == '(':
    arr.append(data[i]);
  else:
    if data[i-1] == '(':
      arr.pop();
      result += len(arr);
    else:
      arr.pop();
      result += 1;

print(result);