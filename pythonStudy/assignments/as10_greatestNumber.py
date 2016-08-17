'''
#
# WAP to accept three inputs from the user and find the greatest number among 3 numbers.
# (Get three numbers from raw_input)
#
'''

num1 = int(raw_input("Inter number 1: "))
num2 = int(raw_input("Inter number 2: "))
num3 = int(raw_input("Inter number 3: "))

max = 0

if num1 < num2:
    if num3 < num2:
        max = num2
    else:
        max = num3
elif num1 < num3:
    max = num3
else:
    max = num1

print "Maximum number amoung %d, %d, %d is: " % (num1, num2, num3), max
                