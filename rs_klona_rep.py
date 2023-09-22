from git import Repo
import os
from rovarsprak import rovare

#Funktion för att klona ett Git-repository, och kryptera dess text filer
# till rövarspråk.
# Nackdelen är att det klonade Git-repositoriet ifall det inte sedan behövs eller ett nytt
# repo ska klonas måste tas bort manuellt i filhanteraren, då konfigurationen för Git-repository 
# ligger i en dold underkatalog. 
# Fördelen är att en stor mängd text-filer kan krypteras på en gång. 
# För att underlätta borttagning av Git-Repositoriet läggs det i en tmp mapp, '/tmp/repo'
# Textfilerna läses direkt från tmp_repo men de krypterade filerna sparas i en separat mapp '/tmp/krypterat'.
# OBS! ifall det finns ett gammalt repo och en krypterad mapp så avslutas programmet


def klona_remote_git(repo_url):

    rep_n = "/tmp/repo"
    cryp_n = '/tmp/krypterat'

    try: 
        Repo.clone_from(repo_url, rep_n)  # klonar remote repository till lokal mapp
    
    except:
        print('Ett lokalt Repository "/tmp/repo" existerar:')
        print('Ta bort det gamla lokala repositoriet eller byt namn på det')
        exit()

    try:
        os.mkdir(cryp_n) #skapar lokal mapp för krypterade filer

    except: 
        print('Lokal mapp "/tmp/krypterat" för de krypterade filerna finns redan')
        print('Ta bort den gamla lokala mappen eller byt namn på den')
        exit()

#repo_url = 'https://github.com/AIDEV23S/svText'
#klona_remote_git(repo_url)

# Funktionen RS_Git_txt() skapar en lista över filerna i '/tmp/repo' och filtrerar och krypterar de filer 
# som har filändelsen .txt
# Ifall användaren vill gå igenom filerna så skapas en textfil 'lista_text_filer.csv' i svenskt csv-format
#  med ';' som separator mellan de okrypterade och krypterade filerna angivna med path och filnamn i mappen 
# '/tmp/kryptering'. filen ger också totalt antal tecken och antalet som finns i alfabetet. 
# Lämplgt Ifall användaren vill köra enstaka filer i UI.
# För namngivning av utdata filen då krypteringen sker från repository och troligtvis i batcher namnges varje 
# fil med ett prefix RS_#_ före filnamnet där # är ett nummer.
# För att minimera risken för granskningsstopp så körs kryptering i batcher med default inställningar och frc = 0.

def RS_Git_txt():

    path_s = 'c:\\tmp\\krypterat\\'
    rep_w = 'c:\\tmp\\repo\\'


    with open(path_s+'lista_text_filer.csv', 'w', encoding = 'utf-8') as sav:

        sav.write('Source;Encrypted;In_Alphabeth;Tot Symbols\n')

        file_list = os.listdir(rep_w)

        n = 0

        for i in file_list:
            if '.txt' in i:
                rsprak, n_c, n_sum = rovare(rep_w+i, path_s+'RS_'+str(n)+'_'+i, encode = 'utf-8', frc = 0)
                sav.write(rep_w+i+';'+path_s+'RS_'+str(n)+'_'+i+';'+str(n_c)+';'+str(n_sum)+'\n')
                
                n +=1
