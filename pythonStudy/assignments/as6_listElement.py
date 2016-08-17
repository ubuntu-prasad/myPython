'''
# WAP to find the distinct, duplicate and unique elements between two  a list.
#
# Assuming :
#           distinct  = present in list one or more times
#           unique    = appeared only once
#           duplicate = present more than once
'''
l1 = [1,2,3,1,5,6,6,3,7,8,8,8,9]

dup  = []
uni = []

dist  = list(set(l1))

# n = input("Numbers of Elements in list1: ")

for i in l1:
    if l1.count(i) == 1:
        uni.append(i)
    else:
        dup.append(i)

print "Unique Elements: ", uni
print "Distinct Elements: ", dist
print "Duplicate Elements: ", list(set(dup))