#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first_name, last_name):
   y = "Hello" + " " + first_name + " " + last_name + "! You just delved into python."
   print(y)


#first_name = "Ross"
#last_name = "Taylor"
#print(first_name)
#print(last_name)
#x = first_name + last_name
#print(x)
#print_full_name(first_name, last_name)

#Hello Ross Taylor! You just delved into python.

"""   
first_name = 'Ross'
last_name = 'Taylor'
print_full_name('Ross','Taylor')
print(print_full_name)
"""
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)