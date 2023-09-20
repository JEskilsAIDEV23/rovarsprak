def rovare(fil_r, fil_s = "", encode = 'utf-8', frc = 0.5):

    #Huvudprogram rovare.py kallar på underfunktioner för att läsa in en inputfil, för att sedan
    # kontrollera dess path, teckenkod och teckeninnehåll före kryptering. Efter krypteringen 
    # anropas underfunktioner för att skapa en utdatafil och kontrollera dess path och att den 
    # kan sparas med en egen vald teckenkod tabell eller default UTF-8.
    # Huvudprogrammet importerar funktioner från två moduler check.py och rs_funktioner.py
    # check modulen innehåller de funktioner som är namngivna som check_#() och anropas av både 
    # rs_funktioner och huvudprogrammet. check modulen innehåller de funktioner som kontrollerar
    # in parametern frc, path för indata- och utdatafilen, textinnehållet och textkodning.
    # rs_funktioner innehåller de funktioner som läser, krypterar, och skapar utdatafilen.

    #rovare.py kan köras enbart med fil_r angivet och kommer då att använda default parametrar
    #samt fråga efter namn på en sparfil, anges ett namn för fil_s används det istället för inmatning.
    #default sparas texten i formatet UTF-8. 
    #Inläsningskontroll av indata m.a.p. UTF-8 eller cp1252 görs alltid, 

    from check import check_param
    from check import check_save_file
    from rs_funktioner import text_imp
    from rs_funktioner import rs_transl
    from rs_funktioner import sav_fil
    from rs_funktioner import text_sav

    frc = check_param(frc)
    text_r, fil_r = text_imp(fil_r, frc)
    rsprak = rs_transl(text_r)

    if fil_s == "":
        fil_s = sav_fil()
    else:
        fil_s = fil_s

    fil_s = check_save_file(fil_s)
    text_sav(fil_s, rsprak, encode)

    return rsprak

#felhantering
#______________
#path fel
#filtyp fel
#hantering av tecken eller nummer som inte ingår i alfabetet och undantag ".,!:; " från felrapport
#kolla om sparfil finns och är ok att skriva över eller skapa ny

#
# rovare('russian.txt','text_rus.txt')
