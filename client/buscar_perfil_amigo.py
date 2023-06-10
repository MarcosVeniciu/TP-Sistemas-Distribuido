import cliente

def requisitar_perfil_amigo(usuario, perfil):
    '''Busca o perfil de um usuario, retornarndo o nome, descriçao e lista de receitas.
    :param usuario: nome do usuario que esta fazendo a requisição.
    :param perfil: nome do usuario que deseja se obter o dados de perfil.
    :return: Perfil do amigo'''
    
    usuario = max(usuario.split(" "))# remove os espaços em branco caso tenha
    perfil = max(perfil.split(" "))# remove os espaços em branco caso tenha
    requisicao = "3 " + usuario + " " + perfil
    resposta = cliente.requisicao(requisicao)
    descricao = get_descricao(resposta)
    lista_receitas = get_lista_receitas(resposta)
    
    return descricao, lista_receitas

def get_descricao(resposta):
    descricao = ""
    for caractere in resposta:
        if caractere != "|":
            descricao += caractere
        else:
            break
    
    descricao = formatar_descricao(descricao)
    return descricao

def formatar_descricao(descricao):
    linha = ""
    for i in range(len(descricao)):
        if i == 65 or i == 130 or i == 195:
           linha +=  "\n" + descricao[i]  if descricao[i] != " " else "\n" 
        else:
            linha += descricao[i]
    
    return linha 
            
def get_lista_receitas(resposta):
    lista_receitas = []                                                                                           
    lista = resposta.split("|")[1:]
    
    for pessoa in lista:
        lista_receitas.append(pessoa)
    
    for i in range(10 - len(lista_receitas)):
        lista_receitas.append("")
    
    return lista_receitas
    
# Teste
#nome = input("Nome: ")
#amigo = input("Nome do amigo: ")
#desc, amigo = requisitar_perfil_amigo(nome, amigo)
#print(amigo)
#print()
#print(desc)