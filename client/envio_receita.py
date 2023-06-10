import cliente

def envio_receita(nome, nome_receita, ingredientes, preparo):
    '''Envia uma receita para ser salva no servidor.
       :param nome: nome do usuario ques esta adicionando a receita.
       :param nome_receita: nome da receita.
       :param ingredientes: lista de ingredientes.
       :param preparo: modo de preparo da receita
       :return: True se tiver sido salvo com sucesso e False caso contrario.'''
    if len(nome_receita) <= 1:
        print("Voce precisa informar um nome!")
        return False

    if len(ingredientes) <= 1:
        print("Voce precisa informar os ingredientes!")
        return False
    
    if len(preparo) <= 1:
        print("Voce precisa informar o modo de reparo!")
        return False
        
    nome = max(nome.split(" "))# remove os espaços em branco caso tenha
    titulo = ajustar_titulo(nome_receita)
    ingredientes = ajsutar_lista_ingredientes(ingredientes)
    requisicao = "1 " + nome + " " + titulo + " " + ingredientes + preparo
    print(requisicao)
    return cliente.requisicao(requisicao)

def ajustar_titulo(titulo):
    return titulo.replace(" ", "_")

def ajsutar_lista_ingredientes(ingredientes):
    lista_ingredientes = ingredientes[0]
    for ingrediente in ingredientes[1:]:
        lista_ingredientes += "|" + ingrediente
    
    lista_ingredientes += "]"
    return lista_ingredientes

# Teste
#nome = input("Nome: ")
#print("Escreva a sua receita: ")
#nome_receita = input("Nome: ")
#ingredientes = input("ingredientes: ")
#preparo = input("preparo: ")
#sesult = envio_receita(nome, nome_receita, ingredientes, preparo)
#print(sesult)