import cliente

def requisitar_perfil_proprio(usuario):
    '''Busca o perfil do proprio usuario, ele deve retornar a
       lista de receitas e lista de amigos.
    :param usuario: nome do usuario que esta fazendo a requisição.
    :return: Perfil do amigo ou do proprio usuario'''
    
    usuario = max(usuario.split(" "))# remove os espaços em branco caso tenha
    requisicao = "4 " + usuario
    resposta = cliente.requisicao(requisicao)
    descricao = get_descricao(resposta)
    lista_amigos = get_lista_amigos(resposta)
    
    return descricao, lista_amigos


# Meu nome e mario, tenho 150 anos e estudo computacao desde quando inventaram o computador e ate hoje nao sei nada. Meu shonho e formar.
# Meu nome e mario, tenho 150 anos e estudo computacao desde quando
# inventaram o computador e ate hoje nao sei nada. Meu shonho e for


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
            
def get_lista_amigos(resposta):
    lista_amigos = []                                                                                           
    lista = resposta.split("|")[1:] # Pega tudo que esta da descrição em diante 

    for pessoa in lista:
        lista_amigos.append(pessoa)
    
    for i in range(10 - len(lista_amigos)):
        lista_amigos.append("")

    return lista_amigos
    
    
# Teste
#nome = "marcos"
#desc, amigo = requisitar_perfil_proprio(nome)
#print(amigo)
#print()
#print(desc)
