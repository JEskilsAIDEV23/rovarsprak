def check_txt2(fil_r, r_encode, w_encode):
    
    txt_r = ""

    with open(fil_r, 'r', encoding = r_encode) as f:
        for i in f:
            i = i.replace('\t', '')
            i = i.replace('\n', '')
            txt_r = txt_r + i + '\n'

    fil_s = fil_r + ' (from ' +str(r_encode) 
    comment = f'Filen lästes som {r_encode}, '
    print(f'Filen lästes som {r_encode}')

    fil_s = fil_s + f' to {w_encode}).txt'
    comment = comment +  f' Filen sparades som {w_encode}'
    print(f'Filen sparades som {w_encode}')

    with open(fil_s, 'w', encoding = w_encode) as sav:
        sav.write(comment+'\n')
        sav.write(txt_r)


    #    r_encode = 'UTF-8'
    #    w_encode = 'cp1252'

#check_txt2('svenskt_text.txt', 'UTF-8', 'cp1252')
#check_txt2('svenskt_text.txt', 'cp1252', 'UTF-8')

check_txt2('svenskt_text.txt (from UTF-8 to cp1252).txt', 'cp1252', 'UTF-8')
check_txt2('svenskt_text.txt (from cp1252 to UTF-8).txt', 'UTF-8', 'cp1252')

