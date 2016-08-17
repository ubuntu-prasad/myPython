'''
#
# WAP to check whether the user input number is Prime, Armstrong number and find out the ascii value of that number.
#
'''

number = raw_input("Enter any Integer number: ")
num = int(number)

# Function to find number is Prime or NOT

def isPrime(num):
    x = 2
    while x * x < num:
        if num % x == 0:
            return 0        # 0 = false = number is NOT prime
        x += 1

    return 1        # 1 = true = number is prime

# Number is Prime or NOT

if isPrime(num):
    print num, "is Prime Number."
else:
    print num, "is NOT Prime Number."


# Number is Armstrong or NOT

number = list(number)

if number[::] == number[::-1]:
    print num, "is Armstrong Number."
else:
    print num, "is NOT an Armstrong Number."


# Binary representation of aNumber

print "Binary representation of %d :", bin(num)