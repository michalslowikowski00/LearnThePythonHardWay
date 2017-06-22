# def - function and name for it cheese_and_crakers with two arguments.
# def prints on the screen four string with agruments

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print"You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for party!"
    print "Get a blanket. \n"
# this line of code says that arguments of function cheese_and_crackers has values 20 and 30
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# this line shows that we can define the new variables in the diferent way
print "OR, we cans use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# we can do math inside the function
print"We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# we can combine with variables and do math with them
print "And we can combine the two, variables and math"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
