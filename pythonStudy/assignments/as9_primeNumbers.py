'''
#
# as9_primeNumbers.py : WAP to find the first hundred prime numbers.
#
'''

print "First 100 Prime numbers are: "
print "2",

count = 0

for i in range(3, 1000, 2):
    j = 2
    flag = 0
    while j ** 2 < i:
        if i % j == 0:
            flag = 1
            break
        j = j + 1

    if flag == 0:
        print i,
        count += 1

        if count % 10 == 0:
            print "\n"
            
        if count == 100:
            break

print "\nTotal Prime Numbers: ", count