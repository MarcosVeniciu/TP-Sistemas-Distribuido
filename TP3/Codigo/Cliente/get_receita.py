import cliente

def get_receita(dono_receita, nome_receita):
    dono_receita = max(dono_receita.split(" "))# remove os espaços em branco caso tenha
    
    requisicao = "5 " + dono_receita + " " + nome_receita
    
    resposta = cliente.requisicao(requisicao)
    lista_ingredientes = getingredientes(resposta)
    modo_preparo = getModoPreparo(resposta)
    return lista_ingredientes, modo_preparo

# Bacalhau com limao]1kg de bacalhau|10 litros de vinagre] joga tudo na panela e torce pra dar certo.]
# removi o nome da resposta do servidor e o primeiro conchete


def getingredientes(resposta):
    ingredientes = resposta.split("]")
    lista_ingredientes = ingredientes[0].split("|")
    return listaToString(lista_ingredientes)

def getModoPreparo(resposta):
    modo_preparo = resposta.split("]")[1]
    return formatar_preparo(modo_preparo) 

def listaToString(mensagem):
    lista_ingredientes = ""
    for ingrediente in mensagem:
        lista_ingredientes += "- " + ingrediente + "\n"
    return lista_ingredientes

def formatar_preparo(mensagem):
    linha = ""
    for i in range(len(mensagem)):
        if i == 65 or i == 130 or i == 195:
           linha +=  "\n" + mensagem[i]  if mensagem[i] != " " else "\n" 
        else:
            linha += mensagem[i]
    
    return linha 



# Teste
#dono_receita = "mario"
#nome_receita = "Bacalhau com limao"
#ingredientes, modo_preparo = get_receita(dono_receita, nome_receita)
#print(ingredientes)
#print("########")
#print(modo_preparo)