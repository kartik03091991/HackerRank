#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
 lst1 = list(s.split())   
 for x in range(0,len(lst1)):
    #spaceb = s.find(" ")
    #a = s.find(lst1[x])
    #print(a ,"line1")
    #print(spaceb , "line2")
    wordA = lst1[x]
    s1 = s.replace(wordA,wordA.capitalize())
    s = s1
 return(s)    
     
        
   




        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


"""

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan
"""