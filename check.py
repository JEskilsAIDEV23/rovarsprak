# check_char(text, frc = 0.5)
# Funktionen kvantifierar de tecken som ska krypteras utifrån förekomst
# i svenska alfabetet och ifall de är siffor eller andra symboler.
# Funktionen kontrollerar även att textfilen inte var tom.

def check_char(text, frc = 0.5):

    l_c = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖabcdefghijklmnopqrstuvwxyzåäö .,!?;:'"
    l_lc = '"1234567890+-/\*()%@<>'

    # l_c common: strängen innehåller de förväntat mest vanliga bokstäver och tecken funna i Svenskt text
    # l_lc less common: strängen innehåller siffror och mindre vanligt förekommande tecken i vanlig svensk text
    # l_un uncommon strängen har inte definierats då den motsvara alla förekommande tecken som inte omfattas av l_c och l_lc 
    #  i utf-8 
    # Ett default värde på 50% eller ett eget värde av textens innehåll av svenska bokstäver kan sättas som filter för bevakning

    txt = text.replace('\n', '') #texten rensas på radbrytning 
    txt = txt.replace('\t', '') #texten rensas på eventuella tabbar 

    #antalet tecken som kvarstår beräknas som fraktioner av common, less common och uncommon

    n_un = 0
    n_c = 0
    n_lc = 0

    for i in txt:
        if i not in l_c and i not in l_lc:
            n_un += 1
        if i in l_lc:
            n_lc += 1
        if i in l_c:
            n_c += 1
    
    n_sum = n_un + n_lc + n_c #summan av alla tecken

    if len(txt) == 0: #Ifall en tom text fil läses in ges ett felmeddelande och programmet avslutas

        print('VARNING! Input filen innehåller inga tecken!')
        print('Kontrollera ifall du angett en korrekt text-fil')
        print('Programmet avslutas')
        return False

    if len(txt) == n_sum: #kontroll att textlängd motsvarar antal tecken

        #kontroll av antal tecken, dess relativa andel och ifall det är övervägande icke svenska bokstäver vilket ger en varning till
        # användaren med ett val att kunna avbryta krypteringen.  

        if n_un/n_sum > n_c/n_sum or n_lc/n_sum > n_c/n_sum or n_c/n_sum < frc:

            print('VARNING! Input filen innehåller flertalet siffror och ovanliga tecken förutom svenska bokstäver')
            print('Kontrollera ifall du angett en korrekt text-fil\n')
            print(f'character fractions: \nuncommon {n_un} ({n_un/n_sum:.3}) \nless common {n_lc} ({n_lc/n_sum:.3}) \ncommon {n_c} ({n_c/n_sum:.3})')
            val = input('\nKrypteringen till rövarspråk kommer inte vara fullständig, J (fortsätt), Avsluta (enter)')

            if val == "J" or val == "j":
                return True
            else:
                return False
    else:

        print('Exception')
        return False
            
    return True

# check_path(file)
# kontrollerar ifal en fil finns redan i katalogen

def check_path(file):
    import os.path
    check_file = os.path.isfile(file)
    return check_file
   
# check_encode(fil_r)
# kontrollerar hur texten i filen är kodad
# Mac rapporterar cp1252 som UTF-8 och Windows rapporterar UTF-8 som cp1252 oavsett kodning.

def check_encode(fil_r):

    with open(fil_r,'r') as f:
        encode = f.encoding
        print(f'inläst fil av typen {encode}')
    return encode

# encode = check_fil_r(fil_r)
# provläser inputfilen för att spåra möjliga UnicodeDecodeErrors som beror på skillnad mellan UTF-8 (Mac/Linux)
# och cp1252 (Windows). Mac rapporterar cp1252 som UTF-8 och Windows rapporterar UTF-8 som cp1252 med funktionen 
# check_encode(). För att undvika programkrash så justeras encoding parametern omvänt till utf-8 respektive cp1252 ifall 
# fel upptäcks vid inläsning av antingen en UTF-8 eller cp1252 kodad fil. 
# Ifall filen är kodad i något annat format och inte kunnat läsas som UTF-8 eller cp1252 så erbjuds ett 
# försök att läsa filen med en valfri teckentabell. 
# __________________
# encode, som ges av funktionen används för att läsa in textfilen med rätt avkodning programmet körs på Mac eller PC

def check_fil_r(fil_r):

    encode = check_encode(fil_r)
    txt = ""

    # funnet att Windows ger cp1252 för UTF-8 och Mac ger UTF-8 för cp1252 oavsett filen som läses är 
    # utf-8 eller cp1252.  

    try: 
        with open(fil_r, 'r', encoding = encode) as f:
            for i in f:
                txt = txt + i
        return encode
        
    except UnicodeDecodeError:
        print(f'{fil_r} är inte formaterad som {encode}')

        #ifall tecken fel upptäcks, försök på nytt med omvänd avkodningstyp

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
            print('Programmet avslutas')
            exit()

        # ifall fel kvarstår med att läsa filen, ges ett försök att läsa filen med en 
        # annan kodtabell än UTF-8 eller cp1252

        #    encode_my = input('Ange en möjlig teckentabell eller avsluta programmet (enter): ')
        #    if encode_my == "":
        #        exit()
        #    else:
        #        try:
        #            print(f'Försöker läsa filen {fil_r} som {encode_my}')
         #           with open(fil_r, 'r', encoding = encode_my) as f:
         #               for i in f:
         #                   txt = txt + i                  
         #           encode = encode_my
          #          return encode
                    
          #      except UnicodeDecodeError:
          #          print(f'{fil_r} är inte heller formaterad som vald {encode_my}')
           #         print('Programmet avslutas')
           #         exit()

# check_param(frc) 
# kontrollerar att angivet värde för frc är 0 - 1, och omvandlar till float

def check_param(frc):

    try:
        frc = float(frc)
        if frc > 1.0:
            frc = 1.0 # positiva värden över 1 sätts till 1
        if frc < 0:
            frc = 0 # negativa värden sätts till 0
        else:
            frc = frc
    except:
        frc = 0.50 # inget angivet värde eller felaktigt tecken ex. bokstav sätt default frc = 0.50

    print(f'\nfrc = {frc}')
    return frc

# check_save_file(fil_s)
# Kontrollerar ifall sparfilen redan existerar och ger möjlighet att skriva över befintlig fil
# namnge en ny fil som sparfil. Ifall ett nytt namn ges till sparfilen och en sådan fil existerar 
# kommer programmet ge en varning och spara filen med namnet Exception_ som ett prefix före det nya 
# filnamnet, för att på så sätt skydda överskrivning av en befintlig fil. Väljer man att i första 
# steget skriva över en befintlig fil genom att trycka enter skrivs filen över.  


def check_save_file(fil_s):

    if check_path(fil_s) == False: #Fil existerar inte
        return fil_s

    if check_path(fil_s) == True: #Fil existerar
        print(f'\nEn fil med namnet {fil_s} finns redan!')
        fil_ns = input('Ange ett nytt filnamn eller skriv över befintlig fil genom att trycka enter: ')

        if fil_ns == "": #OK att skriva över då enter angivet
            fil_s = fil_s

        if fil_ns != "":
            if check_path(fil_ns) == True: #det nya filnamnet som angavs existerar
                print(f'\nEn fil med namnet {fil_ns} finns redan!')
                fil_s = 'Exception_'+fil_ns #ange Exception_ prefix
                print('Exception prefix tillagt för att skydda en befintlig fil')
                return fil_s
            else:
                fil_s = fil_ns #det nya filnamnet som angavs existerar inte
            
        return fil_s
    
    return fil_s

