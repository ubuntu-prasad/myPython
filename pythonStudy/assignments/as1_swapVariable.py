# Swap values of two variables without using third variable

var1 = input("NOTE: Please enter only INTEGER value else program will fail: ");
var2 = input("NOTE: Please enter only INTEGER value else program will fail: ");

print "Values before swapping:"
print "var1 = ", var1
print "var2 = ", var2

print '*' * 20

var1 = var1 + var2
var2 = var1 - var2
var1 = var1 - var2



print "Values after swapping:"
print "var1 = ", var1
print "var2 = ", var2

print '*' * 20   