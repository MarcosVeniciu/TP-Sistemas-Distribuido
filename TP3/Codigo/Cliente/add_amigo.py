import cliente

def add_amigo(usuario, nome_amigo):
    usuario = max(usuario.split(" "))# remove os espaços em branco caso tenha
    nome_amigo = max(nome_amigo.split(" "))# remove os espaços em branco caso tenha
    requisicao = "2 " + usuario + " " + nome_amigo
    return cliente.requisicao(requisicao) 
    
    

# Teste
#nome = input("Nome: ")
#amigo = input("Nome do amigo: ")
#sesult = add_amigo(nome, amigo)
#print(sesult)