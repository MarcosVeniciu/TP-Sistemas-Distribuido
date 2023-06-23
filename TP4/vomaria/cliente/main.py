import tkinter as tk
from tkinter import ttk
from tkinter import *
from objetos.usuario import Usuario
from objetos.amigo import Amigo
from objetos.receita import Receita
import os


os.system('clear') or None

# Fontes
LARGEFONT =("Verdana", 35)
MIDFONT =("Verdana", 15)
MINFONT =("Verdana", 9)
Taxa_Atualizacao = 2


class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

  
		# variaveis de controle
		self.usuario = Usuario()
		self.receita = Receita()
		self.amigo = Amigo()

		self.usuario_lista_amigos = [tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(),
                       		 tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()]
  
		self.usuario_lista_receitas = [tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(),
                       		   tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()]
		
		self.amigo_lista_receitas = [tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(),
                       		 		 tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()]
  
		
		# Inicializa as variaveis com um valor padão  
		for i in range(len(self.usuario_lista_amigos)):
			self.usuario_lista_amigos[i].set("")
			self.usuario_lista_receitas[i].set("")
			self.amigo_lista_receitas[i].set("")


		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (Login, perfil_usuario, Perfil_usuario_receitas, Perfil_amigo, mostrar_receita_usuario, mostrar_receita_amigo, adicionar_receita, adicionar_amigo):
			if F == Login:
				frame = F(container, self, self.usuario, self.usuario_lista_amigos)

			if F == perfil_usuario:
				frame = F(container, self, self.amigo, self.usuario, self.usuario_lista_amigos, self.amigo_lista_receitas, self.usuario_lista_receitas)
    
			if F == Perfil_usuario_receitas:
				frame = F(container, self, self.usuario, self.usuario_lista_receitas, self.receita)

			if F == Perfil_amigo:
				frame = F(container, self, self.amigo, self.amigo_lista_receitas, self.receita)

			if F == mostrar_receita_usuario:
				frame = F(container, self, self.receita)

			if F == mostrar_receita_amigo:
				frame = F(container, self, self.receita)
    
			if F == adicionar_receita:
				frame = F(container, self, self.usuario, self.usuario_lista_receitas)

			if F == adicionar_amigo:
				frame = F(container, self, self.usuario, self.usuario_lista_amigos)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(Login)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.grid()
		frame.tkraise()

# Tela de Login
class Login(tk.Frame):
	def __init__(self, parent, controller, usuario, usuario_lista_amigos):
		tk.Frame.__init__(self, parent)
		fontePadrao = ("Arial", "11")

		self.usuario_lista_amigos = usuario_lista_amigos
		self.controller = controller		
		self.usuario = usuario
  
		# titulo
		self.conteiner_titulo = Frame(self)
		self.conteiner_titulo.place(x = 150,y = 20)

		self.nomeLabel = Label(self.conteiner_titulo, text="Login", font=("Arial", "40"))
		self.nomeLabel.pack(side=LEFT)

		# Ler o nome de usuario
		self.conteiner_usuario = Frame(self)
		self.conteiner_usuario.place(x = 20,y = 250)

		self.nomeLabel = Label(self.conteiner_usuario, text="Nome ", font=fontePadrao)
		self.nomeLabel.pack(side=LEFT)
	
		self.nome = Entry(self.conteiner_usuario)
		self.nome["width"] = 40 # largura da caixa de texto
		self.nome["font"] = fontePadrao
		self.nome.pack(side=LEFT)

		# Ler o nome de usuario
		self.conteiner_senha = Frame(self) 
		self.conteiner_senha.place(x = 20,y = 290)

		self.senhaLabel = Label(self.conteiner_senha, text="Senha", font=fontePadrao)
		self.senhaLabel.pack(side=LEFT)
  
		self.senha = Entry(self.conteiner_senha)
		self.senha["width"] = 40 # largura da caixa de texto
		self.senha["font"] = fontePadrao
		self.senha["show"] = "*"
		self.senha.pack(side=LEFT)
	
		
  		# Botão Logar
		self.conteiner_logar = Frame(self)
		self.conteiner_logar.place(x = 160,y = 340)
  
		self.autenticar = Button(self.conteiner_logar)
		self.autenticar["text"] = "Logar"
		self.autenticar["font"] = ("Calibri", "8")
		self.autenticar["width"] = 12
		self.autenticar["command"] = lambda : self.verificaSenha()
		self.autenticar.pack()
		self.logarLabel = Label(self.conteiner_logar, text="", font=fontePadrao)
		self.logarLabel.pack(side=LEFT, pady= 10, padx= 10)
	
	def verificaSenha(self):
			valid = False   
			if self.nome.get() != "" and self.senha.get() != "": # verifica se algo foi digitado
				valid = self.usuario.logar(self.nome.get(), self.senha.get())

			if valid == True:
				self.usuario.get_usuario()
				self.lista_amigos = self.usuario.get_lista_amigos()
				for i in range(len(self.lista_amigos)):
					self.usuario_lista_amigos[i].set(self.lista_amigos[i])
     				
				self.controller.show_frame(perfil_usuario)
			else:
				self.logarLabel["text"] = "Login invalido!"
			return True

# Tela perfil usuario
class perfil_usuario(tk.Frame):
	
	def __init__(self, parent, controller, amigo, usuario, usuario_lista_amigos, amigo_lista_receitas, usuario_lista_receitas):
		tk.Frame.__init__(self, parent)
  
		self.amigo = amigo
		self.usuario = usuario

		self.amigo_lista_receita = amigo_lista_receitas  
		self.usuario_lista_amigos = usuario_lista_amigos
		self.usuario_lista_receitas = usuario_lista_receitas
			
		
		self.controller = controller

  
		# Nome do usuario
		self.usuariolabel = ttk.Label(self, text ="", font = MIDFONT)
		self.usuariolabel.place(x = 10,y = 10)
  
		# Descrição do perfil 
		self.descricaolabel = ttk.Label(self, text ="", font = MINFONT, justify=LEFT)
		self.descricaolabel.place(x = 8,y = 60)
		


		# Botão da lista de receita do usuario
		self.button1 = ttk.Button(self, text ="Minhas Receitas", width=50, command = lambda : self.minhas_receitas())
		self.button1.place(x = 10,y = 140)
  
		# lista de Amigos
		style = ttk.Style()
		style.configure("NoBorder.TButton", relief="flat", borderwidth=0)
		# Amigo 1
		y_base = 185
		#if self.usuario_lista_amigos[0].get() != "":
		self.amigo_list_1 = ttk.Button(self, text = self.usuario_lista_amigos[0].get(), style="NoBorder.TButton", width=50, command = lambda : self.commando(self.usuario_lista_amigos[0].get()))
		self.amigo_list_1.place(x = 10,y =y_base + (28*0))
		# Amigo 2
		#if self.usuario_lista_amigos[1].get() != "":
		self.amigo_list_2 = ttk.Button(self, text = self.usuario_lista_amigos[1].get(), style="NoBorder.TButton", width=50, command = lambda : self.commando(self.usuario_lista_amigos[1].get()))
		self.amigo_list_2.place(x = 10,y = y_base + (28*1))
		# Amigo 3
		#if self.usuario_lista_amigos[2].get() != "":
		self.amigo_list_3 = ttk.Button(self, text = self.usuario_lista_amigos[2].get(), style="NoBorder.TButton", width=50, command = lambda : self.commando(self.usuario_lista_amigos[2].get()))
		self.amigo_list_3.place(x = 10,y = y_base + (28*2))
		# Amigo 4
		#if self.usuario_lista_amigos[3].get() != "":
		self.amigo_list_4 = ttk.Button(self, text = self.usuario_lista_amigos[3].get(), style="NoBorder.TButton", width=50, command = lambda : self.commando(self.usuario_lista_amigos[3].get()))
		self.amigo_list_4.place(x = 10,y = y_base + (28*3))
		# Amigo 5
		#if self.usuario_lista_amigos[4].get() != "":
		self.amigo_list_5 = ttk.Button(self, text = self.usuario_lista_amigos[4].get(), style="NoBorder.TButton", width=50, command = lambda : self.commando(self.usuario_lista_amigos[4].get()))
		self.amigo_list_5.place(x = 10,y = y_base + (28*4))
		# Amigo 6
		#if self.usuario_lista_amigos[5].get() != "":
		self.amigo_list_6 = ttk.Button(self, text = self.usuario_lista_amigos[5].get(), style="NoBorder.TButton", width=50, command = lambda : self.commando(self.usuario_lista_amigos[5].get()))
		self.amigo_list_6.place(x = 10,y = y_base + (28*5))
		# Amigo 7
		#if self.usuario_lista_amigos[6].get() != "":
		self.amigo_list_7 = ttk.Button(self, text = self.usuario_lista_amigos[6].get(), style="NoBorder.TButton", width=50, command = lambda : self.commando(self.usuario_lista_amigos[6].get()))
		self.amigo_list_7.place(x = 10,y = y_base + (28*6))
		# Amigo 8
		#if self.usuario_lista_amigos[7].get() != "":
		self.amigo_list_8 = ttk.Button(self, text = self.usuario_lista_amigos[7].get(), style="NoBorder.TButton", width=50, command = lambda : self.commando(self.usuario_lista_amigos[7].get()))
		self.amigo_list_8.place(x = 10,y = y_base + (28*7))
		# Amigo 9
		#if self.usuario_lista_amigos[8].get() != "":
		self.amigo_list_9 = ttk.Button(self, text = self.usuario_lista_amigos[8].get(), style="NoBorder.TButton", width=50, command = lambda : self.commando(self.usuario_lista_amigos[8].get()))
		self.amigo_list_9.place(x = 10,y = y_base + (28*8))
		# Amigo 10
		#if self.usuario_lista_amigos[9].get() != "":
		self.amigo_list_10 = ttk.Button(self, text = self.usuario_lista_amigos[9].get(), style="NoBorder.TButton", width=50, command = lambda : self.commando(self.usuario_lista_amigos[9].get()))
		self.amigo_list_10.place(x = 10,y = y_base + (28*9))
  

		
		# botão para adicionar amigo
		button2 = ttk.Button(self, text ="Adicionar Amigo", command = lambda : controller.show_frame(adicionar_amigo))
		button2.place(x = 160,y = 610)
		self.setState()
	
	def minhas_receitas(self):
		self.lista = self.usuario.get_lista_receitas()
		for i in range(len(self.lista)):
			self.usuario_lista_receitas[i].set(self.lista[i])

		self.controller.show_frame(Perfil_usuario_receitas)
  
	def commando(self, nome_amigo):# mostra o perfil do amigo
			if nome_amigo != "":
				self.amigo.get_amigo()
				self.lista_receitas = self.amigo.get_lista_receitas()
				for i in range(len(self.lista_receitas)):
					self.amigo_lista_receita[i].set(self.lista_receitas[i])
				self.controller.show_frame(Perfil_amigo)

	def setState(self):
		self.usuariolabel["text"] = self.usuario.get_nome()
		self.descricaolabel["text"] = self.usuario.get_descricao()

		self.amigo_list_1["text"] = self.usuario_lista_amigos[0].get()
		self.amigo_list_2["text"] = self.usuario_lista_amigos[1].get()
		self.amigo_list_3["text"] = self.usuario_lista_amigos[2].get()
		self.amigo_list_4["text"] = self.usuario_lista_amigos[3].get()
		self.amigo_list_5["text"] = self.usuario_lista_amigos[4].get()
		self.amigo_list_6["text"] = self.usuario_lista_amigos[5].get()
		self.amigo_list_7["text"] = self.usuario_lista_amigos[6].get()
		self.amigo_list_8["text"] = self.usuario_lista_amigos[7].get()
		self.amigo_list_9["text"] = self.usuario_lista_amigos[8].get()
		self.amigo_list_10["text"] = self.usuario_lista_amigos[9].get()
  
		self.after(Taxa_Atualizacao, self.setState) # atualiza os widget 25 vezes por segundo
  
# mostra a lista de receitas do usuario logado
class Perfil_usuario_receitas(tk.Frame):

	def __init__(self, parent, controller, usuario, usuario_lista_receita, receita):
		self.receita = receita
		self.usuario = usuario
		self.controller = controller
		self.usuario_lista_receita = usuario_lista_receita
		
		tk.Frame.__init__(self, parent)

		# botão para voltar a tela anterior
		self.button_voltar = ttk.Button(self, text ="Voltar", command = lambda : controller.show_frame(perfil_usuario))
		self.button_voltar.place(x = 340,y = 10)
		
		# Nome do usuario
		self.label = ttk.Label(self, text ="", font = MIDFONT)
		self.label.place(x = 10,y = 10)
  
		# Descrição do perfil
		self.descricaolabel = ttk.Label(self, text ="", font = MINFONT, justify=LEFT)
		self.descricaolabel.place(x = 8,y = 60)
  
		# lista de Receitas
		style = ttk.Style()
		style.configure("NoBorder.TButton", relief="flat", borderwidth=0)
		# Receita 1
		self.receita_list_1 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.usuario_lista_receita[0].get()))
		self.receita_list_1.place(x = 10,y = 150 + (28*0))
		# Receita 2
		self.receita_list_2 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.usuario_lista_receita[1].get()))
		self.receita_list_2.place(x = 10,y = 150 + (28*1))
		# Receita 3
		self.receita_list_3 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.usuario_lista_receita[2].get()))
		self.receita_list_3.place(x = 10,y = 150 + (28*2))
		# Receita 4
		self.receita_list_4 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.usuario_lista_receita[3].get()))
		self.receita_list_4.place(x = 10,y = 150 + (28*3))
		# Receita 5
		self.receita_list_5 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.usuario_lista_receita[4].get()))
		self.receita_list_5.place(x = 10,y = 150 + (28*4))
		# Receita 6
		self.receita_list_6 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.usuario_lista_receita[5].get()))
		self.receita_list_6.place(x = 10,y = 150 + (28*5))
		# Receita 7
		self.receita_list_7 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.usuario_lista_receita[6].get()))
		self.receita_list_7.place(x = 10,y = 150 + (28*6))
		# Receita 8
		self.receita_list_8 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.usuario_lista_receita[7].get()))
		self.receita_list_8.place(x = 10,y = 150 + (28*7))
		# Receita 9	
		self.receita_list_9 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.usuario_lista_receita[8].get()))
		self.receita_list_9.place(x = 10,y = 150 + (28*8))
		# Receita 10
		self.receita_list_10 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.usuario_lista_receita[9].get()))
		self.receita_list_10.place(x = 10,y = 150 + (28*9))
		
		# botão para adicionar receitas
		self.button2 = ttk.Button(self, text = "Adicionar Receita", command = lambda : controller.show_frame(adicionar_receita))
		self.button2.place(x = 160,y = 610)

		self.setState()
  
	def commando(self, receita):
			if receita != "":
				self.receita.get_receita()
				self.controller.show_frame(mostrar_receita_usuario)
    
	def setState(self):
		self.label["text"] = self.usuario.get_nome()
		self.descricaolabel["text"] = self.usuario.get_descricao()

		self.receita_list_1["text"] = self.usuario_lista_receita[0].get()
		self.receita_list_2["text"] = self.usuario_lista_receita[1].get()
		self.receita_list_3["text"] = self.usuario_lista_receita[2].get()
		self.receita_list_4["text"] = self.usuario_lista_receita[3].get()
		self.receita_list_5["text"] = self.usuario_lista_receita[4].get()
		self.receita_list_6["text"] = self.usuario_lista_receita[5].get()
		self.receita_list_7["text"] = self.usuario_lista_receita[6].get()
		self.receita_list_8["text"] = self.usuario_lista_receita[7].get()
		self.receita_list_9["text"] = self.usuario_lista_receita[8].get()
		self.receita_list_10["text"] = self.usuario_lista_receita[9].get()
		
		self.after(Taxa_Atualizacao, self.setState) # atualiza os widget 25 vezes por segundo

# Exibir perfil dos amigos
class Perfil_amigo(tk.Frame):

	def __init__(self, parent, controller, amigo, amigo_lista_receita, receita):
     
		self.amigo = amigo
		self.receita = receita
		self.controller = controller
		self.amigo_lista_receita = amigo_lista_receita
  
		tk.Frame.__init__(self, parent)

		# botão para voltar a tela anterior
		self.button_voltar = ttk.Button(self, text ="Voltar", command = lambda : controller.show_frame(perfil_usuario))
		self.button_voltar.place(x = 340,y = 10)
		
		# Nome do usuario
		self.label_nome_amigo = ttk.Label(self, text ="", font = MIDFONT)
		self.label_nome_amigo.place(x = 10,y = 10)
  
		# Descrição do perfil
		self.amigo_descricaolabel = ttk.Label(self, text ="", font = MINFONT, justify=LEFT)
		self.amigo_descricaolabel.place(x = 8,y = 60)
  
		# lista de Receitas
		style = ttk.Style()
		style.configure("NoBorder.TButton", relief="flat", borderwidth=0)
		# Receita 1
		self.receita_list_1 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.amigo_lista_receita[0].get()))
		self.receita_list_1.place(x = 10,y = 150 + (28*0))
		# Receita 2
		self.receita_list_2 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.amigo_lista_receita[1].get()))
		self.receita_list_2.place(x = 10,y = 150 + (28*1))
		# Receita 3
		self.receita_list_3 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.amigo_lista_receita[2].get()))
		self.receita_list_3.place(x = 10,y = 150 + (28*2))
		# Receita 4
		self.receita_list_4 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.amigo_lista_receita[3].get()))
		self.receita_list_4.place(x = 10,y = 150 + (28*3))
		# Receita 5
		self.receita_list_5 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.amigo_lista_receita[4].get()))
		self.receita_list_5.place(x = 10,y = 150 + (28*4))
		# Receita 6
		self.receita_list_6 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.amigo_lista_receita[5].get()))
		self.receita_list_6.place(x = 10,y = 150 + (28*5))
		# Receita 7
		self.receita_list_7 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.amigo_lista_receita[6].get()))
		self.receita_list_7.place(x = 10,y = 150 + (28*6))
		# Receita 8
		self.receita_list_8 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.amigo_lista_receita[7].get()))
		self.receita_list_8.place(x = 10,y = 150 + (28*7))
		# Receita 9	
		self.receita_list_9 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.amigo_lista_receita[8].get()))
		self.receita_list_9.place(x = 10,y = 150 + (28*8))
		# Receita 10
		self.receita_list_10 = ttk.Button(self, text = "", width=50, style="NoBorder.TButton", command = lambda : self.commando(self.amigo_lista_receita[9].get()))
		self.receita_list_10.place(x = 10,y = 150 + (28*9))
		
		self.setState()

	def commando(self, nome_receita):
			if nome_receita != "":
				self.receita.get_receita()
				self.controller.show_frame(mostrar_receita_amigo)
    
	def setState(self):
		self.label_nome_amigo["text"] = self.amigo.get_nome()
		self.amigo_descricaolabel["text"] = self.amigo.get_descrisao()

		self.receita_list_1["text"] = self.amigo_lista_receita[0].get()
		self.receita_list_2["text"] = self.amigo_lista_receita[1].get()
		self.receita_list_3["text"] = self.amigo_lista_receita[2].get()
		self.receita_list_4["text"] = self.amigo_lista_receita[3].get()
		self.receita_list_5["text"] = self.amigo_lista_receita[4].get()
		self.receita_list_6["text"] = self.amigo_lista_receita[5].get()
		self.receita_list_7["text"] = self.amigo_lista_receita[6].get()
		self.receita_list_8["text"] = self.amigo_lista_receita[7].get()
		self.receita_list_9["text"] = self.amigo_lista_receita[8].get()
		self.receita_list_10["text"] = self.amigo_lista_receita[9].get()

		self.after(Taxa_Atualizacao, self.setState) # atualiza os widget 25 vezes por segundo

# Tela em que mostra a receita do proprio usuario, e ele não pode dar garfadas na propria receita
class mostrar_receita_usuario(tk.Frame):
	def __init__(self, parent, controller, receita):
		self.controller = controller
		self.receita = receita
		
		tk.Frame.__init__(self, parent)      
		# botão para voltar a tela anterior
		self.button_voltar = ttk.Button(self, text ="Voltar", command = lambda : controller.show_frame(Perfil_usuario_receitas))
		self.button_voltar.place(x = 340,y = 10)
  
		# Titulo da receita
		self.label = ttk.Label(self, text ="", font = MIDFONT)
		self.label.place(x = 10,y = 10)
    
		# Ingredientes
		self.label_ingredientes = ttk.Label(self, text ="Ingredientes:", font = MIDFONT)
		self.label_ingredientes.place(x = 10,y = 70)
		
		# Lista de ingredientes
		self.lista_ingredienteslabel = ttk.Label(self, text ="", font = MINFONT)
		self.lista_ingredienteslabel.place(x = 10,y = 100)
   
   
		# Modo Preparo
		self.linha_inicio = 300 + 50
		self.label_ingredientes = ttk.Label(self, text ="Modo Preparo:", font = MIDFONT)
		self.label_ingredientes.place(x = 10,y = self.linha_inicio)

				
		self.label_preparo = ttk.Label(self, text ="", font = MINFONT)
		self.label_preparo.place(x = 10,y = self.linha_inicio + 30)
		self.setState()
  
	def setState(self):
			self.label["text"] = self.receita.get_titulo()
			self.lista_ingredienteslabel["text"] = self.receita.get_lista_ingredientes()
			self.label_preparo["text"] = self.receita.get_modo_preparo()

			self.after(Taxa_Atualizacao, self.setState) # atualiza os widget 25 vezes por segundo

class mostrar_receita_amigo(tk.Frame):
	def __init__(self, parent, controller, receita):
		self.receita = receita
		self.controller = controller

		tk.Frame.__init__(self, parent)

		# botão para voltar a tela anterior
		self.button_voltar = ttk.Button(self, text ="Voltar", command = lambda : controller.show_frame(Perfil_amigo))
		self.button_voltar.place(x = 340,y = 10)
  
		# Titulo da receita
		self.label = ttk.Label(self, text ="", font = MIDFONT)
		self.label.place(x = 10,y = 10)
  
		# Botão avaliar receita
		self.button_garfadas = ttk.Button(self, text ="", command = lambda : self.atualizar_garfadas())
		self.button_garfadas.place(x = 160,y = 610)
  
		# Ingredientes
		self.label_ingredientes = ttk.Label(self, text ="Ingredientes:", font = MIDFONT)
		self.label_ingredientes.place(x = 10,y = 70)
		
		# Lista de ingredientes
		self.lista_ingredienteslabel = ttk.Label(self, text ="", font = MINFONT)
		self.lista_ingredienteslabel.place(x = 10,y = 100)
   
   
		# Modo Preparo
		self.linha_inicio = 300 + 50
		self.label_ingredientes = ttk.Label(self, text ="Modo Preparo:", font = MIDFONT)
		self.label_ingredientes.place(x = 10,y = self.linha_inicio)

				
		self.label_preparo = ttk.Label(self, text ="", font = MINFONT)
		self.label_preparo.place(x = 10,y = self.linha_inicio + 30)
		self.setState()

	def setState(self):
		self.label["text"] = self.receita.get_titulo()
		self.lista_ingredienteslabel["text"] = self.receita.get_lista_ingredientes()
		self.label_preparo["text"] = self.receita.get_modo_preparo()
		self.button_garfadas["text"] = "Garfadas: " + str(self.receita.get_garfadas())

		self.after(Taxa_Atualizacao, self.setState) # atualiza os widget
   
	def atualizar_garfadas(self):
		self.receita.set_garfada()
		self.receita.get_receita()
		self.setState()



# em andamento
class adicionar_receita(tk.Frame):
	
	def __init__(self, parent, controller, usuario, usuario_lista_receita):
		self.controller = controller
		self.usuario = usuario
		self.usuario_lista_receita = usuario_lista_receita

		self.lista_ingredientes = [] # adicionar_receita

		tk.Frame.__init__(self, parent)
		self.fontePadrao = ("Arial", "11")
  		
		# botão para voltar a tela anterior
		self.button_voltar = ttk.Button(self, text ="Voltar", command = lambda : self.controller.show_frame(Perfil_usuario_receitas))
		self.button_voltar.place(x = 340,y = 10)
  
		# Titulo da receita
		self.label = ttk.Label(self, text ="Adicionar Receita", font = MIDFONT)
		self.label.place(x = 10,y = 10)

  
		# Adicionar Titulo
		self.tituloLabel = Label(self, text="Titulo", font=("Arial", "14"))
		self.tituloLabel.place(x = 8,y = 60)
  
		self.conteiner_titulo = Frame(self)
		self.conteiner_titulo.place(x = 8,y = 88)

		self.titulo_receita=tk.StringVar()
		self.titulo = Entry(self.conteiner_titulo, textvariable = self.titulo_receita)
		self.titulo["width"] = 40 # largura da caixa de texto
		self.titulo["font"] = self.fontePadrao
		self.titulo.pack(side=LEFT)
  

		# Adicionar Ingredientes
		self.ingredientesLabel = Label(self, text="Ingredientes:", font=("Arial", "14"))
		self.ingredientesLabel.place(x = 8,y = 130)
  
		self.conteiner_ingredientes = Frame(self)
		self.conteiner_ingredientes.place(x = 8,y = 158)
  
		self.ingredientes = Entry(self.conteiner_ingredientes)
		self.ingredientes["width"] = 40 # largura da caixa de texto
		self.ingredientes["font"] = self.fontePadrao
		self.ingredientes.pack(side=LEFT)
		

		self.add_ingrediente = ttk.Button(self.conteiner_ingredientes, text ="Add", command = lambda : self.listar_ingredientes())
		self.add_ingrediente.pack(side=LEFT, padx= 5)
		self.listar_ingredienetesLabel = Label(self, text="", font=("Arial", "9"), justify=LEFT)
		self.listar_ingredienetesLabel.place(x = 8, y = 200)
  
		# Modo Preparo
		self.preparoLabel = Label(self, text="Modo Preparo:", font=("Arial", "14"))
		self.preparoLabel.place(x = 8,y = 400)
		self.modo_preparo = Text(self, height = 10, width = 51)
		self.modo_preparo.place(x = 8, y= 428)


		# botão para adicionar a receita
		self.button_salvar = ttk.Button(self, text ="Salvar Receita", command = lambda: self.salvar_receita())
		self.button_salvar.place(x = 160,y = 610)

	def salvar_receita(self):
			self.titulo = self.titulo_receita.get()
			self.preparo = self.modo_preparo.get(1.0, END)
			self.usuario.add_receita(self.usuario.get_nome(), self.titulo, self.lista_ingredientes, self.preparo)
			self.usuario.get_usuario()
			lista_receita = self.usuario.get_lista_receitas()
			for i in range(len(lista_receita)):
				self.usuario_lista_receita[i].set(lista_receita[i])
   
			# limpa os campos de titulo, lista_ingrediente e modo preparo
			self.titulo_receita.set("")
			self.modo_preparo.delete("1.0","end")
			self.lista_ingredientes.clear()
			self.listar_ingredienetesLabel["text"] = ""
		
			self.controller.show_frame(Perfil_usuario_receitas)
   
	def listar_ingredientes(self):
			self.texto = ""
			self.ingrediente = self.ingredientes.get()
			self.ingredientes.delete(0, tk.END)
			if self.ingrediente != "":
				self.lista_ingredientes.append(self.ingrediente) 
				inicio = len(self.lista_ingredientes)-13 if len(self.lista_ingredientes) >= 13 else 0 # exibi apenas os ultimos 15 ingredientes	

				for i in range(inicio, len(self.lista_ingredientes)):
					self.texto += self.lista_ingredientes[i] + "\n"
				self.listar_ingredienetesLabel["text"] = self.texto
   
   
   
   
   
class adicionar_amigo(tk.Frame):
	def __init__(self, parent, controller, usuario, usuario_lista_amigos):
		self.usuario_lista_amigos = usuario_lista_amigos
		self.controller = controller
		self.usuario = usuario

		tk.Frame.__init__(self, parent)
		fontePadrao = ("Arial", "11")
		
		# botão para voltar a tela anterior
		self.button_voltar = ttk.Button(self, text ="Voltar", command = lambda : controller.show_frame(perfil_usuario))
		self.button_voltar.place(x = 340,y = 10)
  
		# Titulo da receita
		self.label = ttk.Label(self, text ="Adicionar Amigo", font = MIDFONT)
		self.label.place(x = 10,y = 10)

  
		# Adicionar Titulo
		self.nomeLabel = Label(self, text="Nome", font=("Arial", "14"))
		self.nomeLabel.place(x = 8,y = 60)
  
		self.conteiner_nome = Frame(self)
		self.conteiner_nome.place(x = 8,y = 88)

		self.nome = Entry(self.conteiner_nome)
		self.nome["width"] = 40 # largura da caixa de texto
		self.nome["font"] = fontePadrao
		self.nome.pack(side=LEFT)

		self.label_resposta = Label(self, text="", font=("Arial", "10"), justify=LEFT)
		self.label_resposta.place(x = 8,y = 150)
   

		# botão para adicionar a receita
		self.button_buscar = ttk.Button(self, text ="Adicionar Amigo", command = lambda : self.adicionarAmigo())
		self.button_buscar.place(x = 160,y = 610)
		self.setState()

	def setState(self):
			self.label_resposta["text"] = ""

			self.after(Taxa_Atualizacao*5001, self.setState) # atualiza os widget 25 vezes por segundo

	def adicionarAmigo(self):
			if self.nome.get() != "" and self.nome.get() != self.usuario.get_nome():
				resposta = self.usuario.add_amigo(self.usuario.get_nome(), self.nome.get())	
				if resposta == "adicionado":
					self.usuario.get_usuario()
					lista_amigos = self.usuario.get_lista_amigos()
					self.nome.delete(0, tk.END)
					for i in range(len(lista_amigos)):
						self.usuario_lista_amigos[i].set(lista_amigos[i])
					self.controller.show_frame(perfil_usuario)
				else:
					self.label_resposta["text"] = resposta
# Driver Code

app = tkinterApp()
app.title("Vó Maria")
app.geometry("430x650")
app.tk.call('tk', 'scaling', 2.0)
app.mainloop()
