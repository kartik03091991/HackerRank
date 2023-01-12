# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

inp1 = list(map(int,input().split()))
#print(inp1)

for x in range(1,2):
    month1 = inp1[x-1]
    day1 = inp1[x]
    year1 = inp1[x+1]
    
#print(month1)
#print(day1)
#print(year1)

fin = calendar.weekday(year1,month1,day1)
#print(fin)

#print(type(fin))

if fin == 0:
    print("MONDAY")
elif fin == 1:
    print("TUESDAY")
elif fin == 2:
    print("WEDNESDAY")
elif fin == 3:
    print("THURSDAY")
elif fin == 4:
    print("FRIDAY")
elif fin == 5:
    print("SATURDAY")
else:
    print("SUNDAY")