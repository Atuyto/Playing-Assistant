import tkinter as tk
from PIL import Image, ImageTk
import keyboard

class ImageChanger:
    def __init__(self, fenetre ):
        self.current = 1
        # imageWood = 1
        self.imageWood = Image.open(r"MAP\wood.jpg")
        self.photoWood = ImageTk.PhotoImage(self.imageWood)

        self.imageCustoms = Image.open(r"MAP\customs.jpg")
        self.photoCustoms = ImageTk.PhotoImage(self.imageCustoms)

        self.imageFactory = Image.open(r"MAP\factory.jpg")
        self.photoFactory = ImageTk.PhotoImage(self.imageFactory)

        self.imageInterchange = Image.open(r"MAP\interchange.jpg")
        self.photoInterchange = ImageTk.PhotoImage(self.imageInterchange)
        
        self.imageLab = Image.open(r"MAP\lab.jpg")
        self.photoLab = ImageTk.PhotoImage(self.imageLab)

        self.imageShorline = Image.open(r"MAP\shorline.jpg")
        self.photoShorline = ImageTk.PhotoImage(self.imageShorline)

        self.label = tk.Label(fenetre, image = self.photoWood)
        self.label.pack()
        

    def changeImage(self, event):
        if self.current == 1:
            self.label.config(image=self.photoCustoms)
            self.current = 2
        elif self.current == 2:
            self.label.config(image=self.photoFactory)
            self.current = 3
        elif self.current == 3:
            self.label.config(image=self.photoInterchange)
            self.current = 4
        elif self.current == 4:
            self.label.config(image=self.photoLab)
            self.current = 5
        elif self.current == 5:
            self.label.config(image=self.photoShorline)
            self.current = 6
        else :
            self.label.config(image=self.photoWood)
            self.current = 1


            
class OpacityChanger:
    def __init__(self, fenetre):
        self.opacity = 1.0
        self.fenetre = fenetre

    def change_opacity(self, event):
        if self.opacity == 1.0:
            self.fenetre.attributes("-alpha", 0.0)
            self.opacity = 0.0
        else:
            self.fenetre.attributes("-alpha", 1.0)
            self.opacity = 1.0

class Fenetre:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.attributes("-topmost", True)
        self.fenetre.lift()
        self.fenetre.attributes("-fullscreen", True)
    



   
def on_press_callback(e):
    if e.name == "bas":
        fenetre.destroy()
        raise SystemExit

def mainprog(fenetre):
    image = ImageChanger(fenetre)
    opacity = OpacityChanger(fenetre)

    keyboard.on_press(on_press_callback)

    keyboard.on_press_key("right", image.changeImage)
    keyboard.on_press_key("up", opacity.change_opacity)
    
    


if __name__ == "__main__":
    root = Fenetre()
    fenetre = root.fenetre
    mainprog(fenetre)
    fenetre.mainloop()