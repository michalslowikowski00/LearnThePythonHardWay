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
            print "fooboo"
        else:
            print "DIE!"
    elif "lay" in choice:
	    print "new function" # nothing
    else:
        print "new function" # nothing
        
start()