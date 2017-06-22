""" study drills form ex33 lear the python hard way """

def ex_drill(n):
    i = 0
    numbers = []
    
    for i in range(10):
        print "the number is %d" % i
        numbers.append(i)
        
        i = i + 1
        print "the number is %d" % i, numbers
        print "some shit"

# ex_drill(1)

print ex_drill(3)
