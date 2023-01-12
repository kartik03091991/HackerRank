
def print_rangoli(size):
    #size = 5
    for i in range(1,size*2):   # size = 5 (1,10)
        lst = []
        if i<=size:               # 1 <= 5
            for j in range(i):    # j in 2  96 +5-0 = 101 = e  96 +5 -1 = 100 = d
                lst.append(chr(96+size-j))   # lst = ['e', 'd']
               # print(lst)
            for k in range(i-1):         # k in 0
                lst.append(chr(96+size-i+2+k))  # 96+5-1+2+0 = 101 e
                #print(lst)
        else:
            for j in range(2*size - i):
                lst.append(chr(96+size-j))
            for k in range(2*size-i-1):
                lst.append(chr(96+k+i-size+2))
        print('-'.join(lst).center(size*4-3,'-'))




        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)