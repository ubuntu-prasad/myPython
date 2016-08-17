'''
#
# WAP to get the factorial of user defined number. 
#
'''

def fact(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * fact(num - 1)

num = int(raw_input("Enter number less than 1000: "))

#f = fact(num)

print "Factorial of %d is: " % num, fact(num), #f
#print type(f)
#print f.bit_length()