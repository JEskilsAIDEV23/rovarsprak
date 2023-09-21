from rovarsprak import rovare
from rs_klona_rep import RS_Git_txt
from rs_klona_rep import klona_remote_git


def rs_ui():

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

    rsprak = rovare(fil_r,'', encode = 'utf-8', frc = 0.5)

    val = input('\nVill du granska den krypterade texten på skärmen: Ja (J) eller N (enter):')
    if val == "J" or val == "j":
        print('\n___Resultat av Text krypterad till Rövarspråk___\n'+rsprak)
    else:
        exit()

def rs_Git():

    #Funktionen rs_Git() anropar funktioner för att klona ett angivet Git-reository
    #Text filer med filändelsen .txt i det klonade repository krypteras och läggs i en lokal 
    # mapp tillsammans med en textfil som innehåller ursprungsfilnamn och den krypterade filens namn

    repo_url = input('Ange en länk till ett Git-Repository med textfiler som skall krypteras: ')

    try:
        #repo_url = 'https://github.com/AIDEV23S/svText'
        klona_remote_git(repo_url) #Klonar angivet Git

    except:
        print(f'Det gick inte att klona angivet repository {repo_url}')
        print('Programmet avslutas')
        exit()

    RS_Git_txt() #Krypterar de text-filer som finns i angivet Git

choose = input('Vill du köra en batch kryptering genom att klona ett Git-Repository ange G, annars enter: ')

if choose == 'G' or choose == 'g':
    rs_Git()
else:
    rs_ui()        


