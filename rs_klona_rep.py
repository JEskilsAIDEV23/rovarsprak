from git import Repo
import os
from rovarsprak import rovare

#Funktion för att klona ett Git-repository, och kryptera dess text filer
# till rövarspråk.
#En Nackdel med att klona Git-repositoriet är att det sedan ifall det inte behövs 
# enklast tas bort manuellt med filhanteraren då konfigurationen för Git-repository 
# ligger i en dold underkatalog. 
# Fordelen är att en stor mängd text-filer kan krypteras på en gång. 
# För att underlätta borttagning av Git-Repositoriet läggs det i en tmp mapp, '/tmp/repo'
# Textfilerna läses direkt från tmp_repo men sparas i en separat mapp '/tmp/krypterat' utanför 
# repositoriet.


def klona_remote_git(repo_url):

    try: 
        Repo.clone_from(repo_url, "/tmp/repo")  # klonar remote repository till lokal mapp
    
    except:
        print('Ett lokalt Repository "/tmp/repo" existerar och skrivs över:')

    try:
        os.mkdir('/tmp/krypterat') #skapar lokal mapp för krypterade filer

    except: 
        print('Lokal mapp "/tmp/krypterat" för de krypterade filerna finns redan') 


#repo_url = 'https://github.com/AIDEV23S/svText'
#klona_remote_git(repo_url)

# Funktionen RS_Git_txt() skapar en lista över filerna i '/tmp/repo' och filtrerar och krypterar de filer 
# som har filändelsen .txt
# Ifall användaren vill gå igenom filerna så skapas en textfil 'lista_text_filer.csv' i svenskt csv-format
#  med ';' som separator mellan de okrypterade och krypterade filerna angivna med path och filnamn i mappen 
# '/tmp/kryptering'. Lämplgt Ifall användaren vill köra enstaka filer i UI.
# För namngivning av utdata filen då krypteringen sker från repository och troligtvis i batcher namnges varje 
# fil med ett prefix RS_#_ före filnamnet där # är ett nummer.
# För att minimera risken för granskningsstopp så körs kryptering i batcher med default inställningar och frc = 0.

def RS_Git_txt():

    path_s = 'c:\\tmp\\krypterat\\'

    with open(path_s+'lista_text_filer.csv', 'w', encoding = 'utf-8') as sav:

        file_list = os.listdir("/tmp/repo")

        n = 0

        for i in file_list:
            if '.txt' in i:
                sav.write('c:\\tmp\\repo\\'+i+';'+path_s+'RS_'+str(n)+'_'+i+'\n')
                rovare('c:\\tmp\\repo\\'+i, path_s+'RS_'+str(n)+'_'+i, encode = 'utf-8', frc = 0)
                n +=1

