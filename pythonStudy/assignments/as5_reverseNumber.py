'''
as5_reverseNumber : WAP to reverse a given number.
'''
num = raw_input("Enter Number: ")
num = eval(num)
rnum = 0

while(num):
    rnum = rnum * 10 + num % 10
    num /= 10

print rnum