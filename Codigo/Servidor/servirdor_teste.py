import socket
import pickle
import requisicoes
import os
from threading import *   
 
requisisao_id = -1 
lista_requisicoes = [] # lista contendo as threads de cada requisiçao


def server(host = 'localhost', port=8082):    
    global requisisao_id
    
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
            requisicao = requisicoes.split_mensagem(data)
            
            if requisicao[0] == "0": # requisição de login
                Thread_obj = Thread(target=requisicoes.requisicao_login, args=(data,))  
                Thread_obj.start()
                lista_requisicoes.append(Thread_obj)
                requisisao_id += 1
            
            if requisicao[0] == "1": # requisição para adicionar receitas
                Thread_obj = Thread(target=requisicoes.requisicao_adicionar_receita, args=(data,))  
                Thread_obj.start()
                lista_requisicoes.append(Thread_obj) 
                requisisao_id += 1
                #resposta = requisicoes.requisicao_adicionar_receita(data)
            
            if requisicao[0] == "2": # requisição para adicionar um amigo 
                Thread_obj = Thread(target=requisicoes.requisicao_adicionar_amigo, args=(data,))  
                Thread_obj.start()
                lista_requisicoes.append(Thread_obj) 
                requisisao_id += 1
                #resposta = requisicoes.requisicao_adicionar_amigo(data)
            
            if requisicao[0] == "3": # requisição para buscar o perfil de um usuario
                Thread_obj = Thread(target=requisicoes.requisicao_buscar_perfil_amigo, args=(data,))  
                Thread_obj.start()
                lista_requisicoes.append(Thread_obj) 
                requisisao_id += 1
                #resposta = requisicoes.requisicao_buscar_perfil_amigo(data)
            
            if requisicao[0] == "4": # requisição para buscar o perfil proprio
                Thread_obj = Thread(target=requisicoes.requisicao_perfil_proprio, args=(data,))  
                Thread_obj.start()
                lista_requisicoes.append(Thread_obj)
                requisisao_id += 1 
                #resposta = requisicoes.requisicao_perfil_proprio(data)
                
            if requisicao[0] == "5": # requisição para buscar o perfil proprio
                Thread_obj = Thread(target=requisicoes.requisicao_get_receita, args=(data,))  
                Thread_obj.start()
                lista_requisicoes.append(Thread_obj) 
                requisisao_id += 1
                #resposta = requisicoes.requisicao_get_receita(data)
                
            if requisicao[0] == "6": # requisição para buscar o perfil proprio
                Thread_obj = Thread(target=requisicoes.requisicao_add_garfada, args=(data,))  
                Thread_obj.start()
                lista_requisicoes.append(Thread_obj) 
                requisisao_id += 1
                #resposta = requisicoes.requisicao_add_garfada(data)
            
            if requisicao[0] == "7": # requisição para buscar o numero de garfadas na receita
                Thread_obj = Thread(target=requisicoes.requisicao_get_garfada, args=(data,))  
                Thread_obj.start()
                lista_requisicoes.append(Thread_obj) 
                requisisao_id += 1
                #resposta = requisicoes.requisicao_get_garfada(data) 
                
            #if len(requisicoes.database.lista_respostas) > 0:
            print(requisisao_id)
            print(len(requisicoes.database.lista_respostas))
            
            resposta = requisicoes.database.lista_respostas[requisisao_id]
            client.send(resposta.encode("ascii"))
            #requisicoes.database.lista_respostas.pop(0)
            print ("Mensagem enviada %s bytes back to %s" % (resposta, address))       
            print("##########################################################################")  




    return True
os.system('clear') or None
server()
