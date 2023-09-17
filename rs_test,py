from rovarsprak import rovare

fil_r = input('Ange en text fil: ')
#prefix = input('Ange prefix eller använd default ("enc_rs_"  = enter) för krypterad fil: ')
frc = input('Ange hur noga icke svenska bokstäver granskas 0.00 - 1.00, default (0.50 = enter): ')

#rsprak = rovare(fil_r, prefix, frc)

rsprak = rovare(fil_r, frc)

val = input('\nVill du granska den krypterade texten på skärmen: Ja (J) eller N (enter):')
if val == "J" or val == "j":
    print('\n___Resultat av Text krypterad till Rövarspråk___\n'+rsprak)

else:
    exit()