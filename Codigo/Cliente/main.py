import tkinter as tk
from tkinter import ttk
from tkinter import *


LARGEFONT =("Verdana", 35)

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
		for F in (StartPage, Page1, Page2):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# Tela de Login
class StartPage(tk.Frame):
	

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
		
	
		


# second window frame page1
class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place
		# by using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="Page 2",
							command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)




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
		button2 = ttk.Button(self, text ="Startpage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)


# Driver Code
app = tkinterApp()
app.title("Vó Maria")
app.geometry("430x650")
app.tk.call('tk', 'scaling', 2.0)
app.mainloop()

