import customtkinter 
from models.janela import App
import os
import sys
from PIL import Image, ImageTk


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

if __name__ == "__main__":

    icon_path = resource_path("icon2.png")
  
    root = customtkinter.CTk()
    root.geometry("900x600")
    root.title("Vagabundagem 1.0")
    root._set_appearance_mode("dark")

    icon_image = Image.open(icon_path)
    icon = ImageTk.PhotoImage(icon_image)

    root.iconphoto(False, icon)

    app = App(master=root)
    
    root.mainloop()

# código de compilamento :D pyinstaller --noconfirm --onefile --windowed --icon=icon2.png --add-data "icon2.png;." --add-data "models;models" --add-data "dados.txt;." --hidden-import "models.janela" --hidden-import "models.conexao" main.py