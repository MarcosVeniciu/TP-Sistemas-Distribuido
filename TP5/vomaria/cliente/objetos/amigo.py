import Pyro5.api

class Amigo():
    def __init__(self):
        self.nome = ""
        self.descricao = ""
        self.lista_receitas = []
    
    def get_objeto_remoto(self):
        # Obtém uma referência ao objeto remoto registrado no Name Server
        uri = Pyro5.api.locate_ns().lookup("servidor")
        return Pyro5.api.Proxy(uri)
    
    def get_amigo(self, username):
        '''
        Monta o objeto amigo, buscando os seus atributos no servidor
        '''
        objeto_remoto = self.get_objeto_remoto()
        
        self.nome = username
        self.descricao = objeto_remoto.get_user_description(username)
        self.lista_receita = objeto_remoto.get_recipes(username)
        
    def get_nome(self):
        '''
        Retorna o nome do amigo que foi buscado.
        '''
        return self.nome
    
    def get_descrisao(self):
        '''
        Retorna a descricão do amigo que foi buscado no servidor.
        '''
        return self.descricao
    
    def get_lista_receitas(self):
        '''
        Retorna a lista de receitas do usuario buscado.
        '''
        return self.lista_receita