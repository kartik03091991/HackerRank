#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])  

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    #print(n)
    #print(m)
    #print(arr)
    #print(k)
    arrt = tuple(arr)
    #print(arrt)
    #sorted()
    fin = list(sorted(arrt, key = lambda arrt: arrt[k]))
    #print(fin)
    #q = "".join(str(fin))
    #print(q)
    

    for x in range(0,len(fin)):
        #print(fin[x],len(fin[x]),"line1")
        for y in range(0,len(fin[x])):
            print(fin[x][y],end = " ")
        print()
            #print("line1")
    #for y in range(0,len(fin)):

    