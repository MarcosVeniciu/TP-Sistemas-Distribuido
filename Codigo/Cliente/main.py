import tkinter as tk
from tkinter import ttk
from tkinter import *

### import das funcionalidades
import login
import buscar_perfil_proprio

# Variaveis Globais
usuario_logado = "" # nome do usuario logado no sistema
descricao_usuario = "" # descrição do perfil do usuario logado
lista_amigos_usuario = ["", "", "", "", "", "", "", "", "", ""] # lista de amigos do usuario logado




import os
os.system('clear') or None

# Fontes
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
		for F in (Login, perfil_usuario, Perfil_amigo, mostrar_receita, adicionar_receita, adicionar_amigo):

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
			global usuario_logado, descricao_usuario, lista_amigos_usuario

			valid = False   
			if nome.get() != "" and senha.get() != "": # verifica se algo foi digitado
				valid = login.logar(nome.get(), senha.get())
    
			if valid == True:
				usuario_logado = nome.get()
				descricao_usuario, lista_amigos_usuario = buscar_perfil_proprio.requisitar_perfil_proprio(usuario_logado)
				controller.show_frame(perfil_usuario)
			else:
				logarLabel["text"] = "Login invalido!"
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
		autenticar["command"] = lambda : verificaSenha()
		autenticar.pack()
		logarLabel = Label(conteiner_logar, text="", font=fontePadrao)
		logarLabel.pack(side=LEFT, pady= 10, padx= 10)
		

# Tela perfil usuario
class perfil_usuario(tk.Frame):
	
	def __init__(self, parent, controller):
		def setState(): # atualiza as informações que podem mudar ao longo da execução
			usuariolabel["text"] = usuario_logado
			descricaolabel["text"] = descricao_usuario
			amigo_list_1["text"] = lista_amigos_usuario[0]
			amigo_list_2["text"] = lista_amigos_usuario[1]
			amigo_list_3["text"] = lista_amigos_usuario[2]
			amigo_list_4["text"] = lista_amigos_usuario[3]
			amigo_list_5["text"] = lista_amigos_usuario[4]
			amigo_list_6["text"] = lista_amigos_usuario[5]
			amigo_list_7["text"] = lista_amigos_usuario[6]
			amigo_list_8["text"] = lista_amigos_usuario[7]
			amigo_list_9["text"] = lista_amigos_usuario[8]
			amigo_list_10["text"] = lista_amigos_usuario[9]
			
			self.after(40, setState) # atualiza os widget 25 vezes por segundo
   
		def commando(event):
			controller.show_frame(Perfil_amigo)
   
		tk.Frame.__init__(self, parent)
  
		# Nome do usuario
		usuariolabel = ttk.Label(self, text ="", font = MIDFONT)
		usuariolabel.place(x = 10,y = 10)
  
		# Descrição do perfil Cada linha tem no maximo 65 caracteres. Total de 260 caracteres para a descrição
		# adiocionar altomaticamente os - para quebrar uma palavra logo 260 - 3 caracteres por descrição.
		# posso fazer um loop como nos botoes e divir a string nesse valor
		descricaolabel = ttk.Label(self, text ="", font = MINFONT, justify=LEFT)
		descricaolabel.place(x = 8,y = 60)
		


		# Botão da lista de receita do usuario
		button1 = ttk.Button(self, text ="Minhas Receitas", width=50, command = lambda : controller.show_frame(Perfil_amigo))
		button1.place(x = 10,y = 150)
  
		# lista de Amigos
		# Amigo 1
		amigo_list_1 = tk.Label(text= lista_amigos_usuario[0], justify=LEFT, width=51, height=2, master=self, borderwidth=1, relief="groove")
		amigo_list_1.place(x = 10,y = 200 + (0*40))
		amigo_list_1.config(bg= "#e0e1e0")
		amigo_list_1.bind("<Button-1>", commando)
		# Amigo 2
		amigo_list_2 = tk.Label(text= lista_amigos_usuario[1], justify=LEFT, width=51, height=2, master=self, borderwidth=1, relief="groove")
		amigo_list_2.place(x = 10,y = 200 + (1*40))
		amigo_list_2.config(bg= "#e0e1e0")
		amigo_list_2.bind("<Button-1>", commando)
		# Amigo 3
		amigo_list_3 = tk.Label(text= lista_amigos_usuario[2], justify=LEFT, width=51, height=2, master=self, borderwidth=1, relief="groove")
		amigo_list_3.place(x = 10,y = 200 + (2*40))
		amigo_list_3.config(bg= "#e0e1e0")
		amigo_list_3.bind("<Button-1>", commando)
		# Amigo 4
		amigo_list_4 = tk.Label(text= lista_amigos_usuario[3], justify=LEFT, width=51, height=2, master=self, borderwidth=1, relief="groove")
		amigo_list_4.place(x = 10,y = 200 + (3*40))
		amigo_list_4.config(bg= "#e0e1e0")
		amigo_list_4.bind("<Button-1>", commando)
		# Amigo 5
		amigo_list_5 = tk.Label(text= lista_amigos_usuario[4], justify=LEFT, width=51, height=2, master=self, borderwidth=1, relief="groove")
		amigo_list_5.place(x = 10,y = 200 + (4*40))
		amigo_list_5.config(bg= "#e0e1e0")
		amigo_list_5.bind("<Button-1>", commando)
		# Amigo 6
		amigo_list_6 = tk.Label(text= lista_amigos_usuario[5], justify=LEFT, width=51, height=2, master=self, borderwidth=1, relief="groove")
		amigo_list_6.place(x = 10,y = 200 + (5*40))
		amigo_list_6.config(bg= "#e0e1e0")
		amigo_list_6.bind("<Button-1>", commando)
		# Amigo 7
		amigo_list_7 = tk.Label(text= lista_amigos_usuario[6], justify=LEFT, width=51, height=2, master=self, borderwidth=1, relief="groove")
		amigo_list_7.place(x = 10,y = 200 + (6*40))
		amigo_list_7.config(bg= "#e0e1e0")
		amigo_list_7.bind("<Button-1>", commando)
		# Amigo 8
		amigo_list_8 = tk.Label(text= lista_amigos_usuario[7], justify=LEFT, width=51, height=2, master=self, borderwidth=1, relief="groove")
		amigo_list_8.place(x = 10,y = 200 + (7*40))
		amigo_list_8.config(bg= "#e0e1e0")
		amigo_list_8.bind("<Button-1>", commando)
		# Amigo 9	
		amigo_list_9 = tk.Label(text= lista_amigos_usuario[8], justify=LEFT, width=51, height=2, master=self, borderwidth=1, relief="groove")
		amigo_list_9.place(x = 10,y = 200 + (8*40))
		amigo_list_9.config(bg= "#e0e1e0")
		amigo_list_9.bind("<Button-1>", commando)
		# Amigo 10
		amigo_list_10 = tk.Label(text= lista_amigos_usuario[9], justify=LEFT, width=51, height=2, master=self, borderwidth=1, relief="groove")
		amigo_list_10.place(x = 10,y = 200 + (9*40))
		amigo_list_10.config(bg= "#e0e1e0")
		amigo_list_10.bind("<Button-1>", commando)

  

		
		# botão para adicionar amigo
		button2 = ttk.Button(self, text ="Adicionar Amigo", command = lambda : controller.show_frame(adicionar_amigo))
		button2.place(x = 160,y = 610)
		setState()
   
   
# Exibir perfil dos amigos
class Perfil_amigo(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)

		nome = "Nome Usuario"
		# botão para voltar a tela anterior
		button_voltar = ttk.Button(self, text ="Voltar", command = lambda : controller.show_frame(perfil_usuario))
		button_voltar.place(x = 340,y = 10)
		
		# Nome do usuario
		label = ttk.Label(self, text =nome, font = MIDFONT)
		label.place(x = 10,y = 10)
  
		# Descrição do perfil Cada linha tem no maximo 65 caracteres. Total de 260 caracteres para a descrição
		# adiocionar altomaticamente os - para quebrar uma palavra logo 260 - 3 caracteres por descrição.
		# posso fazer um loop como nos botoes e divir a string nesse valor
		label = ttk.Label(self, text ="Tenho 126 anos, e a 97 estou na universidade universidade univers", font = MINFONT)
		label.place(x = 8,y = 60)
		label = ttk.Label(self, text ="Tenho 126 anos, e a 97 estou na universidade universidade univers", font = MINFONT)
		label.place(x = 8,y = 75)
		label = ttk.Label(self, text ="Tenho 126 anos, e a 97 estou na universidade universidade univers", font = MINFONT)
		label.place(x = 8,y = 90)
		label = ttk.Label(self, text ="Tenho 126 anos, e a 97 estou na universidade universidade univers", font = MINFONT)
		label.place(x = 8,y = 105)

  
		# lista de Amigos
		num_amigos = 16
		num_receitas = 1
		palavra = "Receita de Bacalhau				"
  
		for i in range(num_amigos): # tem de a largura dos botoes
			button1 = ttk.Button(self, text = palavra + str(num_receitas + i+10), 
								 width=50,
								 command = lambda : controller.show_frame(mostrar_receita))
			button1.place(x = 10,y = 150 + (28*i))
		
		# botão para adicionar receitas
		if nome != "Usuario logado":
			button2 = ttk.Button(self, text ="Adicionar Receita", command = lambda : controller.show_frame(adicionar_receita))
			button2.place(x = 160,y = 610)

# Tela em que mostra a receita escolhida
class mostrar_receita(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
  
		# botão para voltar a tela anterior
		button_voltar = ttk.Button(self, text ="Voltar", command = lambda : controller.show_frame(Perfil_amigo))
		button_voltar.place(x = 340,y = 10)
  
		# Titulo da receita
		label = ttk.Label(self, text ="Receita de Bacalhau", font = MIDFONT)
		label.place(x = 10,y = 10)
  
		# Botão avaliar receita
		button_voltar = ttk.Button(self, text ="Garfadas 15", command = lambda : controller.show_frame(mostrar_receita))
		button_voltar.place(x = 160,y = 610)
  
		# Ingredientes
		label_ingredientes = ttk.Label(self, text ="Ingredientes:", font = MIDFONT)
		label_ingredientes.place(x = 10,y = 70)

		ingredientes = ["2kg de bacalhau", "500g de manteiga", "2L de água sanitaria", "2 batatas"]	
		nun_ingredientes = len(ingredientes)
		
		for i in range(nun_ingredientes):
			label = ttk.Label(self, text ="   - " + ingredientes[i], font = MINFONT)
			label.place(x = 10,y = 100 + (i*20))
   
   
		# Modo Preparo
		linha_inicio = 100 + (nun_ingredientes*20) + 50
		label_ingredientes = ttk.Label(self, text ="Modo Preparo:", font = MIDFONT)
		label_ingredientes.place(x = 10,y = linha_inicio)

		lista_preparo = ["Junta tudo em uma panela", "joga a agua sanitaria e torce pra dar certo", " se não der certo, corre"]	
		nun_pasos = len(lista_preparo)
		
		for i in range(nun_pasos):
			label = ttk.Label(self, text =lista_preparo[i], font = MINFONT)
			label.place(x = 10,y = linha_inicio + 30 + (i*20))
  

class adicionar_receita(tk.Frame):
	

	def __init__(self, parent, controller):
		lista_ingredientes = [] # adicionar_receita
  
		def salvar_receita():
			preparo = modo_preparo.get(1.0,END)
			controller.show_frame(perfil_usuario)

		def listar_ingredientes():
			texto = ""
			ingrediente = ingredientes.get()
			ingredientes.delete(0, tk.END)
			if ingrediente != "":
				lista_ingredientes.append(ingrediente) 
				inicio = len(lista_ingredientes)-13 if len(lista_ingredientes) >= 13 else 0 # exibi apenas os ultimos 15 ingredientes	

				for i in range(inicio, len(lista_ingredientes)):
					texto += lista_ingredientes[i] + "\n"
				listar_ingredienetesLabel["text"] = texto
   
		tk.Frame.__init__(self, parent)
		fontePadrao = ("Arial", "11")
  
		
		# botão para voltar a tela anterior
		button_voltar = ttk.Button(self, text ="Voltar", command = lambda : controller.show_frame(perfil_usuario))
		button_voltar.place(x = 340,y = 10)
  
		# Titulo da receita
		label = ttk.Label(self, text ="Adicionar Receita", font = MIDFONT)
		label.place(x = 10,y = 10)

  
		# Adicionar Titulo
		tituloLabel = Label(self, text="Titulo", font=("Arial", "14"))
		tituloLabel.place(x = 8,y = 60)
  
		conteiner_titulo = Frame(self)
		conteiner_titulo.place(x = 8,y = 88)

		titulo = Entry(conteiner_titulo)
		titulo["width"] = 40 # largura da caixa de texto
		titulo["font"] = fontePadrao
		titulo.pack(side=LEFT)
  

		# Adicionar Ingredientes
		ingredientesLabel = Label(self, text="Ingredientes:", font=("Arial", "14"))
		ingredientesLabel.place(x = 8,y = 130)
  
		conteiner_ingredientes = Frame(self)
		conteiner_ingredientes.place(x = 8,y = 158)
  
		ingredientes = Entry(conteiner_ingredientes)
		ingredientes["width"] = 40 # largura da caixa de texto
		ingredientes["font"] = fontePadrao
		ingredientes.pack(side=LEFT)
		

		add_ingrediente = ttk.Button(conteiner_ingredientes, text ="Add", command = lambda : listar_ingredientes())
		add_ingrediente.pack(side=LEFT, padx= 5)
		listar_ingredienetesLabel = Label(self, text="", font=("Arial", "9"), justify=LEFT)
		listar_ingredienetesLabel.place(x = 8, y = 200)
  
		# Modo Preparo
		preparoLabel = Label(self, text="Modo Preparo:", font=("Arial", "14"))
		preparoLabel.place(x = 8,y = 400)
		modo_preparo = Text(self, height = 10, width = 51)
		modo_preparo.place(x = 8, y= 428)


		# botão para adicionar a receita
		button_salvar = ttk.Button(self, text ="Salvar Receita", command = lambda: salvar_receita)#lambda : controller.show_frame(Perfil_amigo))
		button_salvar.place(x = 160,y = 610)

class adicionar_amigo(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		fontePadrao = ("Arial", "11")
  
		# botão para voltar a tela anterior
		button_voltar = ttk.Button(self, text ="Voltar", command = lambda : controller.show_frame(perfil_usuario))
		button_voltar.place(x = 340,y = 10)
  
		# Titulo da receita
		label = ttk.Label(self, text ="Adicionar Amigo", font = MIDFONT)
		label.place(x = 10,y = 10)

  
		# Adicionar Titulo
		nomeLabel = Label(self, text="Nome", font=("Arial", "14"))
		nomeLabel.place(x = 8,y = 60)
  
		conteiner_nome = Frame(self)
		conteiner_nome.place(x = 8,y = 88)

		nome = Entry(conteiner_nome)
		nome["width"] = 40 # largura da caixa de texto
		nome["font"] = fontePadrao
		nome.pack(side=LEFT)
  

		

		# botão para adicionar a receita
		button_buscar = ttk.Button(self, text ="Adiocionar Amigo", command = lambda : controller.show_frame(perfil_usuario))
		button_buscar.place(x = 160,y = 610)
		
    
# Driver Code
app = tkinterApp()
app.title("Vó Maria")
app.geometry("430x650")
app.tk.call('tk', 'scaling', 2.0)
app.mainloop()

