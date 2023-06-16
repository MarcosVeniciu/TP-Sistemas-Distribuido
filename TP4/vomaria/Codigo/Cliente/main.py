import tkinter as tk
from tkinter import ttk
from tkinter import *

### import das funcionalidades
import usuario
import amigo
import receita

### Variaveis globais
usuario_logado = None
amigo_usuario = amigo.Amigo() 
receitas = receita.Receita()

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
		for F in (Login, perfil_usuario, Perfil_usuario_receitas, Perfil_amigo, mostrar_receita, adicionar_receita, adicionar_amigo):

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
			global usuario_logado

			valid = False   
			if nome.get() != "" and senha.get() != "": # verifica se algo foi digitado
				if (nome.get() == "mario" and senha.get() == "123" ):
					valid = True
     
			if valid == True:
				usuario_logado = usuario.Usuario()
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
   
		def commando(amigo):
			global usuario_buscado, lista_receitas, descricao_amigo 
			if amigo != "":
				usuario_buscado = amigo
				descricao_amigo, lista_receitas = buscar_perfil_amigo.requisitar_perfil_amigo(usuario_logado, amigo)
				controller.show_frame(Perfil_amigo)
		def commando_2(amigo):
			global usuario_buscado, lista_receitas, descricao_amigo 
			if amigo != "":
				usuario_buscado = amigo
				descricao_amigo, lista_receitas = buscar_perfil_amigo.requisitar_perfil_amigo(usuario_logado, amigo)
				controller.show_frame(Perfil_usuario_receitas)
    
   
		tk.Frame.__init__(self, parent)
  
		# Nome do usuario
		usuariolabel = ttk.Label(self, text ="", font = MIDFONT)
		usuariolabel.place(x = 10,y = 10)
  
		# Descrição do perfil 
		descricaolabel = ttk.Label(self, text ="", font = MINFONT, justify=LEFT)
		descricaolabel.place(x = 8,y = 60)
		


		# Botão da lista de receita do usuario
		button1 = ttk.Button(self, text ="Minhas Receitas", width=50, command = lambda : commando_2(usuario_logado))
		button1.place(x = 10,y = 140)
  
		# lista de Amigos
		# Amigo 1
		y_base = 185
		amigo_list_1 = ttk.Button(self, text = lista_amigos_usuario[0], width=50, command = lambda : commando(lista_amigos_usuario[0]))
		amigo_list_1.place(x = 10,y =y_base + (28*0))
		# Amigo 2
		amigo_list_2 = ttk.Button(self, text = lista_amigos_usuario[1], width=50, command = lambda : commando(lista_amigos_usuario[1]))
		amigo_list_2.place(x = 10,y = y_base + (28*1))
		# Amigo 3
		amigo_list_3 = ttk.Button(self, text = lista_amigos_usuario[2], width=50, command = lambda : commando(lista_amigos_usuario[2]))
		amigo_list_3.place(x = 10,y = y_base + (28*2))
		# Amigo 4
		amigo_list_4 = ttk.Button(self, text = lista_amigos_usuario[3], width=50, command = lambda : commando(lista_amigos_usuario[3]))
		amigo_list_4.place(x = 10,y = y_base + (28*3))
		# Amigo 5
		amigo_list_5 = ttk.Button(self, text = lista_amigos_usuario[4], width=50, command = lambda : commando(lista_amigos_usuario[4]))
		amigo_list_5.place(x = 10,y = y_base + (28*4))
		# Amigo 6
		amigo_list_6 = ttk.Button(self, text = lista_amigos_usuario[5], width=50, command = lambda : commando(lista_amigos_usuario[5]))
		amigo_list_6.place(x = 10,y = y_base + (28*5))
		# Amigo 7
		amigo_list_7 = ttk.Button(self, text = lista_amigos_usuario[6], width=50, command = lambda : commando(lista_amigos_usuario[6]))
		amigo_list_7.place(x = 10,y = y_base + (28*6))
		# Amigo 8
		amigo_list_8 = ttk.Button(self, text = lista_amigos_usuario[7], width=50, command = lambda : commando(lista_amigos_usuario[7]))
		amigo_list_8.place(x = 10,y = y_base + (28*7))
		# Amigo 9	
		amigo_list_9 = ttk.Button(self, text = lista_amigos_usuario[8], width=50, command = lambda : commando(lista_amigos_usuario[8]))
		amigo_list_9.place(x = 10,y = y_base + (28*8))
		# Amigo 10
		amigo_list_10 = ttk.Button(self, text = lista_amigos_usuario[9], width=50, command = lambda : commando(lista_amigos_usuario[9]))
		amigo_list_10.place(x = 10,y = y_base + (28*9))
  

		
		# botão para adicionar amigo
		button2 = ttk.Button(self, text ="Adicionar Amigo", command = lambda : controller.show_frame(adicionar_amigo))
		button2.place(x = 160,y = 610)
		setState()
   
# mostra a lista de receitas do usuario logado
class Perfil_usuario_receitas(tk.Frame):

	def __init__(self, parent, controller):
		def setState():
			label["text"] = usuario_buscado
			descricaolabel["text"] = descricao_amigo

			receita_list_1["text"] = lista_receitas[0]
			receita_list_2["text"] = lista_receitas[1]
			receita_list_3["text"] = lista_receitas[2]
			receita_list_4["text"] = lista_receitas[3]
			receita_list_5["text"] = lista_receitas[4]
			receita_list_6["text"] = lista_receitas[5]
			receita_list_7["text"] = lista_receitas[6]
			receita_list_8["text"] = lista_receitas[7]
			receita_list_9["text"] = lista_receitas[8]
			receita_list_10["text"] = lista_receitas[9]
			
			self.after(40, setState) # atualiza os widget 25 vezes por segundo
		def commando(receita):
			global ingredientes, modo_preparo, titulo_receita, garfadas
			if receita != "":
				titulo_receita = receita
				ingredientes, modo_preparo = get_receita.get_receita(usuario_buscado, receita)
				garfadas = get_garfadas.get_garfadas(usuario_buscado, receita)
				controller.show_frame(mostrar_receita)
    
		tk.Frame.__init__(self, parent)

		# botão para voltar a tela anterior
		button_voltar = ttk.Button(self, text ="Voltar", command = lambda : controller.show_frame(perfil_usuario))
		button_voltar.place(x = 340,y = 10)
		
		# Nome do usuario
		label = ttk.Label(self, text ="", font = MIDFONT)
		label.place(x = 10,y = 10)
  
		# Descrição do perfil
		descricaolabel = ttk.Label(self, text ="", font = MINFONT, justify=LEFT)
		descricaolabel.place(x = 8,y = 60)
  
		# lista de Receitas
		# Receita 1
		receita_list_1 = ttk.Button(self, text = lista_receitas[0], width=50, command = lambda : commando(lista_receitas[0]))
		receita_list_1.place(x = 10,y = 150 + (28*0))
		# Receita 2
		receita_list_2 = ttk.Button(self, text = lista_receitas[1], width=50, command = lambda : commando(lista_receitas[1]))
		receita_list_2.place(x = 10,y = 150 + (28*1))
		# Receita 3
		receita_list_3 = ttk.Button(self, text = lista_receitas[2], width=50, command = lambda : commando(lista_receitas[2]))
		receita_list_3.place(x = 10,y = 150 + (28*2))
		# Receita 4
		receita_list_4 = ttk.Button(self, text = lista_receitas[3], width=50, command = lambda : commando(lista_receitas[3]))
		receita_list_4.place(x = 10,y = 150 + (28*3))
		# Receita 5
		receita_list_5 = ttk.Button(self, text = lista_receitas[4], width=50, command = lambda : commando(lista_receitas[4]))
		receita_list_5.place(x = 10,y = 150 + (28*4))
		# Receita 6
		receita_list_6 = ttk.Button(self, text = lista_receitas[5], width=50, command = lambda : commando(lista_receitas[5]))
		receita_list_6.place(x = 10,y = 150 + (28*5))
		# Receita 7
		receita_list_7 = ttk.Button(self, text = lista_receitas[6], width=50, command = lambda : commando(lista_receitas[6]))
		receita_list_7.place(x = 10,y = 150 + (28*6))
		# Receita 8
		receita_list_8 = ttk.Button(self, text = lista_receitas[7], width=50, command = lambda : commando(lista_receitas[7]))
		receita_list_8.place(x = 10,y = 150 + (28*7))
		# Receita 9	
		receita_list_9 = ttk.Button(self, text = lista_receitas[8], width=50, command = lambda : commando(lista_receitas[8]))
		receita_list_9.place(x = 10,y = 150 + (28*8))
		# Receita 10
		receita_list_10 = ttk.Button(self, text = lista_receitas[9], width=50, command = lambda : commando(lista_receitas[9]))
		receita_list_10.place(x = 10,y = 150 + (28*9))
		
		# botão para adicionar receitas
		button2 = ttk.Button(self, text = "Adicionar Receita", command = lambda : controller.show_frame(adicionar_receita))
		button2.place(x = 160,y = 610)

		setState()

  
# Exibir perfil dos amigos
class Perfil_amigo(tk.Frame):

	def __init__(self, parent, controller):
		def setState():
			label["text"] = usuario_buscado
			descricaolabel["text"] = descricao_amigo

			receita_list_1["text"] = lista_receitas[0]
			receita_list_2["text"] = lista_receitas[1]
			receita_list_3["text"] = lista_receitas[2]
			receita_list_4["text"] = lista_receitas[3]
			receita_list_5["text"] = lista_receitas[4]
			receita_list_6["text"] = lista_receitas[5]
			receita_list_7["text"] = lista_receitas[6]
			receita_list_8["text"] = lista_receitas[7]
			receita_list_9["text"] = lista_receitas[8]
			receita_list_10["text"] = lista_receitas[9]
			
			self.after(40, setState) # atualiza os widget 25 vezes por segundo
		def commando(receita):
			global ingredientes, modo_preparo, titulo_receita, garfadas
			if receita != "":
				titulo_receita = receita
				ingredientes, modo_preparo = get_receita.get_receita(usuario_buscado, receita)
				garfadas = get_garfadas.get_garfadas(usuario_buscado, receita)
				controller.show_frame(mostrar_receita)
    
		tk.Frame.__init__(self, parent)

		# botão para voltar a tela anterior
		button_voltar = ttk.Button(self, text ="Voltar", command = lambda : controller.show_frame(perfil_usuario))
		button_voltar.place(x = 340,y = 10)
		
		# Nome do usuario
		label = ttk.Label(self, text ="", font = MIDFONT)
		label.place(x = 10,y = 10)
  
		# Descrição do perfil
		descricaolabel = ttk.Label(self, text ="", font = MINFONT, justify=LEFT)
		descricaolabel.place(x = 8,y = 60)
  
		# lista de Receitas
		# Receita 1
		receita_list_1 = ttk.Button(self, text = lista_receitas[0], width=50, command = lambda : commando(lista_receitas[0]))
		receita_list_1.place(x = 10,y = 150 + (28*0))
		# Receita 2
		receita_list_2 = ttk.Button(self, text = lista_receitas[1], width=50, command = lambda : commando(lista_receitas[1]))
		receita_list_2.place(x = 10,y = 150 + (28*1))
		# Receita 3
		receita_list_3 = ttk.Button(self, text = lista_receitas[2], width=50, command = lambda : commando(lista_receitas[2]))
		receita_list_3.place(x = 10,y = 150 + (28*2))
		# Receita 4
		receita_list_4 = ttk.Button(self, text = lista_receitas[3], width=50, command = lambda : commando(lista_receitas[3]))
		receita_list_4.place(x = 10,y = 150 + (28*3))
		# Receita 5
		receita_list_5 = ttk.Button(self, text = lista_receitas[4], width=50, command = lambda : commando(lista_receitas[4]))
		receita_list_5.place(x = 10,y = 150 + (28*4))
		# Receita 6
		receita_list_6 = ttk.Button(self, text = lista_receitas[5], width=50, command = lambda : commando(lista_receitas[5]))
		receita_list_6.place(x = 10,y = 150 + (28*5))
		# Receita 7
		receita_list_7 = ttk.Button(self, text = lista_receitas[6], width=50, command = lambda : commando(lista_receitas[6]))
		receita_list_7.place(x = 10,y = 150 + (28*6))
		# Receita 8
		receita_list_8 = ttk.Button(self, text = lista_receitas[7], width=50, command = lambda : commando(lista_receitas[7]))
		receita_list_8.place(x = 10,y = 150 + (28*7))
		# Receita 9	
		receita_list_9 = ttk.Button(self, text = lista_receitas[8], width=50, command = lambda : commando(lista_receitas[8]))
		receita_list_9.place(x = 10,y = 150 + (28*8))
		# Receita 10
		receita_list_10 = ttk.Button(self, text = lista_receitas[9], width=50, command = lambda : commando(lista_receitas[9]))
		receita_list_10.place(x = 10,y = 150 + (28*9))
		
		setState()

# Tela em que mostra a receita escolhida
class mostrar_receita(tk.Frame):
	def __init__(self, parent, controller):
		def setState():
			label["text"] = titulo_receita
			lista_ingredienteslabel["text"] = ingredientes
			label_preparo["text"] = modo_preparo
			button_garfadas["text"] = "Garfadas: " + garfadas

			self.after(40, setState) # atualiza os widget 25 vezes por segundo
   
		tk.Frame.__init__(self, parent)

		def atualizar_garfadas():
			global garfadas
   
			avaliar_receita.avaliar_receita(usuario_logado, usuario_buscado, titulo_receita)
			garfadas = get_garfadas.get_garfadas(usuario_buscado, titulo_receita)
			setState()
      
		# botão para voltar a tela anterior
		button_voltar = ttk.Button(self, text ="Voltar", command = lambda : controller.show_frame(Perfil_amigo))
		button_voltar.place(x = 340,y = 10)
  
		# Titulo da receita
		label = ttk.Label(self, text ="", font = MIDFONT)
		label.place(x = 10,y = 10)
  
		# Botão avaliar receita
		button_garfadas = ttk.Button(self, text ="", command = lambda : atualizar_garfadas())
		button_garfadas.place(x = 160,y = 610)
  
		# Ingredientes
		label_ingredientes = ttk.Label(self, text ="Ingredientes:", font = MIDFONT)
		label_ingredientes.place(x = 10,y = 70)
		
		# Lista de ingredientes
		lista_ingredienteslabel = ttk.Label(self, text ="", font = MINFONT)
		lista_ingredienteslabel.place(x = 10,y = 100)
   
   
		# Modo Preparo
		linha_inicio = 300 + 50
		label_ingredientes = ttk.Label(self, text ="Modo Preparo:", font = MIDFONT)
		label_ingredientes.place(x = 10,y = linha_inicio)

				
		label_preparo = ttk.Label(self, text ="", font = MINFONT)
		label_preparo.place(x = 10,y = linha_inicio + 30)
		setState()

class adicionar_receita(tk.Frame):
	

	def __init__(self, parent, controller):
		lista_ingredientes = [] # adicionar_receita
   
		def voltar():
			atualizaPerfil()
			controller.show_frame(Perfil_usuario_receitas)
   
		def atualizaPerfil():# atualiza os dados do perfil do usuario
			global usuario_buscado, lista_receitas, descricao_amigo 
			descricao_amigo, lista_receitas = buscar_perfil_amigo.requisitar_perfil_amigo(usuario_logado, usuario_logado)
   
		def salvar_receita():
			titulo = titulo_receita.get()
			preparo = modo_preparo.get(1.0, END)
			envio_receita.envio_receita(usuario_logado, titulo, lista_ingredientes, preparo)
			
			titulo_receita.set("")
			modo_preparo.delete("1.0","end")
			lista_ingredientes.clear()
			listar_ingredienetesLabel["text"] = ""
			
   
			atualizaPerfil()
			controller.show_frame(Perfil_usuario_receitas)

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
		button_voltar = ttk.Button(self, text ="Voltar", command = lambda : voltar())
		button_voltar.place(x = 340,y = 10)
  
		# Titulo da receita
		label = ttk.Label(self, text ="Adicionar Receita", font = MIDFONT)
		label.place(x = 10,y = 10)

  
		# Adicionar Titulo
		tituloLabel = Label(self, text="Titulo", font=("Arial", "14"))
		tituloLabel.place(x = 8,y = 60)
  
		conteiner_titulo = Frame(self)
		conteiner_titulo.place(x = 8,y = 88)

		titulo_receita=tk.StringVar()
		titulo = Entry(conteiner_titulo, textvariable = titulo_receita)
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
		button_salvar = ttk.Button(self, text ="Salvar Receita", command = lambda: salvar_receita())#lambda : controller.show_frame(Perfil_amigo))
		button_salvar.place(x = 160,y = 610)

class adicionar_amigo(tk.Frame):
	def __init__(self, parent, controller):
		def setState():
			label_resposta["text"] = ""

			self.after(10001, setState) # atualiza os widget 25 vezes por segundo
   
   
		def adicionarAmigo():
			global descricao_usuario, lista_amigos_usuario
			if nome.get() != "" and nome.get() != usuario_logado:
				resposta = add_amigo.add_amigo(usuario_logado, nome.get())		
				if resposta == "adicionado":
					descricao_usuario, lista_amigos_usuario = buscar_perfil_proprio.requisitar_perfil_proprio(usuario_logado)
					controller.show_frame(perfil_usuario)
				else:
					label_resposta["text"] = resposta
			
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

		label_resposta = Label(self, text="", font=("Arial", "10"), justify=LEFT)
		label_resposta.place(x = 8,y = 150)
   

		

		# botão para adicionar a receita
		button_buscar = ttk.Button(self, text ="Adicionar Amigo", command = lambda : adicionarAmigo())
		button_buscar.place(x = 160,y = 610)
		setState()
    
# Driver Code
app = tkinterApp()
app.title("Vó Maria")
app.geometry("430x650")
app.tk.call('tk', 'scaling', 2.0)
app.mainloop()

