def check_txt2(fil_r, r_encode, w_encode):
    
    txt_r = ""

    with open(fil_r, 'r', encoding = r_encode) as f:
        for i in f:
            i = i.replace('\t', '')
            i = i.replace('\n', '')
            txt_r = txt_r + i + '\n'

    fil_s = fil_r + f'F-{r_encode}'
    comment = f'Filen lästes som {r_encode}, '
    print(f'Filen lästes som {r_encode}')

    fil_s = fil_s + f'-T-{w_encode}.txt'
    comment = comment +  f' Filen sparades som {w_encode}'
    print(f'Filen sparades som {w_encode}')

    with open(fil_s, 'w', encoding = w_encode) as sav:
        sav.write(comment+'\n')
        sav.write(txt_r)

    print(fil_s)

    return fil_s


    #    r_encode = 'UTF-8'
    #    w_encode = 'cp1252'

fil_s = check_txt2('svenskt_text.txt', 'cp1252', 'cp1252')
fil_s1 = check_txt2(fil_s, 'cp1252', 'cp1252')
