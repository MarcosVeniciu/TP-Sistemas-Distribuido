import cliente

def get_garfadas(dono_receita, receita):
    dono_receita = max(dono_receita.split(" "))# remove os espaços em branco caso tenha
    
    requisicao = "7 " + dono_receita + " " + ajustar_titulo(receita)
    return cliente.requisicao(requisicao)


def ajustar_titulo(titulo):
    return titulo.replace(" ", "_")