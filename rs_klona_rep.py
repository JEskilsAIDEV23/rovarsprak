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
# Ifall användaren vill gå igenom filerna och använda granskningsfunktionen så skapas även en 
# textfil med en lista över path och filnamn i mappen '/tmp/kryptering' ifall användaren  vill 
# använda rs_test.py UI.
# För namngivning av utdata filen då krypteringen sker från repository och troligen i batcher 
# ges varje fil ett prefix RS_#_ före filnamnet där # är ett nummer.
# För enkelhetens skull så körs kryptering i batcher med defaultinställningar.

def RS_Git_txt():

    path_s = 'c:\\tmp\\krypterat\\'

    with open(path_s+'lista_text_filer.txt', 'w', encoding = 'utf-8') as sav:

        sav.write(f'I mappen {path_s} sparas alla krypterade filer samt den här listan över\n\
                  okrypterade och krypterade filer med prefix RS_#_ där # är ett nummer.\n')

        file_list = os.listdir("/tmp/repo")

        n = 0

        for i in file_list:
            if '.txt' in i:
                sav.write('c:\\tmp\\repo\\'+i+'\t'+path_s+'RS_'+str(n)+'_'+i+'\n')
                rovare('c:\\tmp\\repo\\'+i, path_s+'RS_'+str(n)+'_'+i, encode = 'utf-8', frc = 0.1)
                n +=1

