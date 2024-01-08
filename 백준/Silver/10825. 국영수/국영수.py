n = int(input());
data = [];
for i in range(n):
  name, a, b, c = input().split();
  data.append([ a, b, c, name]);

data.sort(key = lambda x: (-int(x[0]), int(x[1]), -int(x[2]), x[3]));

for i in range(n):
  print(data[i][3]);