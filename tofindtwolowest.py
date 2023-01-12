


from operator import itemgetter




students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

name = ['Harry','Berry','Tina','Akriti','Harsh']
score = [37.21,37.21,37.2,41,39]

res = []
res.append([name,score])
res1 = []
res1.append([[name[0],score[0]],[name[1],score[1]],[name[2],score[2]],[name[3],score[3]],[name[4],score[4]]])

print(res)
print(res[0][0])
print(res1)

score_ = []
score_.append(score)
print(score_)



b = sorted(set(score_[0]))
print(b)
b.remove(min(score_[0]))
print(b)

a = []
a.append(min(b))
print(a)

name_ = []

name_.append(res[0][0][0])
print(name_)

name_2 = []

name_2.append(res[0][1])
print(name_2)

for x in res:
    if x[0][1] == a:
        name_.append(res[0])
name_.sort()

print(name_)

"""
lst4 = []
for x in lst3:
    if x != re2:
        lst4.append(x)
print(lst4)
"""

"""
lst = [["a","b","c"], [1,2,3], ["x","y","z"]]
lst2 = []
lst2.append([x[0] for x in lst])
print lst2[0]
"""


#final code

if __name__ == '__main__':
    score_= []
    res =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        res.append([name,score])
        score_.append(score)
    b=sorted(set(score_))
    b.remove(min(score_))
    a=min(b)
    # print(a)
    # print(res)
    name_=[]
    for x in res:
        if x[1]== a:
            name_.append(x[0])
    name_.sort()
    c = set(name_)
    for x in c:
        print(x)

#final code 2

n=int(input())
ls=[]   #List to store names and scores
scoreset=[]     #List to store scores
for i in range(n):
    a=[]
    name = input()
    score = float(input())
    a.append(name)
    a.append(score)
    ls.append(a)    #Appending names and scores to list
    scoreset.append(score)  #Appending scores to 2nd list
#Sorting the list
scoreset=sorted(scoreset)
min1=min(scoreset)  #minimum 1 of scores
while (scoreset.count(min1)>0): #Loop to remove all occurences of minimum from list
    for i in scoreset:
        if (i==min1):
            scoreset.remove(i)
min2=min(scoreset)    #second minimum 
namels=[]
for i in range (len(ls)):
    if (ls[i][1]==min2):
        namels.append(ls[i][0]) #Appending names to a different list which have score=minimum
#Sorting names list
namels=sorted(namels)
for i in namels:
    print(i)