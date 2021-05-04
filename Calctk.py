#kalkulator tkinter
#Mau ngapain? recode yak? yahahah buta program
#H-Nut 2021

import sys,os

def versi():
    if sys.version_info.major != 3:
       print("[!] Tools hanya untuk python versi 3\n[!] Untuk python versi 2 tidak di dukung")
       sys.exit(0)  

versi()
       
try:
    from tkinter import Tk, Label, Button, Entry
except ModuleNotFoundError:
    print()
    print("[!] Install Module ny dulu\n[!] Ketik : pip install tkinter")
    print()
    sys.exit(0)
    
class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title_label = Label(self, text="Kalkulator Tkinker\nCoded by H-Nut", bg = "gray")
        self.config(bg = "gray")
        self.title_label.pack()
        self.entry = Entry(self)
        self.entry.pack()
        self.entry.insert(0, "1+2")
        self.label = Label(self, text="",bg = "gray")
        self.label.pack()
        self.button = Button(self, text="Hasil",bg = "green", command=self.onclick)
        self.button.pack()

    def onclick(self):
        self.label.configure(text=str(eval(self.entry.get())))


root = Root()

if __name__ == '__main__':
     root.mainloop()
