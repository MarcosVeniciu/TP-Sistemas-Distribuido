import cliente

def requisitar_perfil_amigo(usuario, perfil):
    '''Busca o perfil de um usuario, retornarndo o nome, descriçao e lista de receitas.
    :param usuario: nome do usuario que esta fazendo a requisição.
    :param perfil: nome do usuario que deseja se obter o dados de perfil.
    :return: Perfil do amigo'''
    
    usuario = max(usuario.split(" "))# remove os espaços em branco caso tenha
    perfil = max(perfil.split(" "))# remove os espaços em branco caso tenha
    requisicao = "3 " + usuario + " " + perfil
    return cliente.requisicao(requisicao)



def get_nome(mensagem):
    lista = mensagem.split(" ")
    return lista[0]

def get_strings(mensagem):
    lista_palavras = []
    
    lista = mensagem.split(" ")
    # marcos [asda asa as] [asas]
    for i in range(0, len(lista)): # percorre toda a lista
      descricao = ""
      palavra = lista[i]
      if palavra[0] == "[": # inicio de uma descricao ou do nome de uma receita
        descricao += " " + palavra[1:]
      i += 1
      palavra = lista[i]
      while palavra[len(palavra)-1] != "]": # ate chegar na palavra que termina com um ]
          descricao += " " + palavra
          lista_palavras += descricao     
    
    return descricao
    
# Teste
nome = input("Nome: ")
amigo = input("Nome do amigo: ")
sesult = requisitar_perfil_amigo(nome, amigo)
print(sesult)