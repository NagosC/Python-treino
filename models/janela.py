import customtkinter
from datetime import datetime, timedelta
from models.conexao import cria_task


class App(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__( master)
        self._fonte = "Arial"
        self._texto_input = []
        self.counter = 0
        self._switch_var = ""
        self.selected_date = datetime.today()
        self.color = "#5b1d73"
        self.hover_color = "#C850C0"
        self.pack(fill= customtkinter.BOTH, expand = True)

        # ----------------------------- TRATAMENTO DE DATAS----------------------------
        self.dates = [(self.selected_date + timedelta(days=i)).strftime("%d/%m/%Y") 
                 for i in range(-3, 4)]
        
        self.times = [(datetime(2024, 1, 1, 8, 0) + timedelta(minutes=30 * i)).strftime("%H:%M")
                      for i in range(((18 - 8) * 60) // 30 + 1)]
        
        current_date_str = self.selected_date.strftime("%d/%m/%Y")
        self.dates.remove(current_date_str)

        self.dates.insert(0, current_date_str)

        # ----------------------------- TRATAMENTO DE DATAS----------------------------
        self.create_widgets()
    
    
    def create_widgets(self):
        self.label = customtkinter.CTkLabel(self, text = "Preencha para enviar as tasks!", font=("Arial", 20), text_color="#ffffff")
        self.label.pack(pady=10)

        self.label2 = customtkinter.CTkLabel(self, text=f"Quantidade de leads adicionados {self.counter}")
        self.label2.pack()
        self.label2.place(x = 500, y = 250)

        self.creat_buttons()
        self.create_inputs()
        self.create_list()
        self.create_check()
        self.create_switch()
        self.telinha()
            
   

    def creat_buttons(self):
        self.button = customtkinter.CTkButton(self, text= "Enviar", command=self.button_call, corner_radius=32, fg_color=self.color, 
        hover_color=self.hover_color, text_color="#ffffff", font=(self._fonte,15))
        self.button.pack(pady=20)
        self.button.place(x = 325, y = 510)

    def create_inputs(self):
        self.entrada = customtkinter.CTkEntry(self, placeholder_text= "Digite o nome e o número do lead", text_color="#ffffff", width= 400)
        self.entrada.pack(pady = 20)
        self.entrada.place(x= 225, y= 100)

    def create_list(self):
        self.lista_casos = customtkinter.CTkComboBox(self,values=["IMP", "Along", "Usucap", "Along+IMP"], border_color=self.color, button_color=self.color, button_hover_color= self.color)
        self.lista_casos.pack(pady = 20)
        self.lista_casos.place(x = 85, y = 185)

        self.data = customtkinter.CTkComboBox(self, values= self.dates, border_color=self.color, button_color=self.color, button_hover_color= self.color)
        self.data.pack(pady = 20)
        self.data.place(x = 85 , y = 330)

        

    def create_check(self):
        self.operadores = customtkinter.CTkOptionMenu(self, values=["Gustavo", "Larissa"], fg_color= self.color, button_color= self.color, button_hover_color= self.color)
        self.operadores.pack(pady = 20)
        self.operadores.place(x= 325 , y= 185)

        self.projeto = customtkinter.CTkOptionMenu(self, values=["Alpha", "Beta"], fg_color= self.color, button_color= self.color, button_hover_color= self.color)
        self.projeto.pack(pady = 20)
        self.projeto.place(x= 525 , y= 185)
    
    def create_switch(self):
        self.opcao = customtkinter.CTkSwitch(self,text="Adicionar horário?", onvalue=1, offvalue=0, button_color= self.color, progress_color=self.hover_color, command=self.mudanca)
        self.opcao.pack(pady = 20)
        self.opcao.place(x = 85, y = 260)

    def lista_horarios(self):
        self.time = customtkinter.CTkComboBox(self, values= self.times, border_color= self.color, button_color= self.color, button_hover_color= self.color)
        self.time.pack(pady = 20)
        self.time.place(x = 300, y=330)

    def mudanca(self):
        state = self.opcao.get()

        if(state == 1):
            self.lista_horarios()
        else:
            self.time.destroy()

    def telinha(self):
        self.tela = customtkinter.CTkTextbox(self, border_color= self.color, text_color= "#ffffff", width= 300)
        self.tela.pack(pady = 20)
        self.tela .place(x = 500, y = 290)

    def telinha_insert(self, tarefa):

        self.counter += 1

        tarefa_linha = tarefa.replace("\n", " ").strip()

        n = str(self.counter - 1.0)
        self.label2.configure(text=f"Quantidade de leads adicionados {self.counter}")

        self.tela.insert(index= n, text= f"{tarefa_linha}")

    
    def button_call(self):
        try:
            lead_input = "🚨 " + self.entrada.get().strip()
            lead_input = lead_input.replace("\n", " ").strip()
            self._texto_input.extend([
                lead_input, 
                self.lista_casos.get(), 
                self.operadores.get(), 
                self.projeto.get(), 
                str(self.data.get())
            ])

            if self.opcao.get() == 1:
                self._texto_input.append(str(self.time.get()))
                task = cria_task(self._texto_input[0], self._texto_input[2], 
                                self._texto_input[4], self._texto_input[1], 
                                self._texto_input[5])
            else:
                task = cria_task(self._texto_input[0], self._texto_input[2], 
                                self._texto_input[4], self._texto_input[1])

            self.telinha_insert(tarefa=task)

        except Exception as e:
            self.tela.insert("end", f"Erro: {str(e)}\n")  # Exibe o erro na tela

        finally:
            self._texto_input.clear()






        

