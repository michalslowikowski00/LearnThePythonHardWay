# import module form python
from sys import argv

# name of script and adding to the argument
script, input_file = argv

# declare function print_all with 'f' argument
def print_all(f):
    print f.read() # the method read() reads the file. 
    			   # Without 'count - object.file(count - there can be a number)' 
    			   # method read() trying to read as much as it can

# declare rewind function that sets the file in the current position    
def rewind(f): 
    f.seek(0) # setting the file in the current position

# declare function with two arguments line_count and f 
def print_a_line(line_count, f):
    print line_count, f.readline(),
    
current_file = open(input_file)

print "First let's print the whole file:\n"

# calling the function print_all with current_file as a argument    
print_all(current_file)


print "Now let's rewind, kind of like a tape."

# calling rewind function with current_file as argument
rewind(current_file)

print "Let's print three lines:"


current_line = 1 # adding 1 as a value to the variable
print_a_line(current_line, current_file) # calling function with arguments current_line, current_file

current_line = current_line + 1 # adding 1 as a value to the variable with value 1
print_a_line(current_line, current_file) # calling function with arguments current_line, current_file

current_line = current_line + 1 # adding 1 as a value to the variable with value 2
print_a_line(current_line, current_file) # calling function with arguments current_line, current_file