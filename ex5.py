my_name = 'Michal'
my_age = 30
my_height = 180 # in cm
my_weight = 75 # in kg
my_eyes = 'grey'
my_teeth = 'white'
my_hair = 'blond'

print "Let's talko about %s" % my_name
print "He's %d cm tall" % my_height
print "He's %d kg heavy" % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" % (my_eyes, my_hair)
print "His teeth are usually %s depending on the caffee." % my_teeth

# this line is tricky, try to get exectly right
print "If I add %d, %d, and %d i get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)