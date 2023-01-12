thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

x = thisdict["model"]
print(x)


x = thisdict.get("model")
print(x)



if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    


#print(input().split())
#print (student_marks)
#print(n)
#print(name, *line)
#print(scores)
#print(query_name)

y = student_marks.keys()
#print(y)
v = student_marks.values()
#print(v)
c = []

if query_name in y:
  #print(query_name)
  r = student_marks.get(query_name)
#print(r)
#for query_name in y:

  
for item in r:
      c.append(format(float(item),".2f"))
#print(c)
scores2 = list(map(float, c))
#print(scores2)
d = sum(scores2)/len(scores2)
#print(d)
e = format(float(d),".2f")
print(e)
#print(d)
    #print(format(c," .2f"))
    
#a = sum(float(scores))
#b = len(float(scores))
#c = (format(a," .2f")/format(b, " .2f"))

#format(c,".2f")
#print(c)


""" 
for item in scores:
      c.append(format(float(item),".2f"))
print(c)
scores2 = list(map(float, c))
print(scores2)
d = sum(scores2)/len(scores2)
print(d)
e = format(float(d),".2f")
print(e)
#print(d)
    #print(format(c," .2f"))
    
#a = sum(float(scores))
#b = len(float(scores))
#c = (format(a," .2f")/format(b, " .2f"))

#format(c,".2f")
#print(c)

"""