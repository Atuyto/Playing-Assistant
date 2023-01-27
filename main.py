import os
import tkinter as tk
from PIL import Image as img, ImageTk as TkImage
import keyboard

class Image:
    def __init__(self, path:str, nom:str) -> None:
        self.image = img.open(path)
        self.tkimage = TkImage.PhotoImage(self.image)
        self.nomimage = nom

class carrousel:
    def __init__(self, collection:list) -> None:
        self.images = {}
        for i  in range(len(collection)):
            self.images[i] = collection[i]        
        self.currentid = 0
        self.idmax = len(collection)-1

    def next(self) -> None :
        if self.currentid < self.idmax : 
            self.currentid += 1
        else:
            self.currentid = 0
    
    def previous(self) -> None :
        if self.currentid > 0:
            self.currentid -= 1
        else:
            self.currentid = self.idmax
    
    def getcurent(self) -> TkImage.PhotoImage :
        return self.images[self.currentid].tkimage

class Fenetre:
    def __init__(self) -> None:
        self.fenetre = tk.Tk()
        self.fenetre.attributes("-topmost", True)
        self.fenetre.lift()
        self.fenetre.attributes("-fullscreen", True)

def getmaplist() -> list:
    listenom:list = os.listdir("./MAP")
    listemap:list = []
    for map in listenom:
        listemap.append(Image(f"MAP/{map}", map[:-4]))
    return listemap

def loop(car:carrousel, fen:tk.Tk, label:tk.Label, curOP:float=1.0):
    touche = keyboard.read_key(False)
    nextop:float = curOP
    if touche == "droite":
        car.next()
        label.configure(image= car.getcurent())
    elif touche == "gauche":
        car.previous()
        label.configure(image= car.getcurent())
    elif touche == "haut":
        if curOP == 1.0:
            fen.attributes("-alpha", 0.0)
            nextop = 0.0
        elif curOP == 0.0:
            fen.attributes("-alpha", 1.0)
            nextop = 1.0
    elif touche == "bas":
        fen.destroy()
    fen.update()
    fen.after(200, loop, car, fen, label, nextop)


def mainprog(): 
    root = Fenetre()
    fen = root.fenetre


    lstmaps = getmaplist()
    
    car = carrousel(lstmaps)

    label = tk.Label(fen, image = car.getcurent())
    label.pack()

    fen.after(500, loop, car, fen, label)
    fen.mainloop()


if __name__ == "__main__":
    mainprog()
