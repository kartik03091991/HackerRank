# Enter your code here. Read input from STDIN. Print output to STDOUT

E = int(input())
lstE = []

lstE.append(list(map(int,input().split())))
#print(lstE)


F = int(input())
lstF = []


lstF.append(list(map(int,input().split())))

#print(lstF)

setE = set(lstE[0])
setF = set(lstF[0])
print(len(setE.difference(setF)))