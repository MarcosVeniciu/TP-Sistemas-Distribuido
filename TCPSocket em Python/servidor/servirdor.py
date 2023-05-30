import socket
import pickle

def server(host = 'localhost', port=8082):
    dict = {'A': 1, 'B': 2, 'C': 3}
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
    print ("Iniciando servidor  na %s porta %s" % server_address)
    print()
    print()
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
        if data:
            encoding = 'utf-8' # pretendo converter para string
            s = str(data, encoding) # converte de byte para string
            valor = str(dict.get(s))
            print ("Mensagem recebida: %s" %data)
            valor = valor.encode("ascii")
            client.send(valor)
            print ("Mensagem enviada %s bytes back to %s" % (valor, address))
            # end connection limitado a 3
            #client.close()
            #i+=1
            #if i>=3: break           
server()
