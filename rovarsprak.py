def rovare(fil_r, prefix = "enc_rs_", frc = 0.5):

    from check import check_param
    from rs_funktioner import text_imp
    from rs_funktioner import rs_transl
    from check import check_save_file
    from rs_funktioner import text_sav

 #   check_encode('rovarsprak_svenskt_text.txt')

    prefix, frc = check_param(prefix, frc)
    text_r, fil_r = text_imp(fil_r, frc)
    rsprak = rs_transl(text_r)
    fil_s = check_save_file(fil_r, prefix)
    text_sav(fil_s, rsprak)

    return rsprak

#felhantering
#path fel
#filtyp fel
#hantering av tecken eller nummer som inte ingår i alfabetet
#kolla om sparfil finns och är ok att skriva över eller skapa ny

#".,!:; " undantag från felrapport