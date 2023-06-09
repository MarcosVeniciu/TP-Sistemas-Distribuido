import cliente

def envio_receita(nome, nome_receita, ingredientes, preparo):
    '''Envia uma receita para ser salva no servidor.
       :param nome: nome do usuario ques esta adicionando a receita.
       :param receita: receita a ser adiociinada no banco de dados.
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
    
    requisicao = "1 " + nome + " " + "[" + nome_receita + "]" + "[" + ingredientes + "]" + "[" + preparo + "]"
    return cliente.requisicao(requisicao)



# Teste
nome = input("Nome: ")
print("Escreva a sua receita: ")
nome_receita = input("Nome: ")
ingredientes = input("ingredientes: ")
preparo = input("preparo: ")
sesult = envio_receita(nome, nome_receita, ingredientes, preparo)
print(sesult)