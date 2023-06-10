import socket
import pickle
from models import *
from repository import *
from service import *
from queries import *
dict = {'A': 1, 'B': 2, 'C': 3, 'marcos': 26}

class Server:
    def __init__(self) -> None:
        pass
    

    def server(self, host = 'localhost', port=8082):    
        data_payload = 2048 

        sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_address = (host, port)
    
        sock.bind(server_address)

        sock.listen(5) 
        while True: 
            client, address = sock.accept() 
            data = client.recv(data_payload) 
            resposta = "Opção invalida!" 
            if data:
                print ("Mensagem recebida: %s" %data)
                requisicao = self.split_mensagem(data)
                
                if requisicao[0] == "0": 
                    resposta = self.requisicao_login(data)
                
                if requisicao[0] == "1": 
                    resposta = self.requisicao_adicionar_receita(data)
                
                if requisicao[0] == "2": 
                    resposta = self.requisicao_adicionar_amigo(data)
                
                if requisicao[0] == "3": 
                    resposta = self.requisicao_buscar_perfil_amigo(data)
                
                if requisicao[0] == "4": 
                    resposta = self.requisicao_perfil_proprio(data)
                    
                if requisicao[0] == "5": 
                    resposta = self.requisicao_get_receita(data)
                    
                if requisicao[0] == "6": 
                    resposta = self.requisicao_garfada(data)

                client.send(resposta.encode("ascii"))
                

    def decodificar_mensagem(self, mensagem):
        '''Recebe a mensagem em bytes e a converte para string
        :param mensagem: mensagem recebida do cliente no formarto de bytes
        :return: mensagem convertida para string'''
        
        encoding = 'utf-8' # pretendo converter para string
        return str(mensagem, encoding) # converte a mensagem recebida de byte para string   

    def split_mensagem(self, data):
        '''Recebe a mensagem enviada pelo cliente e converte para string e depois envia uma lista com as palavras separadas por espaço.
        :param data: mensagem enviada pelo cliente
        :return: lista de strings, cada string é uma palavra que foi separada por espaço'''
        
        mensagem = self.decodificar_mensagem(data)
        return mensagem.split(" ")# gera uma lista separando as strings pelo espaço


    ########################## Requisições dos Clientes ########################## 
    def requisicao_login(self, data):
        '''Verifica se o nome de usuario existe e se a senha esta correta.
        :param data: mensagem enviada pelo cliente
        :return: retorna True se o nome e a senha estiverem corretos, caso contrario False
        '''
        
        user_service = UserService()
        
        lista = self.split_mensagem(data)
        nome = lista[1]
        senha = lista[2]    
        
        return str(user_service.login(nome, senha))
        
    def requisicao_adicionar_receita(self, data):   
        '''Adiciona uma nova receita ao banco de dados do usuario.
        :param data: mensagem recebida com o nome do usuairo que esta adicionando a receita
                        e a receita que sera adicionada
            :return: true caso tenha sido salva com sucesso ou false caso contrario'''
        lista = self.split_mensagem(data)
        user_name = lista[1] # nome do usuario que vai adicionar a receita
        titulo = lista[2] # titulo da receita
        
        receita = lista[3]
        for partes in lista[4:]:
            receita += " " + partes
            
        recipe_service = RecipeService()
    
        # print("usuario: " + nome)
        # print()
        # print("Receita: " + receita)
        
        return str(recipe_service.add(user_name, titulo, receita))
        
    def requisicao_adicionar_amigo(self, data):
        '''Adiciona um novo amigo a lista de amigos do usuario.
        :param data: mensagem recebido do cliente, contmdo o nomeo do usuario que ira adicionar o amigo e o nome do amigo.
        :return true caso seja adicionado com sucesso e false caso contrario.'''
        relation_service = RelationshipService()
        valid = None
        lista = self.split_mensagem(data)
        
        usuario = lista[1]
        nome_amigo = lista[2]
        if relation_service.add(usuario, nome_amigo):
            valid = "adicionado"
        else:
            valid = "Usuario nao encontrado!"
            
        return valid
        
    def requisicao_perfil_proprio(self, data):
        lista = self.split_mensagem(data)
        usuario = lista[1] #Dono do perfil
        
        user_repo = UserRepository()
        relation_repo = RelationshipRepository()
        
        usr = user_repo.find_user_by_username(usuario)
        friends = relation_repo.find(usr[0])
        
        resposta = "vazio" # resposta padrão
        descrisao = usr[3]
        amigos = "|"
        
        for friend in friends:
            amigos += str(friend[4])
            amigos += "|"
            
        # verifica se ele existe no banco de dados
        resposta = descrisao + " " + amigos
    
        return resposta
        
    def requisicao_buscar_perfil_amigo(self, data):   
        lista = self.split_mensagem(data)
        usuario = lista[1] 
        usuario_buscado = lista[2]
        resposta = "vazio" # resposta padrão
        relation_repo = RelationshipRepository()
        user_uuid = user_repo.find_user_by_username(usuario)[0]
        friends = relation_repo.find(user_uuid)
        
        recipe_repo = RecipeRepository()
        recipes = recipe_repo.find_by_user_uuid(user_uuid)
        is_friend = False
        descricao = ""
        for friend in friends:
            if friend[4] == usuario_buscado:
                is_friend = True
                descricao = friend[6]
                break
            
            # verifica se o amigo exite no banco de dados
        resposta = descricao + " " 
        for recipe in recipes:
            resposta += "|" + recipe[1]
        return resposta

    def requisicao_garfada(self, data):
        resposta = False # resposta padrão
        lista = self.split_mensagem(data)
        usuario = lista[1] 
        usuario_avaliado = lista[2]
        
        
        
        nome_receita = ""
        for i in range(3, len(lista)):
            nome_receita += " " + lista[i]
            
        print("receita: " + nome_receita + " do usuario: " + usuario_avaliado + " Foi avaliada pelo usuario: " + usuario)
        resposta = True
        
        
        return str(resposta)

    def requisicao_get_receita(self,data):
        resposta = "" # resposta padrão
        lista = self.split_mensagem(data)
        dono_receita = lista[1]
        nome_receita = lista[2]
        
        for i in range(3, len(lista)):
            nome_receita += " " + lista[i]
        
        recipe_repo = RecipeRepository()
        receita = recipe_repo.find_by_name(nome_receita)
        

            
        if receita != None:
        resposta = receita
        
    return resposta
    
if __name__ == "__main__":
    server = Server()
    server.server()


