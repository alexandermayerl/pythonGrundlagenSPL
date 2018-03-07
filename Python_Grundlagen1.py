print("Taschenrechner (+, -, *, /, **)")
zahl1 = float(input("Bitte die erste Zahl eingeben"))
zahl2 = float(input("Bitte die zweite Zahl eingeben"))
operation = input("+, -, *, /, oder ** rechnen ?")

if(operation == "+"):
  summe = zahl1 + zahl2
  print("Summe = ", summe)
  
if(operation == "-"):
  differenz = zahl1 - zahl2
  print("Differenz = ", differenz)
  
if(operation == "*"):
  produkt = zahl1 * zahl2
  print("Produkt = ", produkt)
  
if(operation == "/"):
  if(zahl2 == 0):
    print("Man kann nicht durch 0 dividieren")
  if(zahl2 != 0):
    quotient = zahl1 / zahl2
    print("Quotient = ", quotient)
    
if(operation == "**"):
  ergebnis = zahl1**zahl2
  print("Ergebnis = ", ergebnis)

