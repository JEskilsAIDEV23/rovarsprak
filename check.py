def check_char(text, frc = 0.5):

    l_c = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖabcdefghijklmnopqrstuvwxyzåäö .,!?;:'"
    l_lc = '"1234567890+-/\*()%@'

    # l_c common: strängen innehåller de förväntat mest vanliga bokstäver och tecken funna i Svenskt text
    # l_lc less common: strängen innehåller siffror och mindre vanligt förekommande tecken i vanlig svensk text
    # l_un uncommon strängen har inte definierats då den motsvara alla förekommande tecken som inte omfattas av l_c och l_lc 
    #  i utf-8 
    # Ett default värde 50% eller valt värde som anger att texten innehåller minst 50% svenska bokstäver kan sättas  

    txt = text.replace('\n', '') #texten rensas på radbrytning 
    txt = txt.replace('\t', '') #texten rensas på eventuella tabbar 

    #antalet tecken som kvarstår beräknas som fraktioner av common, less common och uncommon

    n_un = 0
    n_c = 0
    n_lc = 0

    for i in txt:
        if i not in l_c and i not in l_lc:
            n_un += 1
         #   print(f'{i}')
        if i in l_lc:
            n_lc += 1
        if i in l_c:
            n_c += 1
    
    n_sum = n_un + n_lc + n_c

    if len(txt) == 0: #Ifall en tom text fil läses in ges ett felmeddelande och programmet avslutas

        print('VARNING! Input filen innehåller inga tecken!')
        print('Kontrollera ifall du angett en korrekt text-fil')
        print('Programmet avslutas')
        return False

    if len(txt) == n_sum: #kontroll att textlängd motsvarar antal tecken

        #kontroll av antal tecken, dess relativa andel och ifall det är övervägande icke svenska bokstäver ges en varning till
        # användaren med ett val att avbryta krypteringen.  

        if n_un/n_sum > n_c/n_sum or n_lc/n_sum > n_c/n_sum or n_c/n_sum < frc:

            print('VARNING! Input filen innehåller flertalet siffror och ovanliga tecken förutom svenska bokstäver')
            print('Kontrollera ifall du angett en korrekt text-fil\n')
            print(f'character fractions: \nuncommon {n_un} ({n_un/n_sum:.3}) \nless common {n_lc} ({n_lc/n_sum:.3}) \ncommon {n_c} ({n_c/n_sum:.3})')
            val = input('\nKrypteringen till rövarspråk kommer inte vara fullständig, J (fortsätt) avsluta (enter)')

            if val == "J" or val == "j":
                return True
            else:
                return False
            
    return True


def check_path(file):

    import os.path
    path = file
    check_file = os.path.isfile(path)
    return check_file


def read_new_file():

    fil_r = input('Ange en ny path+fil? eller avsluta programmet med enbart enter: ')

    if fil_r == "":
        print('Programmet avslutas!')
        exit()
    else:
        return fil_r


def save_new_file(fil_s):

    print(f'\nEn fil med namnet {fil_s} finns redan!')

    fil_ns = input('Ange ett nytt filnamn eller skriv över filen med att trycka enter: ')

    if fil_ns == "":

        fil_ns = fil_s
            
    return fil_ns


def check_encode(fil_s):

    with open(fil_s,'r') as f:
        encode = f.encoding
        print(f'inläst fil av typen {encode}')
    return encode




    
