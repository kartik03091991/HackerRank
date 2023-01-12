import numpy

t = list(map(int,input().split()))
#print(t)

N = t[0]
M = t[1]
P = t[2]

lstN = []
for x in range(0,N):
    lstN.append(list(map(int,input().split())))
    
#print(lstN)

lstM = []
for x in range(0,M):
    lstM.append(list(map(int,input().split())))
    
#print(lstM)

array1 = numpy.array(lstN)
#print(array1)

array2 = numpy.array(lstM)
#print(array2)

print(numpy.concatenate((array1, array2), axis = 0)) 

