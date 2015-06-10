from tkinter import *
#Stanja
NEVTRALNO = 0
KODIRANJE = 1
DEKODIRANJE = 2
ODPRTO = 3
ZAPRTO = 4
#sestavni deli

kolo1 = ['U', 'Č', 'Ž', 'M', 'Y', 'P', 'N', 'O', 'G', 'A', 'X', 'C', 'K',
 'Š', ' ', 'H', 'R', 'I', 'T', 'Z', 'W', 'J', 'L', 'D', 'S', 'F', 'E', 'Q', 'B', 'V']

kolo2 = ['Č', 'K', 'Ž', ' ', 'X', 'A', 'Z', 'W', 'J', 'S', 'V', 'E', 'M',
 'D', 'I', 'L', 'B', 'T', 'O', 'H', 'Y', 'G', 'Q', 'N', 'C', 'P', 'F', 'R', 'Š', 'U']

kolo3 = ['L', 'P', 'Š', 'Q', 'B', 'G', 'N', 'A', 'W', 'I', 'U', 'Y', 'T',
 'X', 'J', 'D', 'K', 'R', ' ', 'H', 'Ž', 'F', 'V', 'Z', 'S', 'M', 'E', 'Č', 'O', 'C']

slovar = {"A":0,"B":1,"C":2,"Č":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,
          "J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"R":17,"S":18,
          "Š":19,"T":20,"U":21,"V":22,"Z":23,"Ž":24," ":25,"X":26,"Y":27,
          "W":28,"Q":29,0:"A",1:"B",2:"C",3:"Č",4:"D",5:"E",6:"F",7:"G",
          8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"R",
          18:"S",19:"Š",20:"T",21:"U",22:"V",23:"Z",24:"Ž",25:" ",26:"X",
          27:"Y",28:"W",29:"Q"}

class Stevec():

    def __init__(self, master):
        '''V okno master postavi dva gumba in števec.'''
        
        # Stanje števca je na začetku 0
        self.stevec = 1
        self.stevec1 = 1
        self.stevec2 = 1

        self.stanje = NEVTRALNO
        self.odprto = ZAPRTO

        self.kolo1 = kolo1
        self.kolo2 = kolo2
        self.kolo3 = kolo3

        self.niz = ""
        self.dekodirano = ""
        self.kodirano =""
        self.ime = ""
        self.koda=""
        self.nov_niz=""
        self.tekst=""
        self.koda =""

        # Glavni menu
        menu = Menu(master)
        master.config(menu=menu) # Dodamo menu
        # Naredimo podmenu "File"
        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        # Dodamo izbire v file_menu
        file_menu.add_command(label="Odpri", command=self.odpri)
        file_menu.add_separator() # To doda separator v menu
        file_menu.add_command(label="Izhod", command=master.destroy)

        #prvo kolo gumbi
        gumb_povecaj = Button(master, text=" +1 ", command=self.povecaj)
        gumb_povecaj.grid(row=1, column=1)

        gumb_zmanjsaj = Button(master, text=" -1 ", command=self.zmanjsaj)
        gumb_zmanjsaj.grid(row=1, column=0)

        self.napis_stevec = StringVar(value=str(self.stevec))
        label_stevec = Label(master, textvariable=self.napis_stevec)
        label_stevec.grid(row=2, column=0, columnspan = 2)

        self.ime_stevec = StringVar(value="prvo kolo")
        label_ime_stevec = Label(master, textvariable=self.ime_stevec)
        label_ime_stevec.grid(row=0, column=0, columnspan = 2)

        

        #drugo kolo gumbi

        gumb_povecaj1 = Button(master, text=" +1 ", command=self.povecaj1)
        gumb_povecaj1.grid(row=4, column=1)

        gumb_zmanjsaj1 = Button(master, text=" -1 ", command=self.zmanjsaj1)
        gumb_zmanjsaj1.grid(row=4, column=0)

        self.napis_stevec1 = StringVar(value=str(self.stevec1))
        label_stevec1 = Label(master, textvariable=self.napis_stevec1)
        label_stevec1.grid(row=5, column=0, columnspan = 2)

        self.ime_stevec1 = StringVar(value="drugo kolo")
        label_ime_stevec1 = Label(master, textvariable=self.ime_stevec1)
        label_ime_stevec1.grid(row=3, column=0, columnspan = 2)

        #tretje kolo gumbi

        gumb_povecaj2 = Button(master, text=" +1 ", command=self.povecaj2)
        gumb_povecaj2.grid(row=7, column=1)

        gumb_zmanjsaj2 = Button(master, text=" -1 ", command=self.zmanjsaj2)
        gumb_zmanjsaj2.grid(row=7, column=0)

        self.napis_stevec2 = StringVar(value=str(self.stevec2))
        label_stevec2 = Label(master, textvariable=self.napis_stevec2)
        label_stevec2.grid(row=8, column=0 ,columnspan = 2)

        self.ime_stevec2 = StringVar(value="tretje kolo")
        label_ime_stevec2 = Label(master, textvariable=self.ime_stevec2)
        label_ime_stevec2.grid(row=6, column=0, columnspan =2)

        #gumba za kodiranje in dekodiranje

        gumb_kodiraj = Radiobutton(master, text = "kodiraj", value=2,indicatoron = 0,command = self.kodiraj_stanje)
        gumb_kodiraj.grid(row = 9, column=2)

        gumb_dekodiraj= Radiobutton(master, text = "dekodiraj", value=3, indicatoron = 0,command = self.dekodiraj_stanje)
        gumb_dekodiraj.grid(row=9, column =3)

        gumb_pozeni = Button(master, text="Pozeni", command = self.pozeni)
        gumb_pozeni.grid(row = 10, column = 2, columnspan=2)

        #gumb za odpriranje datoteke
        
        gumb_odpri = Button(master,text="odpri datoteko",command=self.odpri)
        gumb_odpri.grid(row=11,column=2,columnspan=4)
        
        self.pot = StringVar(master,value= "Tukaj se izpise pot")
        pot_datoteke = Label(master, textvariable = self.pot)
        pot_datoteke.grid(row = 12, column = 2, columnspan = 4)

        ##slikca

        canvas = Canvas(master)
        canvas.grid(row = 9,rowspan = 3, column = 0,columnspan=2)

        self.photo = PhotoImage(file = 'exploded.gif')

        canvas.create_image(150,130, image=self.photo)

        #Textwidget v katerem se izpise text v datoteki
        niz = self.tekst
        self.text_insert= Text(root,height=9,width=30)
        self.text_insert.insert(END, niz)
        self.text_insert.grid(row=1,rowspan=9,column=2)

        label_napis_dat = Label(master, text="Besedilo v datoteki")
        label_napis_dat.grid(row=0, column=2)

        niz1 = self.koda
        self.text_out = Text(root,height=9,width=30)
        self.text_out.insert(END, niz)
        self.text_out.grid(row=1,rowspan=9,column=3)

        label_napis_izh = Label(master, text="Besedilo, ki bo v izhodni datoteki")
        label_napis_izh.grid(row=0, column=3)

      

###############################################################################
    def pozeni(self):#funkcija zazene proces kodiranja
        if self.stanje == KODIRANJE and self.odprto == ODPRTO:
            return self.kodiraj(self.niz,self.stevec,self.stevec1,self.stevec2)
        elif self.stanje == DEKODIRANJE and self.odprto == ODPRTO:
            return self.dekodiraj(self.niz,self.stevec,self.stevec1,self.stevec2)
        
###############################################################################
    #funkcije za premik koles
    def povecaj(self):
        '''Povečaj števec za 1.'''
        self.stevec = self.stevec + 1
        self.napis_stevec.set(str(self.stevec))


    def zmanjsaj(self):
        '''Zmanjšaj števec za 1.'''
        self.stevec = self.stevec - 1
        self.napis_stevec.set(str(self.stevec))

    def povecaj1(self):
        '''Povečaj števec za 1.'''
        self.stevec1 = self.stevec1 + 1
        self.napis_stevec1.set(str(self.stevec1))


    def zmanjsaj1(self):
        '''Zmanjšaj števec za 1.'''
        self.stevec1 = self.stevec1 - 1
        self.napis_stevec1.set(str(self.stevec1))

    def povecaj2(self):
        '''Povečaj števec za 1.'''
        self.stevec2 = self.stevec2 + 1
        self.napis_stevec2.set(str(self.stevec2))


    def zmanjsaj2(self):
        '''Zmanjšaj števec za 1.'''
        self.stevec2 = self.stevec2 - 1
        self.napis_stevec2.set(str(self.stevec2))
######################################################################

    def kodiraj_stanje(self):
        self.stanje = KODIRANJE
        print("KODIRANJE")

    def dekodiraj_stanje(self):
        self.stanje = DEKODIRANJE
        print("DEKODIRANJE")
        
    def rotacija_v_desno(self,sez, x):#premakne seznam za x mest v desno
        x = abs(x) % 30
        sez = sez[-x:] + sez[:-x]
        return sez
    
    def kodiraj(self,niz, rot_kolo1, rot_kolo2, rot_kolo3):
        
        self.kolo1 = kolo1 #resetria kolesa na osnovne nastavitve
        self.kolo2 = kolo2
        self.kolo3 = kolo3

        self.niz = ""   #zbriše vse nize
        self.dekodirano = ""
        self.kodirano =""
        
        self.kolo1 = self.rotacija_v_desno(self.kolo1, rot_kolo1)
        self.kolo2 = self.rotacija_v_desno(self.kolo2, rot_kolo2)
        self.kolo3 = self.rotacija_v_desno(self.kolo3, rot_kolo3)
        niz = niz.upper()
        stevec_kolo1 = 0
        stevec_kolo2 = 0
        stevec_kolo3 = 0
        
        for crka in niz:
             indeks = slovar[crka]
             crka = self.kolo1[indeks]
             self.kolo1 = self.rotacija_v_desno(self.kolo1,1) # kolo se zavrti za ena v desno
             # po vsaki crki
             stevec_kolo1 += 1
             
             #dugo kolo

             indeks2 = slovar[crka]
             crka = self.kolo2[indeks2]
             if stevec_kolo1 % 30 == 0:
                 self.kolo2 = self.rotacija_v_desno(self.kolo2, 1)
                 stevec_kolo2 += 1
             #kolo se zavrti ko prvo kolo naredi poln obrat


             #tretje kolo
             
             indeks3 = slovar[crka]
             crka = self.kolo3[indeks3]
             self.kodirano = self.kodirano + crka
             #kolo se zavrti ko drugo kolo naredi poln obrat
             if (stevec_kolo2 % 30) == 0 and (stevec_kolo1 % 30) == 0:
                 self.kolo3 = self.rotacija_v_desno(self.kolo3, 1)
                 stevec_kolo3 += 1
                 
        niz2 = self.kodirano
        self.text_out.delete(1.0,END)
        self.text_out.insert("1.0",niz2)
        return self.shrani()
    def dekodiraj(self,niz, rot_kolo1, rot_kolo2, rot_kolo3):

        self.kolo1 = kolo1
        self.kolo2 = kolo2
        self.kolo3 = kolo3

        self.niz = ""
        self.dekodirano = ""
        self.kodirano =""
        
        self.kolo1 = self.rotacija_v_desno(self.kolo1, rot_kolo1)
        self.kolo2 = self.rotacija_v_desno(self.kolo2, rot_kolo2)
        self.kolo3 = self.rotacija_v_desno(self.kolo3, rot_kolo3)
        niz = niz.upper()
        stevec_kolo1 = 0
        stevec_kolo2 = 0
        stevec_kolo3 = 0

        for crka in niz:
            if stevec_kolo2 > 0 and(stevec_kolo2 % 30) == 0 and (stevec_kolo1 % 30) == 0 and stevec_kolo1 > 0:
                 self.kolo3 = self.rotacija_v_desno(self.kolo3, 1)
                 stevec_kolo3 += 1
            indeks = self.kolo3.index(crka)
            crka = slovar[indeks]

            #drugo kolo

            if (stevec_kolo1 % 30) == 0 and stevec_kolo1 > 0:
                 self.kolo2 = self.rotacija_v_desno(self.kolo2, 1)
                 stevec_kolo2 += 1
            indeks = self.kolo2.index(crka)
            crka = slovar[indeks]
            
            #kolo1

            indeks = self.kolo1.index(crka)
            crka = slovar[indeks]
            self.kolo1 = self.rotacija_v_desno(self.kolo1,1)
            stevec_kolo1 += 1

            self.dekodirano = self.dekodirano + crka
            
        niz1= self.dekodirano
        self.text_out.delete(1.0,END)
        self.text_out.insert("1.0",niz1)
        return self.shrani()

    def odpri(self):
        self.ime =""
        self.ime = filedialog.askopenfilename()
        self.niz = ""
        if self.ime == "": # Pritisnili smo Cancel
            return

        with open(self.ime, encoding="cp1250") as f:
            self.odprto = ODPRTO
            for vrstica in f:
                self.niz = self.niz + vrstica.strip()
        self.pot.set(self.ime)
        self.text_insert.delete(1.0,END)
        niz = self.nova_vrsta(self.niz)
        self.text_insert.insert("1.0",niz)

    def shrani(self):
        self.ime =""
        if self.stanje == DEKODIRANJE:
            self.ime = filedialog.asksaveasfilename()
            if self.ime == "": # Pritisnili smo Cancel
                return

            with open(self.ime, "wt", encoding="cp1250") as f:
                    print(self.dekodirano, file = f)
        else:
            self.ime = filedialog.asksaveasfilename()
            if self.ime == "": # Pritisnili smo Cancel
                return

            with open(self.ime, "wt", encoding="cp1250") as f:
                    print(self.kodirano, file = f)

    def nova_vrsta(self,niz):
        counter = 0
        self.nov_niz = ""
        for znak in niz:
            self.nov_niz = self.nov_niz + znak
            counter += 1
            if counter >= 30 and znak == " ":
                self.nov_niz = self.nov_niz +"\n"
                counter = 0
        return self.nov_niz
                
        
            
        



# Naredimo glavno okno
root = Tk()
root.wm_title("enigma")
aplikacija = Stevec(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
