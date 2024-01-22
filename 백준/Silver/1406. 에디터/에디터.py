import sys
input = sys.stdin.readline;

stack1 = list(input().rstrip());
stack2 = [];

for i in range(int(input())):
  data = input().split();
  if data[0] == 'P' :
    stack1.append(data[1]);
  elif data[0] == 'L' :
    if len(stack1) > 0:
      stack2.append(stack1.pop());
  elif data[0] == 'D':
    if len(stack2) > 0:
      stack1.append(stack2.pop());
  elif data[0] == 'B':
    if len(stack1) > 0:
      stack1.pop();

stack1.extend(reversed(stack2));
print(''.join(stack1));
