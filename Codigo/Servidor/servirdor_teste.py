import socket
import pickle

import os
os.system('clear') or None

lista_usuarios = {'mario': 1,
          'BatmanCozineiro':1,
          'padeiro32': 1,
          'marcos': 1,
          'CangacoCozineiro': 1,
          'MestreDiarreia': 1,
          'animalDaCozinha': 1}

senhas = {'mario': 123,
          'BatmanCozineiro':123,
          'padeiro32': 123,
          'marcos': 123,
          'CangacoCozineiro': 132,
          'MestreDiarreia': 123,
          'animalDaCozinha': 123}

amigos = {'mario': "|BatmanCozineiro|padeiro32|CangacoCozineiro|MestreDiarreia|animalDaCozinha|marcos",
          'BatmanCozineiro': "|mario|padeiro32|CangacoCozineiro|MestreDiarreia|animalDaCozinha|marcos",
          'padeiro32': "|BatmanCozineiro|mario|CangacoCozineiro|MestreDiarreia|animalDaCozinha|marcos",
          'marcos':"|BatmanCozineiro|padeiro32|CangacoCozineiro|MestreDiarreia|animalDaCozinha|mario",
          'animalDaCozinha': "|BatmanCozineiro|padeiro32|CangacoCozineiro|MestreDiarreia|mario",
          'MestreDiarreia': "|BatmanCozineiro|padeiro32|CangacoCozineiro|animalDaCozinha|mario"}

receitas = {'mario': "|Bacalhau com limao|Bolo de sardinha|Carangueijo com quiabo|Feijoada de frando|Angu com laranja",
            'BatmanCozineiro': "|Bacalhau com limao|Bolo de sardinha|Carangueijo com quiabo|Feijoada de frando|Angu com laranja",
            'padeiro32': "|Bacalhau com limao|Bolo de sardinha|Carangueijo com quiabo|Feijoada de frando|Angu com laranja",
            'marcos': "|Bacalhau com limao|Bolo de sardinha|Carangueijo com quiabo|Feijoada de frando|Angu com laranja",
            'CangacoCozineiro': "|Bacalhau com limao|Bolo de sardinha|Carangueijo com quiabo|Feijoada de frando|Angu com laranja",
            'MestreDiarreia': "|Bacalhau com limao|Bolo de sardinha|Carangueijo com quiabo|Feijoada de frando|Angu com laranja",
            'animalDaCozinha': "|Bacalhau com limao|Bolo de sardinha|Carangueijo com quiabo|Feijoada de frando|Angu com laranja"}

descricoes = {'mario': "Meu nome e mario, tenho 150 anos e estudo computacao desde quando inventaram o computador e ate hoje nao sei nada. Meu shonho e formar.",
              'BatmanCozineiro': "Defendo gotan nas horas vagas e trabalho em uma padaria durante o dia.",
              'padeiro32': "Sou o trigesimo segundo padeiro da minha vila, meu sonho e me tornar o maior padeiro de todos os tempo e dominar todas as outras vilas.",
              'marcos': "Descricao com 65 caracteres, e apos cada 65 caracteres eu faco a quebra de linha pra poder ir pra a proxima linha. Descricao com 65 caracteres, e apos cada 65 caracteres eu faco a quebra de linha pra poder ir pra a proxima linha. Descricao com 65 caracteres.",
              'CangacoCozineiro': "OI",
              'animalDaCozinha': "Falo!!!!!!",
              'MestreDiarreia': "Gororoba do mais alto nivel!"}

receitas_preparo = {'Bacalhau_com_limao': "1kg de bacalhau|10 litros de vinagre]" + " joga tudo na panela e torce pra dar certo.]",
                    'Bolo_de_sardinha': "1kg de sardinha|10 litros de vinagre]" + " joga tudo na panela e torce pra dar certo.]",
                    'Carangueijo_com_quiabo': "1kg de carangueijo|10 litros de vinagre]" + " joga tudo na panela e torce pra dar certo.]",
                    'Feijoada_de_frando': "1kg de Feijao|10 litros de vinagre]" + " joga tudo na panela e torce pra dar certo.]",
                    'Angu_com_laranja': "1kg de laranja|10 litros de vinagre]" + " joga tudo na panela e torce pra dar certo.]"}

garfadas = {'Bacalhau_com_limao': 10,
            'Bolo_de_sardinha': 8,
            'Carangueijo_com_quiabo': 17,
            'Feijoada_de_frando': 8000,
            'Angu_com_laranja': 21}
    
    
    
    
def server(host = 'localhost', port=8082):    
    print(dict)
    print()
    print()
    data_payload = 2048 #The maximum amount of data to be received at once
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    # Enable reuse address/port 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print ("Iniciando servidor de Teste: %s porta %s" % server_address)
    print()
    print("##########################################################################")
    sock.bind(server_address)
    # Listen to clients, argument specifies the max no. of queued connections
    sock.listen(5) 
    i = 0
    while True: 
        print()
        print ("Esperando mensagem do cliente!")
        print()
        client, address = sock.accept() 
        data = client.recv(data_payload) 
        resposta = "Opção invalida!" # Resposta padrão caso não tenha a opção
        if data:
            print ("Mensagem recebida: %s" %data)
            requisicao = split_mensagem(data)
            
            if requisicao[0] == "0": # requisição de login
                resposta = requisicao_login(data)
            
            if requisicao[0] == "1": # requisição para adicionar receitas 
                resposta = requisicao_adicionar_receita(data)
            
            if requisicao[0] == "2": # requisição para adicionar um amigo 
                resposta = requisicao_adicionar_amigo(data)
            
            if requisicao[0] == "3": # requisição para buscar o perfil de um usuario
                resposta = requisicao_buscar_perfil_amigo(data)
            
            if requisicao[0] == "4": # requisição para buscar o perfil proprio
                resposta = requisicao_perfil_proprio(data)
                
            if requisicao[0] == "5": # requisição para buscar o perfil proprio
                resposta = requisicao_get_receita(data)
                
            if requisicao[0] == "6": # requisição para buscar o perfil proprio
                resposta = requisicao_garfada(data)

            client.send(resposta.encode("ascii"))
            print ("Mensagem enviada %s bytes back to %s" % (resposta, address))       
            print("##########################################################################")  

def decodificar_mensagem(mensagem):
    '''Recebe a mensagem em bytes e a converte para string
       :param mensagem: mensagem recebida do cliente no formarto de bytes
       :return: mensagem convertida para string'''
    
    encoding = 'utf-8' # pretendo converter para string
    return str(mensagem, encoding) # converte a mensagem recebida de byte para string   

def split_mensagem(data):
    '''Recebe a mensagem enviada pelo cliente e converte para string e depois envia uma lista com as palavras separadas por espaço.
       :param data: mensagem enviada pelo cliente
       :return: lista de strings, cada string é uma palavra que foi separada por espaço'''
       
    mensagem = decodificar_mensagem(data)
    return mensagem.split(" ")# gera uma lista separando as strings pelo espaço


########################## Requisições dos Clientes ########################## 
# pronto
def requisicao_login(data):
    '''Verifica se o nome de usuario existe e se a senha esta correta.
       :param data: mensagem enviada pelo cliente
       :return: retorna True se o nome e a senha estiverem corretos, caso contrario False
    '''
    valid = False
    lista = split_mensagem(data)
    nome = lista[1] # nome recebido
    senha = lista[2] # senha recebida    
    
    senha_real = str(senhas.get(nome))    

    if senha_real != None: # usuario exite, logo a senha existe. Mas a senha esta certa?
        if senha_real == senha:
            valid = True
    return str(valid)
    
def requisicao_adicionar_receita(data):   
    '''Adiciona uma nova receita ao banco de dados do usuario.
       :param data: mensagem recebida com o nome do usuairo que esta adicionando a receita
                    e a receita que sera adicionada
        :return: true caso tenha sido salva com sucesso ou false caso contrario'''
         
    valid = True
    lista = split_mensagem(data)
    nome = lista[1]
    receita = lista[2]
    for i in range(3, len(lista)): # monta novamente a receita      
        receita += " " + lista[i]
    
    print("usuario: " + nome)
    print()
    print("Receita: " + receita)
    
    return str(valid)

#pronto
def requisicao_adicionar_amigo(data):
    '''Adiciona um novo amigo a lista de amigos do usuario.
       :param data: mensagem recebido do cliente, contmdo o nomeo do usuario que ira adicionar o amigo e o nome do amigo.
       :return true caso seja adicionado com sucesso e false caso contrario.'''
       
    valid = "Usuario nao encontrado!"
    lista = split_mensagem(data)
    usuario = lista[1]
    nome_amigo = lista[2]
    
    if lista_usuarios.get(nome_amigo) != None: # verifica se o amigo existe no banco de dados
        valid = nome_amigo + " adicionado a lista de amigos do usuario: " + usuario

    return valid
    
# pronto
def requisicao_perfil_proprio(data):
    lista = split_mensagem(data)
    usuario = lista[1] #Dono do perfil
    
    resposta = "vazio" # resposta padrão
    descrisao = descricoes.get(usuario)
    lista_amigos = amigos.get(usuario)
        
    # verifica se ele existe no banco de dados
    resposta = descrisao + " " + lista_amigos
    
    return resposta
       
# pronto      
def requisicao_buscar_perfil_amigo(data):   
    lista = split_mensagem(data)
    usuario = lista[1] 
    usuario_buscado = lista[2]
    resposta = "vazio" # resposta padrão
    
     
    
    if e_amigo(usuario, usuario_buscado): #verifica se o usuario buscado é amigo do que esta buscando ele
        # deve retornar uma string: descricao nome_receita_1 nome_receita_2 nome_receita_3  
        descrisao = descricoes.get(usuario_buscado)
        lista_receitas = receitas.get(usuario_buscado) 
        
        # verifica se o amigo exite no banco de dados
        resposta = descrisao + " " + lista_receitas        
    return resposta

def requisicao_garfada(data):
    resposta = False # resposta padrão
    lista = split_mensagem(data)
    usuario = lista[1] 
    usuario_avaliado = lista[2]
    
    nome_receita = ""
    for i in range(3, len(lista)):
        nome_receita += " " + lista[i]
        
    print("receita: " + nome_receita + " do usuario: " + usuario_avaliado + " Foi avaliada pelo usuario: " + usuario)
    resposta = True
    
    
    return str(resposta)

# pronto
def requisicao_get_receita(data):
    resposta = "" # resposta padrão
    lista = split_mensagem(data)
    dono_receita = lista[1]
    nome_receita = lista[2]
    for i in range(3, len(lista)):
        nome_receita += " " + lista[i]
    
    receita = receitas_preparo.get(nome_receita.replace(" ", "_"))
    print(receita)
    if receita != None:
        resposta = receita
        
    return resposta

def e_amigo(usuario, usuario_buscado):
    return True

server()
