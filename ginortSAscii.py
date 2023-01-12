# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
Sample Input

Sorting1234
Sample Output

ginortS1324
"""

inputlst = list(map(str,input()))
#print(inputlst)
#print(inputlst[0])
#print(ord(inputlst[0]))
#print(type(ord(inputlst[0])))
# ascii value for the lowercase alphabet ---> 97 - 122
# ascii value for the UPPERCASE alphabet ---> 65 - 90
# ascii value for the 0-9 numbers ---> 48 - 57

lst1 = []
lst2 = []
lst3 = []
lst4 = []
for x in range(0,len(inputlst)):
    if 97 <= ord(inputlst[x]) <= 122:
        lst1.append(inputlst[x])
    lst1.sort()
    if 65 <= ord(inputlst[x]) <= 90:
        lst2.append(inputlst[x])
    lst2.sort()
    if 48 <= ord(inputlst[x]) <= 57:
        if int(inputlst[x]) % 2 != 0:
           lst3.append(inputlst[x])
           lst3.sort()
        else:
           lst4.append(inputlst[x])
           lst4.sort()

#print(lst1)
#print(lst2)
#print(lst3)
#print(lst4)
lst5 = []
#print(lst1+lst2+lst3+lst4)
lst5 = lst1+lst2+lst3+lst4
print("".join(lst5))
