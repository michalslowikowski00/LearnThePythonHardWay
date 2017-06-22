from sys import argv

# wywoluje skrypt z nazwy pliku
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit the RETURN."

raw_input("?")

# target - nowa zmienne wywolujaca funkcje otwarcia pilku FILENAME, argument 'w' otwiera plik do funkcji write/do zapisu danych.
print "Opening the file...!"
target = open(filename, 'w')

# zmienna TARGET wywoluje funkcje TURNCATE 
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

# trzy nowe zmienne z raw_input, ktore zostana przekazane do target.write(line...)
# user wpisuje co chce - to zostanie przezkazane do pliku
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# target.write - fukcja zapiesuje to co zostalo wstukane przez usera w line... = raw_input('line1: ')
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# eleganckie zamkniecie programu .cloe() - metoda zmiennej target, ktora zostala zdefiniowana wczesniej
print "And finally, we close it."
target.close()