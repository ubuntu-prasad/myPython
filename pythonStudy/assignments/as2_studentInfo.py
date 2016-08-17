# Assignment No.2 : WAP to create a DS of students (define DS as per the protocols)
# and print the sum of scores in five subjects and gets the each student percentage.

# variable declaration

name = ""
marks = []
studentInfo = {}
addMore = 'y'
sum1 = 0
per = 0

while addMore != 'n':
    name = raw_input("Enter Name of student: ")

    for i in range(1,6):
        marks.extend([input("Enter mark of subject %d : " % i)])

    for i in range(5):
        sum1 = sum1 + marks[i]

    per = sum1 / 5.0

    marks.extend([sum1, per])           # appends data in list
    
    studentInfo[name] = marks

    addMore = raw_input("Do you want to continue - y or n :")
    marks = []
    sum1 = 0
    
else:
    print "Data insertion complete. \nDisplaying Result:\n"


print "Name \tMarks \t\t\tTotal  %tile"
print "*" * 50

for key in studentInfo:
    print key,
    print "\t", studentInfo[key][:5],
    print "\t", studentInfo[key][5:]

print "*" * 50
    
#print studentInfo
#print name, marks
