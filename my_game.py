### my_game ###

print("""In a front of you see a deeply dark room.
You couldn't see anything...
You have a choice: enter the room or turn around go run away.
What do you do:
Option #1: enter the room checking out what's going on.
Option #2: run away.""")

player = raw_input("> ")

if player == "1":
    print "You entering the most darkly room you've ever seen"
    print "You're going further..."
    print "Waving your hand you find out two things: #1 candle with matches, #2 flashlight, nothing - your the bravest mutherfucker on the world"
    print "What do you choose?"

    choice = raw_input("> ")

    if choice == "1":
        print "The matches are wet."
        print "You cannot fire the candle"
        print "You are searching for flashlight..."
        print "You cannot find it but you are touching something wet that thing disappearing quickly..."
        print "You are terrified."
        print "You run."
        print "You are hidding under the table and hearing that the Thing is walking around."
        print "You are waiting."
        print ""        
        run = raw_input("> ")

	    

    elif choice == "2":
        print "Flashlight is working. You are happy."
        print "You looking around the room... This is a old room with furniture form the last age."
        print "Suddenly you see big, ugly thing..."
        print "The Thing is comming for you."
        print "Quick! Find something to throw in."
        print "You throwing with flashlight and running away..."

    else:
        "You taking nothig. You are the BOSS!"

elif player == "2":
    print "You are stumble around and falling down the stairs and breaking your neck. You DIE!"

else:
    print "Something ugly was jumped out of the room and grabbed you and dragged to the room... YOU DIE!"



# print "You see the two corridors with light: left and right"
# print "Which do you choose: left #1 or right #2?"
#
# corridoor = raw_input("> ")