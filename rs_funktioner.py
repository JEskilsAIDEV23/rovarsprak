from check import check_char
from check import check_path
from check import check_fil_r


# fil_r = read_new_file()
# funktion för att skapa namnet för en fil att läsa

def read_new_file():

    fil_r = input('Ange en ny fil? eller avsluta programmet med enbart enter: ')
    if fil_r == "":
        print('Programmet avslutas!')
        exit()
    else:
        return fil_r

#rs_funktioner.py innehåller funktionerna för att läsa in en textfil, kryptera med rövarspråk samt spara 
# till en ny fil. Kontroller av importen av filen och dess tecken innehåll görs med importerade och implementerade
# funktioner som importeras från check.py modulen check_char, check_path, check_fil_r
#
#
# text_r, fil_r = text_imp(fil_r, frc)
# 
# Importerar en text fil och extraherar texten, kontroll att filen existerar görs med funktionen check_path(fil_r)
# read_new_file() anropas ifall filen saknas och ger användaren möjlighet att använda en existerande fil och anropar
# på nytt funktionen text_imp(fil_r, frc)
# text innehållet kontrolleras med funktionen check_char(), ifall textfilen saknar tecken ges en varning att programmet kommer att
# avslutas, ifall texten innehåller stora mängder tecken som inte finns i det svenska alfabetet samt siffror, matematik symboler
# ges en varning och fråga om användaren vill fortsätta krypteringen. Ett värde för fraktionen av icke svenska 
# bokstäver frc, kan sättas av användaren i huvudfunktionen som default är frc = 0.5

def text_imp(fil_r, frc = 0.5):

    text_r = ""
    fil_n = "" # blank ifall textfil som ska läsas existerar
    
    if check_path(fil_r) == True: #ser om inputfil existerar

        encode = check_fil_r(fil_r) #kontrollerar input filens kodtabell

        with open(fil_r, 'r', encoding = encode) as f: #läser textfil

            for i in f:
                text_r = text_r + i #extraherar texten rad för rad
            
            if (check_char(text_r, frc)) == True: #kontrollerar textinnehållet m.a.p. tecken innehåll
                return text_r, fil_r
                
            else:
                exit()

    if check_path(fil_r) == False:  
        print("Angiven fil kan inte hittas")

        fil_n = read_new_file() # fil_n namn på ny textfil att importera
        text_r, fil_r = text_imp(fil_n, frc) #rekursivt anrop av text_imp() fil_r motsvaras nu av fil_n

        return text_r, fil_r
        
    return text_r, fil_r

# s2 = rs_transl(text)
# ____________________
# text = utdata text_r från text_imp()
#
# Krypterar texten enligt specifikationen för rövarspråket, användaren har innan fått ett aktivt val att
# att fortsätta ifall texten innehåller många tecken och siffror som inte finns i det svenska alfabetet.
# s2 är variablen som innehåller den krypterade texten 


def rs_transl(text):

    konsonanter = 'bdfghjklmnpqrstvxzBDFGHJKLMNPQRSTVXZ' #små och stora bokstäver gör att inledande konsonant är upper_case
    s2 = ""

    for i in text:
        s2 = s2 + i
        if i in konsonanter:
            s2 = s2 + "o" + i.lower() #andra konsonanten sätts till lower_case

    return s2


# sav_fil() är en funktion för att skapa namnet för filen fil_s där krypterad data sparas

def sav_fil():

    fil_s = input('Vad vill du spara den krypterade filen som: ')
    if fil_s == "":
        fil_s = sav_fil() # rekursivt anrop ifall inget filnamn ges
    else:
        return fil_s
    return fil_s


# text_sav(fil_s, rsprak, encode)
# Sparar krypterad data till filen fil_s
# default sparas krypterad text i formatet UTF-8
# encode parameter ges ifall användaren vill spara till en egen vald teckentabell. Ifall vald 
# teckentabell inte fungerar görs ett försök att spara som utf-8, och prefixet Exception UTF-8_ 
# läggs till i filnamnet. ifall det inte går att spara som utf-8 avslutas programmet
# användaren ges information ifall tomma sparfiler skapats vid exception errors  
# ______________________________________________
# fil_s = namn på sparad fil
# rsprak = utdata s2 från rs_tansl()
# encode = vald teckentabell


def text_sav(fil_s, rsprak, encode = 'utf-8'):

    try:
        with open(fil_s, 'w', encoding = encode) as sav: #sparar den krypterade filen
            sav.write(rsprak)
            return print(f"Fil sparad som {fil_s}")
    
    except UnicodeEncodeError:
        print(f'Tom fil {fil_s} har skapats, den kan tas bort')
        fil_s = 'Exception UTF-8_'+fil_s
        print(f'UnicodeEncodeError för {encode}: försöker spara filen {fil_s} i UTF-8: ')
        
        try:
            with open(fil_s, 'w', encoding = 'utf-8') as sav:
                sav.write(rsprak)
                return print(f"Fil sparad som {fil_s} i UTF-8")
        
        except UnicodeEncodeError:
            print(f'Den krypterade filen {fil_s} kunde inte sparas i UTF-8')
            print(f'Tom fil {fil_s} har skapats, den kan tas bort')
            