from check import check_encode

fil_r = input('Läs fil: ')
encode = check_encode(fil_r)
txt_r = ""

try: 
    with open(fil_r, 'r', encoding = encode) as f:
        for i in f:
            i = i.replace('\t', '')
            i = i.replace('\n', '')
            txt_r = txt_r + i + '\n'

    fil_s = fil_r + ' (from ' +str(encode)+ ' to UTF-8).txt'

    comment = f'Exception Filen lästes som {encode}\n'

    print(f'Exception Filen lästes som {encode}')


except UnicodeDecodeError:
    with open(fil_r, 'r', encoding = "UTF-8") as f:
        for i in f:
            i = i.replace('\t', '')
            i = i.replace('\n', '')
            txt_r = txt_r + i + '\n'

    fil_s = fil_r + ' (from ' +str(encode)+' exception used UTF-8'+ ' to UTF-8).txt'

    comment = f'Exception Filen detekteras som {encode} men lästes in som UTF-8\n'

    print(f'Exception Filen detekteras som {encode} men läses som UTF-8')

with open(fil_s, 'w', encoding = 'UTF-8') as sav:
    sav.write(comment+'\n')
    sav.write(txt_r)