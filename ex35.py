#import from system exit function. Is a exit python.
from sys import exit

#function gold_room()
def gold_room():
    print "This room is full of gold. How much do you take?"
    
    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)   #checking if the choice from raw_input is a number (integer)
    else:
        dead("Man, learn to type number.")   #calling dead() function (is define below, line 59)
        
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)   # exit(0) if in the argument is integer (number), zero is
    else:   # considered "successful termination".
        dead("You greedy bastard!")   # Any nonzero value is considered "abnormal termination."
        
# end of function gold_room
    
# function bear_room()        
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False   # variable bear_moved and the value is boolean False
    
    while True:   # the loop while
        choice = raw_input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved form the door. You can go through it now."
            
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed of and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."
            
def cthulhu_room():
    print "Here you can see great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    
    choice = raw_input ("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
        
        
def dead(why):
    print why, "Good job!"
    exit(0) # exit(0) if in the argument is integer (number), zero is
            # considered "successful termination".
            # Any nonzero value is considered "abnormal termination."
    
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    
    choice = raw_input("> ")
    
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
        
        
start() # calling the start function which is define on line 65 of program

