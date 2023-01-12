# Enter your code here. Read input from STDIN. Print output to STDOUT


master_set = input()
num_of_ele_MS = list(map(int,input().split()))
N = int(input())

#print(master_set)
#print(num_of_ele_MS)
#print(N)


set_num_of_ele_MS = set(num_of_ele_MS)

lst1 = []
"""
in1 = list(map(str,input().split()))
print(in1)
in2 = list(map(str,input().split()))
print(in2)
"""

 
for x in range(0,2*N):
    lst1.append(list(map(str,input().split())))
    #if lst1[x] == "intersection_update":
     #   set_num_of_ele_MS.intersection_update(set(lst1[x+1]))
    
#print(lst1)

p = len(lst1)
#print(p)
#print(lst1[0][0])
#print(set(int(y) for y in lst1[1]))


#int(x) for x in strings
lst2_commands = []

for x in range(0,len(lst1),2):
    lst2_commands.append(lst1[x])

#print(lst2_commands)

lst3_set = []

for x in range(1,len(lst1),2):
    lst3_set.append(lst1[x])

#print(lst3_set)

for x in range(0,len(lst2_commands)):
    if lst2_commands[x][0] == "intersection_update":
        set_num_of_ele_MS.intersection_update(set(int(y) for y in lst3_set[x]))
        #print(set_num_of_ele_MS)
    if lst2_commands[x][0] == "update":
        set_num_of_ele_MS.update(set(int(y) for y in lst3_set[x]))
        #print(set_num_of_ele_MS)   
    if lst2_commands[x][0] == "symmetric_difference_update":
        set_num_of_ele_MS.symmetric_difference_update(set(int(y) for y in lst3_set[x]))  
        #print(set_num_of_ele_MS)       
    if lst2_commands[x][0] == "difference_update":
        set_num_of_ele_MS.difference_update(set(int(y) for y in lst3_set[x])) 
        #print(set_num_of_ele_MS)


"""
for x in range(0,len(lst1),2):
    if lst1[x][0] == "intersection_update":
        set_num_of_ele_MS.intersection_update(set(int(y) for y in lst1[x+1]))
    if lst1[x][0] == "update":
        set_num_of_ele_MS.intersection_update(set(int(y) for y in lst1[x+1]))   
    if lst1[x][0] == "symmetric_difference_update":
        set_num_of_ele_MS.intersection_update(set(int(y) for y in lst1[x+1]))         
    if lst1[x][0] == "difference_update":
        set_num_of_ele_MS.intersection_update(set(int(y) for y in lst1[x+1]))     
"""   
#print(set_num_of_ele_MS)        

list_set_num_of_ele_MS = list(set_num_of_ele_MS)

total = 0

for x in range(0,len(list_set_num_of_ele_MS)):
    total += list_set_num_of_ele_MS[x]

print(total)
 