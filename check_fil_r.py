def check_fil_r():

    from check import check_encode

    fil_r = input('Läs fil: ')
    encode = check_encode(fil_r)
    txt = ""

    try: 
        with open(fil_r, 'r', encoding = encode) as f:
            for i in f:
                txt = txt + i
        return encode
        
    except UnicodeDecodeError:
        print(f'{fil_r} är inte formaterad som {encode}')

        if encode == 'UTF-8':
            try_encode = 'cp1252'
        if encode == 'cp1252':
            try_encode = 'UTF-8'

        try:
            print(f'Försöker läsa filen {fil_r} som {try_encode}')
            with open(fil_r, 'r', encoding = try_encode) as f:
                for i in f:
                    txt = txt + i

            encode = try_encode
            return encode
            
        except UnicodeDecodeError:
            print(f'{fil_r} är inte formaterad som {try_encode}')
            encode_my = input('Ange en möjlig teckentabell eller avsluta programmet (enter): ')
            if encode_my == "":
                exit()
            else:
                try:
                    print(f'Försöker läsa filen {fil_r} som {encode_my}')
                    with open(fil_r, 'r', encoding = encode_my) as f:
                        for i in f:
                            txt = txt + i                  
                    encode = encode_my
                    return encode
                    
                except UnicodeDecodeError:
                    print(f'{fil_r} är inte heller formaterad som vald {encode_my}')
                    print('Programmet avslutas')
                    exit()

encode = check_fil_r()
print(encode)








