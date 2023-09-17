def rovare(fil_r, frc = 0.5):

    from check import check_param
    from check import check_save_file
    from rs_funktioner import text_imp
    from rs_funktioner import rs_transl
    from rs_funktioner import sav_fil
    from rs_funktioner import text_sav

    frc = check_param(frc)
    text_r, fil_r = text_imp(fil_r, frc)
    rsprak = rs_transl(text_r)
    fil_s = sav_fil()
    fil_s = check_save_file(fil_s)
    text_sav(fil_s, rsprak)

    return rsprak

#felhantering
#______________
#path fel
#filtyp fel
#hantering av tecken eller nummer som inte ingår i alfabetet och undantag ".,!:; " från felrapport
#kolla om sparfil finns och är ok att skriva över eller skapa ny