from check import check_char
from check import check_path
from check import read_new_file
from check import save_new_file


def text_imp(fil_r, frc = 0.5):

    text_r = ""
    fil_n = ""

    if check_path(fil_r) == False:  
        print("Angiven fil kan inte hittas")

        fil_n = read_new_file()
        text_r, fil_r, fil_n = text_imp(fil_n, frc)

        return text_r, fil_r, fil_n
    
    if check_path(fil_r) == True:
        with open(fil_r, 'r', encoding = 'utf-8') as f:

            for i in f:
                text_r = text_r + i
            
            if (check_char(text_r, frc)) == True:
                return text_r, fil_r, fil_n
                
            else:
                exit()
        
    return text_r, fil_r, fil_n

def rs_transl(text):

    konsonanter = 'bdfghjklmnpqrstvxzBDFGHJKLMNPQRSTVXZ'
    s2 = ""

    for i in text:
        s2 = s2 + i
        if i in konsonanter:
            s2 = s2 + "o" + i.lower()

    return s2


def text_sav(fil_r, fil_n, rsprak, prefix = 'rs_'):

    if fil_n == "":
        fil_s = prefix+fil_r
        if check_path(fil_s) == True:
            fil_s = save_new_file(fil_s)

    else:
        fil_s = prefix+fil_n
        if check_path(fil_s) == True:
            fil_s = save_new_file(fil_s)

    with open(fil_s, 'w', encoding = 'utf-8') as sav:
        
        sav.write(rsprak)

    return print(f"Fil sparad som {fil_s}")