import numpy

def arrays(arr):
  #arr =  input().strip().split(' ')
  x = numpy.array(arr, dtype = 'f')
  #print(x)
  return(numpy.flip(x))




arr = input().strip().split(' ')
result = arrays(arr)
print(result)

"""
Sample Input

1 2 3 4 -8 -10
Sample Output

[-10.  -8.   4.   3.   2.   1.]
"""