data = input();
upper = [chr(i) for i in range(ord('A'), ord('Z')+1)];
lower = [chr(i) for i in range(ord('a'),ord('z')+1)];
for i in data:
    if i.isupper():
        print(upper[(ord(i)+13-65)%26],end='');
    elif i.islower():
        print(lower[(ord(i)+13-97)%26],end='');
    else:
        print(i,end='');