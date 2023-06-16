import socket


def conect(host = 'localhost', port=8082): 
    ''' Conecta ao servidor usando o IP local como ip do servidor'''
    
    # Create a TCP/IP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connect the socket to the server 
    server_address = (host, port) 
    print ("Connecting to %s port %s" % server_address) 
    sock.connect(server_address) 
    return sock
    

def mensagem_decoding(mensagem):
    ''' Decodifica a mensagem recebida de bytes para string'''
    
    encoding = 'utf-8' # pretendo converter para string
    return str(mensagem, encoding) # converte de byte para string

def requisicao(message):
    resposta = "False"
    sock = conect()
    try: 
        # Send data 
        print ("Mensagem enviada: %s" % message) 
        sock.sendall(message.encode('utf-8')) 
      
        # Look for the response 
        amount_expected = 100000 # tamanho maximo da string a ser recebida
        
        data = sock.recv(amount_expected) 

        resposta = mensagem_decoding(data)
        #print ("Mensagem recebida: " + resposta) 

    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
    finally: 
        print()
        print ("Encerrando conecxão com o servidor!") 
        sock.close() 
        
    return resposta