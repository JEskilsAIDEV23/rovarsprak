from check import check_encode

fil_r = input('Läs fil: ')
encode = check_encode(fil_r)
txt_r = ""

with open(fil_r, 'r', encoding = 'UTF') as f:
    for i in f:
        i = i.replace('\t', '')
        i = i.replace('\n', '')
        txt_r = txt_r + i + '\n'

    n = 0
    for j in txt_r:
        if n > 50 and n < 60:
            print(n, j)
        n = n+1

    fil_s = fil_r + ' (from ' +str(encode)+ ' to UTF-8).txt'

    comment = f'Filen lästes som "UTF"\n'

    print(f'Filen lästes som "UTF"')

with open(fil_s, 'w', encoding = 'UTF-8') as sav:
    sav.write(comment+'\n')
    sav.write(txt_r)