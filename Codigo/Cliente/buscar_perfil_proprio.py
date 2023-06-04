import cliente

def requisitar_perfil_proprio(usuario):
    '''Busca o perfil do proprio usuario, ele deve retornar o nome,
       lista de receitas e lista de amigos e a quantidade de receitas de cada amigo.
    :param usuario: nome do usuario que esta fazendo a requisição.
    :param perfil: nome do usuario que deseja se obter o dados de perfil.
    :return: Perfil do amigo ou do proprio usuario'''
    
    usuario = max(usuario.split(" "))# remove os espaços em branco caso tenha
    requisicao = "4 " + usuario
    return cliente.requisicao(requisicao)


# Teste
#nome = input("Nome: ")
#sesult = requisitar_perfil_proprio(nome)
#print(sesult)