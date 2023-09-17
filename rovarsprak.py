

#______Main______


def rovare(fil_r, prefix = "rs_", frc = 0.5):

 #   check_encode('rovarsprak_svenskt_text.txt')
    text_r, fil_r, fil_n = text_imp(fil_r, frc)
    rsprak = rs_transl(text_r)
    text_sav(fil_r, fil_n, rsprak, prefix)

    return rsprak

fil_r = 'texter.txt'

rovare(fil_r,'rs_', frc = 1)

#felhantering
#path fel
#filtyp fel
#hantering av tecken eller nummer som inte ingår i alfabetet
#kolla om sparfil finns och är ok att skriva över eller skapa ny

#".,!:; " undantag från felrapport