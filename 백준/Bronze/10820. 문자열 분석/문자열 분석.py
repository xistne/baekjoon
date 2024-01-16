while True :
  try :
    arr = [0] * 4;
    for i in input():
      if i == ' ':
        arr[3] += 1;
      elif i.isdigit():
        arr[2] += 1;
      elif i.isupper() :
        arr[1] += 1;
      elif i.islower() :
        arr[0] += 1;
    for i in arr:
      print(i, end=' ');
  except EOFError :
    break
  