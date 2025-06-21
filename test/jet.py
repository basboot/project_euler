cijfer1 = int(input("geef hier het eerste cijfer: "))
cijfer2 = int(input("geef hier het tweede cijfer: "))
cijfer3 = int(input("geef hier het derde cijfer: "))

getallen = [cijfer1, cijfer2, cijfer3]
print(getallen)
getallen.remove(cijfer2)
print(getallen)
print(sum(getallen))



wachtwoord = input("geef je wachtwoord: ")
if wachtwoord.isnumeric():
    print("cijfers")
elif wachtwoord.isalpha():
    print("letters")
else:
    print("combinate")






name = input("wat is je naam?: ")

print("Hallo " + name)

a = input("Geef een getal: ")

# error, want a is een string (zelfs al zet je er een 2 in)
# print(a / 2)

# Python maakt van dse string (tekst) nu een getal (int)
b = int(input("Geef een getal: ")) # of float als je weet dat er een kommagetal komt

print(b / 2)

# Je kunt een string en getal niet optellen, maak van b een string om hem eraan vast te plakken
print("B = " + str(b))

lijst_met_getallen = [1, 23, 4, 45, 34, 23, 234, 45, 456, 456]

print(lijst_met_getallen[0])

hi = [ [1, 2, 3], [4, 5, 6] ]

print(hi[0][0]) # eerste 0, is eerste lijst [1, 2, 3], tweede 0 haalt eerste item uit die eerste lijst, dus 1


# range maakt een lijst met gehele getallen, de eerste is de start, de tweede het eind, dat niet mee doet (tot, niet tot en met)
print(range(5, 10))

# len geeft aan hoeveel er in een lijst zitten
print(len(lijst_met_getallen))

# sum telt alles in een lijst op
print(sum(lijst_met_getallen))

# met append voeh je iets toe, en met remove verwijder je
lijst_met_getallen.append(19)
lijst_met_getallen.remove(4)
print("456 staat " + str(lijst_met_getallen.count(456)) + " keer in de lijst" )

hallo = input("Geef een getal of iets anders: ")

if hallo.isnumeric(): # isalpha zou het omgekeerde doen
    print("Dat is een getal")
else:
    print("Dat is geen getal")
