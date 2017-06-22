#my_game

def room_with_gold():
    print "This is the room first with i dont'know what"
    print "There is some gold. You can take some. How much do you take?"    
    
    greed = raw_input("> ")
    
    if "0" in greed or "1" in greed: # what 0 or 1???
        how_much = int(greed)
    else:
        dead("man, you have to learn how to type strings!")
        #function dead() is define below
    
    if how_much < 500:
        print "Damn, you are not greedy..."
        exit(0)
    else:
        dead("You are greedy motherfucker... You DIE!")
        #function dead() is define below

def right_room():
    print "You are entering to the room with nothing."
    print "You can see nothing"

### DEATHS ###
### And diferent types of them ###

def dead(why):
     print why, "You know nothing John Snow... DIE!"
     exit(0)
    
# death by burpees
def death_brupees(why):
    print why, "Ivisble force force you to do brupees until you die. You make thousands of them and die."
    exit(0)
    
def start():
    print "You are waking up..."
    print "You cannot recognize this place."
    print "What do you do?"
    
    choice = raw_input("> ")
    
    if "stand" in choice:
        print"You see the two doors."
        print "On the left and the right."
        print "What do you choose?"
        
        door = raw_input("> ")
        
        if "left" in door:
            room_with_gold()
        elif "right" in door:
            death_abyss() # the other room
        elif "run" in door:
            
        else:
            print "DIE!"
    elif "lay" in choice:
	    print "new function" # nothing
    else:
        print "new function" # nothing
        
start()

# death by run
def death_abyss(why): # should i use why argument?
    print why, "You running away through darkness and fall to the abyss."
    exit(0)
        
        
        