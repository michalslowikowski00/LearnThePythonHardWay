# i = 0 # variable called i equals to 0
# numbers = [] # empty list of data
# 
# # while-loop is ogoing on when the statmen is good, whicj is mean when the i is less then 6
# while i < 6: 
#     print "At the top i is %d" % i # then we print i which in this case is 0
#     numbers.append(i) # to the number (empty list) we adding i (variable equals 0)
#     
#     # in the next block of code we define variable i with i + 1 which is means that to the next step of looping we adding 1 to the i, in e.g.: 1 + 1 = 2; 2 + 1 = 3 etc.
#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i
#     
#     
# print "The numbers: "
# 
# for num in numbers:
#     print num

################# the drills ########################

print "\nConverting while-loop to function drill_1"

def drill_1(b):
    i = 0
    numbers1 = []
    while i < b:
        print "Item: %d" % i
        numbers1.append(i)
        i = i + 1
        print numbers1
        
drill_1(3)

drill_1(9)        

#################### for loop ########################


for i in range(10):                    # RANGE - in this line create loop with range 10, the iteration will be doing until it get to 10
    numbers = []                       # numbers = [] is a empty list
    print "Item %d" %i                 # printing i 
    numbers.append(i)                  # appending (adding to the end of list) the argument (i) which is define by i = i + 1 in the line below 
    
    i = i + 1                          # this line define the variable i; to each line of looping code the i will be increasing by 1
    print "numbers now: ", numbers     # printing data from list come numbers 
    print "At the bootom i is %d" % i  # printing the value of variable i - it depends of line of loop
    
#print numbers 


    

    