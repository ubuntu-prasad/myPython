'''
#
# ex17_fileOperations: Copy content of one file to another
#
'''
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
# indata = open(from_file).read()

input = open(from_file)
indata = input.read()

print "The input file is %d bytes long." % len(indata)

print "Does the output file exist? %r " % exists(to_file)
print "Ready, hit Return to continue, CTRL-c to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."