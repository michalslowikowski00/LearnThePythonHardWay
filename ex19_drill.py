#study drill - my own new function

# crossfit function

# global var for function
pullup = 5
pushup = 10
squat = 15

print """
Alright! Listen up fellows!
You can do this WOD in this way.
Here's the drill:
"""

def workout_of_the_day(pullup, pushup, squat):
	print "The first exercise is to make %r pullups." % pullup
	print "If you finish the %d pullups then you get to do is %d of pushups." % (pullup, pushup)
	print "Next to do after %d pullups and %d pushups is to do %d of squat with the great technique.\n" % (pullup, pushup, squat)
	
workout_of_the_day(pullup, pushup, squat)

# another way to do it with other arguments:
print "Another way to do it:"
workout_of_the_day(100,100,100)

# the other way
print "Maybe this fuckers!"
numer_of_pullup = 5
numer_of_pushup = 10
numer_of_squat = 15

workout_of_the_day(numer_of_pullup, numer_of_pushup, numer_of_squat)

# one more def of WOD

print"Do this my spartans!"

workout_of_the_day(numer_of_pullup + 5, numer_of_pushup + 5 , numer_of_squat + 5)


print """
Let's go!
Start in two minutes!
Get this shit done! 
Give all you can!
Remeber! This is fucking EMOM!
"""

