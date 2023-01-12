def swap_case(s):
    lst = []
    for x in range(0,len(s)):
       if s[x].isupper():
           lst.append(s[x].casefold())
       else:
           lst.append(s[x].upper())
    m = "".join(lst)
    result = m
    return(result)
    
"""
s = "HackerRank.com presents \"Pythonist 2\"."    
print(s)

lst = []

for x in range(0,len(s)):
    if s[x].isupper():
        print(s[x])
        lst.append(s[x].casefold())
    else:
        lst.append(s[x].upper())


m = "".join(lst)
print(lst)  
print(m)

"""
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)