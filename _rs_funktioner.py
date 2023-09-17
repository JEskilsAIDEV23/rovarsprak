from check import check_char
from check import check_path
from check import read_new_file
from check import save_new_file

#rs_funktioner.py innehåller funktionerna för att läsa in en textfil, kryptera med rövarspråk samt spara 
# till en ny fil. Kontroller av importen av filen och dess tecken innehåll görs med importerade och implementerade
# funktioner som importeras från check.py modulen check_char, check_path, read_new_file, save_new_file.


# text_r, fil_r, fil_n = text_imp(fil_r, frc)
# ___________________________________________

# Importerar en text fil och extraherar texten, kontroll att filen existerar görs med funktionen check_path(fil_r)
# read_new_file() anropas ifall filen saknas och ger användaren möjlighet att använda en existerande fil och anropar
# på nytt funktionen text_imp(fil_r, frc)
# text innehållet kontrolleras med funktionen check_char(), ifall textfilen ges en varning att programmet kommer att
# avslutas, ifall texten innehåller stora mängder tecken som inte finns i det svenska alfabetet samt siffror, matematik
# ges en varning och fråga om användaren vill fortsätta krypteringen. Ett värde för fraktionen av icke svenska 
# bokstäver frc, kan sättas av användaren i huvudfunktionen som default är frc = 0.5

def text_imp(fil_r, frc = 0.5):

    text_r = ""
    fil_n = "" # blank ifall textfil som ska läsas existerar

    if check_path(fil_r) == False:  
        print("Angiven fil kan inte hittas")

        fil_n = read_new_file() # namn på ny textfil att importera
        text_r, fil_r, fil_n = text_imp(fil_n, frc) #rekursivt anrop av text_imp()

        return text_r, fil_r, fil_n
    
    if check_path(fil_r) == True:
        with open(fil_r, 'r', encoding = 'utf-8') as f: #läser textfil

            for i in f:
                text_r = text_r + i #extraherar texten rad för rad
            
            if (check_char(text_r, frc)) == True: #kontrollerar textinnehållet m.a.p. tecken innehåll
                return text_r, fil_r, fil_n
                
            else:
                exit()
        
    return text_r, fil_r, fil_n

# s2 = rs_transl(text)
# ____________________
# text = utdata text_r från text_imp()
#
# Krypterar texten enligt specifikationen för rövarspråket, användaren har fått ett aktivt val att
# att fortsätta ifall texten innehåller många tecken och siffror som inte finns i det svenska alfabetet.
# s2 är den krypterade texten som sedan 


def rs_transl(text):

    konsonanter = 'bdfghjklmnpqrstvxzBDFGHJKLMNPQRSTVXZ' #små och stora bokstäver gör att inledande konsonant är upper_case
    s2 = ""

    for i in text:
        s2 = s2 + i
        if i in konsonanter:
            s2 = s2 + "o" + i.lower() #andra konsonanten sätts till lower_case

    return s2

# text_sav(fil_r, fil_n, rsprak, prefix = 'rs_')
# ______________________________________________
# rsprak = utdata s2 från rs_tansl()
# fil_r = läst fil
# fil_n = fil ifall fil_r inte existerade
# prefix = en möjlighet att ge sparfilen ett automatiskt skript för att underlätta identifiering av krypterade
# filer samt för att undvika att någon fil skrivs över. 
# Kontroll ifall en sparfil existerar görs även med check_path()


def text_sav(fil_r, fil_n, rsprak, prefix = 'rs_'):

    if fil_n == "": #Kontroll att fil_r existerade
        fil_s = prefix+fil_r #namnger sparfilen med valt prefix, default = 'rs_'
        if check_path(fil_s) == True: #Kontrollerar ifall sparfil redan finns
            fil_s = save_new_file(fil_s) #Ifall sparfil finns ge användare möjlighet att ge nytt namn

    else:
        fil_s = prefix+fil_n #namnger sparfilen med valt prefix, default = 'rs_'
        if check_path(fil_s) == True: #Kontrollerar ifall sparfil redan finns
            fil_s = save_new_file(fil_s) #Ifall sparfil finns ge användare möjlighet att ge nytt namn

    with open(fil_s, 'w', encoding = 'utf-8') as sav: #sparar den krypterade filen
        
        sav.write(rsprak)

    return print(f"Fil sparad som {fil_s}")