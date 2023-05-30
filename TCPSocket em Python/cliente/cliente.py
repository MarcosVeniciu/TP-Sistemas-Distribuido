import socket


def client(host = 'localhost', port=8082): 
    # Create a TCP/IP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connect the socket to the server 
    server_address = (host, port) 
    print ("Connecting to %s port %s" % server_address) 
    sock.connect(server_address) 
    # Send data 
    try: 
        # Send data 
        message = "B" 
        print ("Mensagem enviada: %s" % message) 
        sock.sendall(message.encode('utf-8')) 
        # Look for the response 
        amount_received = 0 
        amount_expected = len(message) 
        
        data = sock.recv(amount_expected) 

	
        #print("Tipo de dado recebido: " + str(type(data))) # verifico o tipo de dado que recebo
        encoding = 'utf-8' # pretendo converter para string
        s = str(data, encoding) # converte de byte para string
        print ("Mensagem recebida: " + s) 
        #while amount_received < amount_expected: 
        #    data = sock.recv(16) 
        #    amount_received += len(data) 
        #    print ("Received: %s" % data) 
    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
    finally: 
        print()
        print ("Encerrando conecxão com o servidor!") 
        sock.close() 

client()
