import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from func import troca
import os

class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)
        
        self.cordenadax = 300 
        self.cordenaday = 100
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

        #criando as abas

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.first_tab = tk.Frame(self.notebook)
        self.notebook.add(self.first_tab, text="1")

        self.second_tab = tk.Frame(self.notebook)
        self.notebook.add(self.second_tab, text="2")

        #colocando os fundos
        self.image = Image.open(os.path.join(self.base_dir, "images", "coracao.jpg"))
        self.image2 = Image.open(os.path.join(self.base_dir, "images", "momo.jpg"))

        self.image = self.image.resize((800, 1000))
        self.image2 = self.image2.resize((800,1000))
        self.background_image = ImageTk.PhotoImage(self.image) 
        self.background_image2 = ImageTk.PhotoImage(self.image2)

        self.fundo = tk.Label(self.first_tab, image=self.background_image)
        self.fundo.place(x=0, y=0,relwidth=1, relheight=1)
   
        self.fundo2 = tk.Label(self.second_tab, image= self.background_image2)
        self.fundo2.place(x=0, y=0, relheight=1, relwidth=1)

        self.create_widgets()

    def create_widgets(self):

        #criando o botão sim
        self.yes_button = tk.Button(self.first_tab, text="Sim", command= self.click_yes, width= 10, height= 2, justify="center")
        self.yes_button.place(x=300, y= 150)
        
        # criando o botão não e sua bind
        self.no_button = tk.Button(self.first_tab, text= "Não", width= 10, height=2, justify="center" )
        self.no_button.place(x= 400, y=150)

        self.no_button.bind("<Enter>", self.on_enter)
        
        #criando o texto 
        self.text = tk.Label(self.first_tab, text= "Quer casar comigo?", background= "black", foreground= "white")
        self.text.config(font=("Helvetica", 20))
        self.text.place(x= 280, y= 50)
    
        self.text2 = tk.Label(self.second_tab, text= "ESTAMOS CASADOS!", background="black",  foreground= "white")
        self.text2.config(font=("Helvetica", 20))
        self.text2.place(x= 280, y= 50)

        self.text3 = tk.Label(self.second_tab, text= "TE AMO MEU AMOR 💓", background= "black", foreground= "white")
        self.text3.config(font=("Helvetica", 20))
        self.text3.place(x= 270, y= 750)

    def on_enter(self, event):
        self.click_no()

    def click_no(self):
        self.cordenadax, self.cordenaday = troca()

        self.no_button.place(x=self.cordenadax, y= self.cordenaday)

    def click_yes(self):
        self.notebook.select(self.second_tab)
        
