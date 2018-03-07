import random
zufallszahl = random.randint(1,101)

print("Zahlraten - errate eine Zahl zwischen 1 und 100")
versuche = 0


gewonnen = False
while gewonnen == False: 
  zahl = int(input("Welche Zahl?"))
  versuche = versuche + 1
  if (zahl == zufallszahl):
    print("Gratuliere! du hast die Zahl erraten.")
    gewonnen = True
  elif (zahl < zufallszahl):
    print("Leider Nein! Die gesuchte Zahl ist größer.")
  elif (zahl > zufallszahl):
    print("Leider Nein! Die gesuchte Zahl ist kleiner.")
    
print("Versuche: ", versuche)