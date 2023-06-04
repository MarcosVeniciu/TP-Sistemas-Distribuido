import tkinter as tk
from tkinter import ttk
from tkinter import *


LARGEFONT =("Verdana", 35)
MIDFONT =("Verdana", 15)
MINFONT =("Verdana", 9)
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

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (Login, Page1, Page2):

			frame = F(container, self)

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
		frame.tkraise()

# Tela de Login
class Login(tk.Frame):
	

	def __init__(self, parent, controller):
		def verificaSenha():
			print(nome.get())
			print(senha.get())
			return True

		tk.Frame.__init__(self, parent)
		
		fontePadrao = ("Arial", "11")

		# titulo
		conteiner_titulo = Frame(self)
		conteiner_titulo.place(x = 150,y = 20)

		nomeLabel = Label(conteiner_titulo, text="Login", font=("Arial", "40"))
		nomeLabel.pack(side=LEFT)

		# Ler o nome de usuario
		conteiner_usuario = Frame(self)
		conteiner_usuario.place(x = 20,y = 250)

		nomeLabel = Label(conteiner_usuario, text="Nome ", font=fontePadrao)
		nomeLabel.pack(side=LEFT)
	
		nome = Entry(conteiner_usuario)
		nome["width"] = 40 # largura da caixa de texto
		nome["font"] = fontePadrao
		nome.pack(side=LEFT)

		# Ler o nome de usuario
		conteiner_senha = Frame(self) 
		conteiner_senha.place(x = 20,y = 290)

		senhaLabel = Label(conteiner_senha, text="Senha", font=fontePadrao)
		senhaLabel.pack(side=LEFT)
  
		senha = Entry(conteiner_senha)
		senha["width"] = 40 # largura da caixa de texto
		senha["font"] = fontePadrao
		senha.pack(side=LEFT)
	
		
  		# Botão Logar
		conteiner_logar = Frame(self)
		conteiner_logar.place(x = 160,y = 340)
  
		autenticar = Button(conteiner_logar)
		autenticar["text"] = "Logar"
		autenticar["font"] = ("Calibri", "8")
		autenticar["width"] = 12
		autenticar["command"] = lambda : controller.show_frame(Page1) if verificaSenha() == True  else print("Login invalido")
		autenticar.pack()
		

# Tela perfil usuario
class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)

		# Nome do usuario
		label = ttk.Label(self, text ="Nome Usuario", font = MIDFONT)
		label.place(x = 10,y = 10)
  
		# Descrição do perfil Cada linha tem no maximo 66 caracteres
		# posso fazer um loop como nos botoes e divir a string nesse valor
		label = ttk.Label(self, text ="Tenho 126 anos, e a 97 estou na universidade universidade universi", font = MINFONT)
		label.place(x = 10,y = 60)
		label = ttk.Label(self, text ="Tenho 126 anos, e a 97 estou na universidade universidade universi", font = MINFONT)
		label.place(x = 10,y = 75)
		label = ttk.Label(self, text ="Tenho 126 anos, e a 97 estou na universidade universidade universi", font = MINFONT)
		label.place(x = 10,y = 90)


		# Botão da lista de receita do usuario
		button1 = ttk.Button(self, text =" 		 Minhas Receitas 	       		     ", command = lambda : controller.show_frame(Login))
		button1.place(x = 10,y = 150)
  
		# lista de Amigos
		num_amigos = 14
		num_receitas = 1
  
		for i in range(num_amigos): # tem de a largura dos botoes
			button1 = ttk.Button(self, text ="A	   		 			 " + str(num_receitas + i), 
                        		 command = lambda : controller.show_frame(Page2))
			button1.place(x = 10,y = 200 + (28*i))
		
		# botão para adicionar amigo
		button2 = ttk.Button(self, text ="Adicionar Amigo", command = lambda : controller.show_frame(Login))
		button2.place(x = 160,y = 610)


# third window frame page2
class Page2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="Page 1",
							command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		button2 = ttk.Button(self, text ="Login",
							command = lambda : controller.show_frame(Login))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)


# Driver Code
app = tkinterApp()
app.title("Vó Maria")
app.geometry("430x650")
app.tk.call('tk', 'scaling', 2.0)
app.mainloop()

