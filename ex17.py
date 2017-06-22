#import module form system
from sys import argv
#import os.path module with argument EXISTS
from os.path import exists

# script, with two velues, form_file (with name which i can give) and the same with to_file
script, from_file, to_file = argv

# copying data form one file to another
print "Copying form %s to %s" % (from_file, to_file)

#we could write this two line in a one line, how?
# OIN ONE LINE in_file = open(from_file) ; indata = in_file.read() ... i think.
# in_file - new variable is open function
in_file = open(from_file)
# in data is new variable with function open and read method
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

# exists file is argument from os.path which was declered at the begining of the program 
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# out_file - new var with open function with 'w' (write argument) which is writing the data and eraseing the old one
out_file = open(to_file, 'w')
# out_file is writing the data form var in_data which is function .read()
out_file.write(indata)

print "Alright, all done"

# elegant closing the files - is important to close the files to relese the machine memory
out_file.close()
in_file.close()

