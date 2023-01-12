import numpy
from warnings import filterwarnings
filterwarnings(action='ignore', category=DeprecationWarning, message='`np.int` is a deprecated alias')

lst = list(map(int,input().split()))


if len(lst) == 2:
    N = int(lst[0])
    m = int(lst[1])  

      
if len(lst) == 3:
    N = int(lst[0])
    m = int(lst[1]) 
    n = int(lst[2])
        
if len(lst) == 4:
    N = int(lst[0])
    m = int(lst[1]) 
    n = int(lst[2])
    p = int(lst[3])
    
    
#for x in range(0,len(lst)):
if len(lst) == 2:
      print(numpy.zeros((N,m), dtype = numpy.int))
      print(numpy.ones((N,m), dtype = numpy.int))
      
if len(lst) == 3:
      print(numpy.zeros((N,m,n), dtype = numpy.int))
      print(numpy.ones((N,m,n), dtype = numpy.int))

if len(lst) == 4:
      print(numpy.zeros((N,m,n,p), dtype = numpy.int))
      print(numpy.ones((N,m,n,p), dtype = numpy.int))
      
      
      
#print(N)
#print(m)
#print(n)

#print(numpy.zeros((N,m,n), dtype = numpy.int))
#print(numpy.ones((N,m,n), dtype = numpy.int))
"""
for x in range(0,N):
    if x == N-1:
       print(numpy.zeros((m,n), dtype = numpy.int))
    else: 
       print(numpy.zeros((m,n), dtype = numpy.int), end = "\n\n")
    
for x in range(0,N):
    print(numpy.ones((m,n), dtype = numpy.int), end = "\n\n")
    
"""
"""
Sample Input 0

3 3 3
Sample Output 0

[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
Explanation 0

Print the array built using numpy.zeros and numpy.ones tools and you get the result as shown.
"""