'''
# WAP to find out the leap year. (Except a year from the user using raw_input)
'''

year = eval(raw_input("Enter Year: "))

#'''
if year % 4 == 0 and year % 400 == 0:
    print "%d is a Leap Year." % year
else:
    print "%d is NOT a Leap Year." % year

'''
# Why to devide by 400: 

for yr in range(0, year, 4):
    if yr % 4 == 0 and yr % 400 == 0:
        print yr,
 #       if yr % 100 is 0:
  #          print "\n"
#'''