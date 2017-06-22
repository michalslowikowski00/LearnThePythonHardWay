# function drill
# return number 998

g_value = 998

def add(a, b):
    print "adding %d + %d" % (a, b)
    return a + b
    
def substract(a, b):
    print "substract %d - %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "mulitply %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
	print "Divide %d / %d" % (a, b)
	return a / b

print "Ok, let's do some math with this thing."

one = add(666, 666) # 1332
two = substract(400, 100) # 300 # 1332 - 334 = 998
three = multiply(8, 4) # 1332 - 300 = 1032
four = divide(68, 2) #34 || 1032 - 34 = 998

print "Ok, let's look at the result."

def score(a, b, c, d):
    print "Let's print the g_value: ",
    return a - b - c - d

g_value = score(one, two, three, four)

print g_value

