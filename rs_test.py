from rovarsprak import rovare

# användargränsnitt som anropar huvudfunktionen rovare(fil_r, frc, encode)
# Huvudfunktionen anropas med default inställningar för frc och encode
# ifall inga värden anges
# Val att se den sparade krypterade texten på skärmen ges



fil_r = input('Ange en text fil: ')
val_e = input('Vill du spara filen i annat format än UTF-8? Ja (J), Nej (enter = UTF-8):')

if val_e == "J" or val_e == "j":
    encode = input('Ange Teckentabell ex. cp1252: ')
    if encode == "":
        print('Ingen tabell vald, UTF-8 används')
        encode = 'utf-8'
else:
    encode = 'utf-8'

frc = input('Ange hur noga icke svenska bokstäver granskas 0.00 - 1.00, default (0.50 = enter): ')

    #Huvudfunktionen anropar funktioner för att läsa och kontrollera inputfilen och dess textinnehåll 
    # samt för att kryptera och kontrollera att det går att spara resultatet i en ny textfil med default
    # eller vald teckentabell. 
val = input('\nVill du granska den krypterade texten på skärmen: Ja (J) eller N (enter):')
if val == "J" or val == "j":
    print('\n___Resultat av Text krypterad till Rövarspråk___\n'+rsprak)
else:
    exit()

