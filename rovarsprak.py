from rs_funktioner import text_imp
from rs_funktioner import rs_transl
from rs_funktioner import text_sav


#______Main______


def rovare(fil_r, prefix = "rs_", frc = 0.5):

 #   check_encode('rovarsprak_svenskt_text.txt')
    text_r, fil_r, fil_n = text_imp(fil_r, frc)
    rsprak = rs_transl(text_r)
    text_sav(fil_r, fil_n, rsprak, prefix)

    return rsprak

fil_r = 'german.txt'

rovare(fil_r,'', frc = 0.99)

#felhantering
#path fel
#filtyp fel
#hantering av tecken eller nummer som inte ingår i alfabetet
#kolla om sparfil finns och är ok att skriva över eller skapa ny

#".,!:; " undantag från felrapport