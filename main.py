import maps
import tkinter as tk
from PIL import Image as img, ImageTk as TkImage

class Image:
    def __init__(self, path:str, nom:str) -> None:
        self.image = img.open(path)
        self.tkimage = TkImage.PhotoImage(self.image)
        self.nomimage = nom

class Fenetre:
    def __init__(self) -> None:
        self.fenetre = tk.Tk()
        self.fenetre.lift()


def start(fen:tk.Tk, choixsoft:tk.StringVar):
    choix = choixsoft.get()
    if choix == "Tarkovmap":
        fen.destroy()
        maps.mainprog()




def mainprog() -> None:
    root = Fenetre()
    fen = root.fenetre
    fen.geometry("500x500")
    choixsoft = tk.StringVar()
    drop = tk.OptionMenu(fen , choixsoft, *["Tarkovmap","Tamere", "Missié salam"])
    drop.pack()
    button = tk.Button( fen, text = "Valider" , command = lambda : start(fen, choixsoft))
    button.pack()
    fen.mainloop()



if __name__ == "__main__":
    mainprog()