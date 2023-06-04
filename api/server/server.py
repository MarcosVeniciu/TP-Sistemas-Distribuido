import socket
import pickle

dict = {'A': 1, 'B': 2, 'C': 3, 'marcos': 26}

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
def requisicao_login(data):
    '''Verifica se o nome de usuario existe e se a senha esta correta.
       :param data: mensagem enviada pelo cliente
       :return: retorna True se o nome e a senha estiverem corretos, caso contrario False
    '''
    valid = False
    lista = split_mensagem(data)
    nome = lista[1]
    senha = lista[2]    
    
    senha_real = dict.get(nome)
    if  senha_real != None: # usuario exite, logo a senha existe. Mas a senha esta certa?
        if str(senha_real) == senha:
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
    
def requisicao_adicionar_amigo(data):
    '''Adiciona um novo amigo a lista de amigos do usuario.
       :param data: mensagem recebido do cliente, contmdo o nomeo do usuario que ira adicionar o amigo e o nome do amigo.
       :return true caso seja adicionado com sucesso e false caso contrario.'''
       
    valid = False
    lista = split_mensagem(data)
    usuario = lista[1]
    nome_amigo = lista[2]
    
    if dict.get(nome_amigo) != None: # verifica se o amigo existe no banco de dados
        print("nome adicionado a lista de amigos do usuario: " + usuario)
        valid = True

    return str(valid)
    
def requisicao_perfil_proprio(data):
    lista = split_mensagem(data)
    usuario = lista[1]
    
    resposta = "vazio" # resposta padrão
    descrisao = "[Tenho 157 anos, e estou na faculdade a 117]"
    
    # deve retornar uma string: usuario descricao amigo_1:nun_receita amigo_2:nun_receita
    
    # verifica se ele existe no banco de dados
    resposta = usuario + " " + descrisao + " " + "[A:123] " + "[B:6] " + "[C:55] "
    
    return resposta
       
def requisicao_buscar_perfil_amigo(data):   
    lista = split_mensagem(data)
    usuario = lista[1] 
    usuario_buscado = lista[2]
    resposta = "vazio" # resposta padrão
    
    if e_amigo(usuario, usuario_buscado): #verifica se o usuario buscado é amigo do que esta buscando ele
        # deve retornar uma string: usuario descricao nome_receita_1 nome_receita_2 nome_receita_3  
        descrisao = "[Tenho 157 anos, e estou na faculdade a 117]"
        
        # verifica se o amigo exite no banco de dados
        resposta = usuario_buscado + " " + descrisao + " " + " [receita de bacalhau] " + " [receita de frango frito]" # O nome das receutas ficam entre os []
        
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

def requisicao_get_receita(data):
    resposta = "" # resposta padrão
    lista = split_mensagem(data)
    usuario = lista[1] 
    usuario_avaliado = lista[2]
    
    nome_receita = ""
    for i in range(3, len(lista)):
        nome_receita += " " + lista[i]
        
    resposta = "[Receita de bacalhau] " + " [1kg de manteiga, 10 litros de vinagre]" + " [joga tudo na panela e torce pra dar certo.]"
    
    return resposta

def e_amigo(usuario, usuario_buscado):
    return True

server()
