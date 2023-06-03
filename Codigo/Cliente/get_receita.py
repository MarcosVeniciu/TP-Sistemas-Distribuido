import cliente

def get_receita(usuario, dono_receita, nome_receita):
    usuario = max(usuario.split(" "))# remove os espaços em branco caso tenha
    dono_receita = max(dono_receita.split(" "))# remove os espaços em branco caso tenha
    
    requisicao = "5 " + usuario + " " + dono_receita + " " + nome_receita
    return cliente.requisicao(requisicao)

# Teste
usuario = input("Nome: ")
avaliado = input("avaliado: ")
nome_receita = input("receita: ")
sesult = get_receita(usuario, avaliado, nome_receita)
print(sesult)