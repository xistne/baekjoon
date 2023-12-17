a, b = map(int,input().split());
dayList = ['MON','TUE','WED','THU','FRI','SAT','SUN'];
days = [31,28,31,30,31,30,31,31,30,31,30,31];

day = 0;
for i in range(0,a-1) :
    day += days[i];

day += b-1;

print(dayList[day%7]);
