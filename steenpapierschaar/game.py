# importeer de random module
import random

# Print spelinstructies af
print("Blad steen schaar win je op de volgende manier: \n"
      + "Steen vs papier->Papier wint \n"
      + "Steen vs schaar->Steen wint \n"
      + "Blad vs schaar->Schaar wint \n")


while True:
    print("Kies uit \n 1. steen \n 2. papier \n 3. schaar \n")

    # neem input van de gebruiker
    choice = int(input("Jouw beurt: "))

    # loop tot er een ongeldige waarde wordt ingegeven
    while choice > 3 or choice < 1:
        choice = int(input("Geef een geldige input: "))

    # de keuze van de gebruiker aan een variabele koppelen
    if choice == 1:
        choice_name = 'steen'
    elif choice == 2:
        choice_name = 'papier'
    else:
        choice_name = 'schaar'

    # print user choice
    print("Uw keuze is: " + choice_name)
    print("\nNu is het de beurt aan de computer.......")

    # De computer kiest willekeurig een nummer van de random module
    comp_choice = random.randint(1, 3)

    # loop totdat de computer keuze is gelijk aan de waarde van de keuzemogelijkheden
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    # de keuze van de computer wordt gekoppeld aan een variabele
    if comp_choice == 1:
        comp_choice_name = 'steen'
    elif comp_choice == 2:
        comp_choice_name = 'papier'
    else:
        comp_choice_name = 'schaar'

    print("De keuze van de computer is: " + comp_choice_name)

    print(choice_name + " vs " + comp_choice_name)

    # voorwaarden om te winnen
    if ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 1)):
        print("papier wint => ", end="")
        result = "papier"

    elif ((choice == 1 and comp_choice == 3) or
          (choice == 3 and comp_choice == 1)):
        print("steen wint =>", end="")
        result = "steen"
    else:
        print("schaar wint =>", end="")
        result = "schaar"

    # Print af of de gebruiker of de computer gewonnen is
    if result == choice_name:
        print(" ** Jij hebt gewonnen ** ")
    else:
        print(" ** De computer heeft gewonnen ** ")

    print("Wil je nog eens spelen? (J/N)")
    ans = input()

    # als de gebruiker n of N ingeeft, stopt het programma
    if ans == 'n' or ans == 'N':
        break

# nadien komen we uit de while loop en willen we de gebruiker bedanken om het spel te spelen
print("\nBedankt om te spelen!")
