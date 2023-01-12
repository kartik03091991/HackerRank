# Enter your code here. Read input from STDIN. Print output to STDOUT
# 48 -57

N = int(input())
#print(N)
lst1 = []


for x in range(0,N):
    lst1.append(input())


#lst1 = ['+9-2','2.2','8-10','-6.1','-7*8','+1.3','+4*5','10.6','2*4']    
#lst1 = ['1.414','+.5486468','0.5.0','1+1.0','0']
#print(lst1)
lst2 = []

count1 = 0
count2 = 0
for x in range(0,len(lst1)):
    for y in range(0,len(lst1[x])):
      if 48 <= ord(str(lst1[x][y])) <= 57 and len(lst1[x]) != 1:
          lst2.append(True)
      elif (lst1[x][0] == "-" or lst1[x][0] == "+") and count1 == 0:
          lst2.append(True)
          count1 += 1
      elif (lst1[x][y] == ".") and count2 == 0:
          lst2.append(True)
          count2 += 1
      else:
          lst2.append(False)
    #print(lst2)
    print(all(lst2))
    lst2.clear()
    count1 = 0
    count2 = 0

"""
Input (stdin)

Download
4
4.0O0
-1.00
+4.54
SomeRandomStuff
Expected Output

Download
False
True
True
False
"""