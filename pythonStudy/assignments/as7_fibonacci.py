'''
#
# as7_fibonacci : WAP to create a Fibonacci series of n numbers.
# 
'''

num = eval(raw_input("Enter number: "))

print "Fibonacci Series for %d: \n starting with f(0) = 0,  f(1) = 1: \n 0" % num,
a, b = 1, 0

while num:
    fib = a + b
    a = b
    b = fib
    print fib,
    num -= 1