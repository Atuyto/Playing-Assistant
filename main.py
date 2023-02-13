import maps ,items
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
        self.fenetre.geometry("500x500")
    def getroot(self) -> tk.Tk :
        return self.fenetre



def start(fen:tk.Tk, choixsoft:tk.StringVar):
    choix = choixsoft.get()

    if choix == "Tarkovmap":
        fen.destroy()
        maps.mainprog()
        
    elif choix == "TarkyItems":
        fen.destroy()
        items.mainprog()



def mainprog() -> None:
    fen = Fenetre()
    surface = fen.getroot()
    choixsoft = tk.StringVar()
    drop = tk.OptionMenu(surface , choixsoft, *["Tarkovmap","TarkyItems", "Missié salam"])
    drop.pack()
    button = tk.Button( surface, text = "Valider" , command = lambda : start(surface, choixsoft))
    button.pack()
    surface.mainloop()



if __name__ == "__main__":
    mainprog()