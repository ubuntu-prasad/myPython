'''
#
# WAP to get the count of words in the statement string and the count of vowels in complete statement.
#
'''
string = raw_input("Enter String:\n")

string = string.upper()

count = 0

for ch in string[:]:
    if ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        count += 1

print "Number of Words in String is/are: ", len(string.split())
print "Number of Vowels in statement is/are: ", count