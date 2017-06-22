# importuje modul z systemu, zeby odpalic program
from sys import argv

# uruchamia skrypt o nazwie jaka podam, tu ex15_sample.txt
script, filename = argv

# zmienna txt wywoluje funkcje otwarcia pliku tekstowego
txt = open(filename)


print "Here's your file %r: " % filename
# print txt.read() - funkcja drukujace tresc pliku ex15_sample.txt na ekranie
print txt.read()

print "Type the filename again:"
#file_again - zmianna przechwytujaca nazwe pliku ex15_sample.txt, ktora wspisuje user
file_again = raw_input("> ") 

txt_again = open(file_again)
 
print txt_again.read()
