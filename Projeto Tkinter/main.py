import tkinter as tk
from Janela import App

if __name__ == "__main__":

    root = tk.Tk() #cria a janela
    root.geometry("800x1000")
    app = App(master=root) # criando o APP


    app.mainloop()