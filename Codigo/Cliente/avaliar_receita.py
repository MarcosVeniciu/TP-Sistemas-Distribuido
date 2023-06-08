import cliente

def avaliar_receita(usuario, avaliado, nome_receita):
    usuario = max(usuario.split(" "))# remove os espaços em branco caso tenha
    avaliado = max(avaliado.split(" "))# remove os espaços em branco caso tenha
    
    requisicao = "6 " + usuario + " " + avaliado + " " + ajustar_titulo(nome_receita)
    return cliente.requisicao(requisicao)

def ajustar_titulo(titulo):
    return titulo.replace(" ", "_")

# Teste
#usuario = input("Nome: ")
#avaliado = input("avaliado: ")
#nome_receita = input("receita: ")
#sesult = avaliar_receita(usuario, avaliado, nome_receita)
#print(sesult)