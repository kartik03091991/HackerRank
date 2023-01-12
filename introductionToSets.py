# sets are not iterable

def average(array):
    #n = int(input())
    #arr = list(map(int, input().split()))

    #print(n)
    #print(arr)

    set1 = set(arr)
    lst1 = list(set1)
    #print(set1)
    #print(lst1)

    total = 0
    for x in range(0,len(lst1)):
        total += lst1[x]

    #print(total)
    result = float(total)/float(len(lst1))
    return float(result)

    



    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)