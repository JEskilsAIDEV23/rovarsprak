from check import check_encode

fil_r = input('Läs fil: ')
encode = check_encode(fil_r)
txt_r = ""
if encode == 'cp1252':
 #   enc = 'UTF-8'
    enc = encode

with open(fil_r, 'r', encoding = enc) as f:
    for i in f:
        i = i.replace('\t', '')
        i = i.replace('\n', '')
        txt_r = txt_r + i + '\n'

    fil_s = fil_r + ' (from ' +str(enc)+ ' to UTF-8).txt'

    comment = f'Filen lästes som {enc}\n'

    print(f'Filen lästes som {enc}')

with open(fil_s, 'w', encoding = 'UTF-8') as sav:
    sav.write(comment+'\n')
    sav.write(txt_r)