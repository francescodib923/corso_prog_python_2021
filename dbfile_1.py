import json
from pyfiglet import Figlet
while True:
    
    def main_screen():
        f = Figlet(font='slant')
        print (f.renderText ("FAN GHOUL"))

    def save_data(dt):
        fp= open ("elenco.dat","w")
        fp.write (json.dumps(dt))
        fp.close()

    def read_data():
        fp = open ("elenco.dat","r")
        dati_agenda = fp.read()
        fp.close()
        return json.loads (dati_agenda)

    def clear_dbfile():
        fp = open ("elenco.dat", "w")
        fp.write ("[()]")
        fp.close

    def modifica ():
        pass

    def cancella ():
        lst = stampa()
        id_del = input ("inserisci ID da cancellare: ")
        del (lst[id_del])

    def inserisci():
        ana = {}
        ana ["Nome"] = input ("Nome: ")
        ana ["Cognome"] = input ("Cognome: ")
        ana ["Email"] = input ("Email: ")
        ana ["Tel"] = input ("Tel: ")
        lista = read_data()
        return lista
        

    def stampa():
        lista = read_data()
        print (lista)


    #menu

    def main_menu():
        main_screen()
        print ("\n")
        print ("1. Inserisci")
        print ("2. Stampa")
        print ("3. Modifica")
        print ("4. Purge DB")
        print ("99. Esci")


    print (main_menu())

    cmd = input ("#: ")
    if (cmd == "99"):
        exit()
    elif (cmd =="1"):
        inserisci()
    elif (cmd =="2"):
        stampa()
    elif (cmd =="4"):
        clear_dbfile()
    
    

    else:
        print ("comando inserito:" + cmd)
        
