from check import check_encode

fil_r = input('Läs fil: ')
encode = check_encode(fil_r)
txt_r = ""
with open(fil_r, 'r', encoding = encode) as f:
    for i in f:
        i = i.replace('\t', '')
        i = i.replace('\n', '')
        txt_r = txt_r + i + '\n'

fil_s = fil_r + ' (from ' +str(encode)+ ' to UTF-8).txt'
with open(fil_s, 'w', encoding = 'UTF-8') as sav:
    sav.write(txt_r)