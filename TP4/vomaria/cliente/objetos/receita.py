import Pyro5.api


class Receita():
    def __init__(self):        
        self.titulo = ""
        self.lista_ingredientes = []
        self.modo_preparo = ""
        self.garfadas = 0
    
    def get_objeto_remoto(self):
        # Obtém uma referência ao objeto remoto registrado no Name Server
        uri = Pyro5.api.locate_ns().lookup("servidor")
        return Pyro5.api.Proxy(uri)
    
    def get_receita(self):
        '''
        Monta o objeto receita, buscando os seus atributos no servidor
        '''
        objeto_remoto = self.get_objeto_remoto()
        
        self.titulo = objeto_remoto.get_titulo() 
        self.lista_ingredientes = objeto_remoto.get_lista_ingredientes()
        self.modo_preparo = objeto_remoto.get_modo_preparo()
        self.garfadas = objeto_remoto.get_garfadas()
        
    def get_titulo(self):
        '''
        Retorna o titulo da receita.
        '''
        return self.titulo
        
    def get_lista_ingredientes(self):
        '''
        Retorna a lista de ingredientes da receita
        '''
        texto = ""
        for ingrediente in self.lista_ingredientes:
            texto += "- " + ingrediente + "\n"
            
        return texto
    
    def get_modo_preparo(self):
        '''
        Retorna a string com o modo de preparo da receita.
        '''
        return self.modo_preparo
        
    def get_garfadas(self):
        '''
        Retorna o numero de garfadas da receita.
        '''
        return self.garfadas
    
    def set_garfada(self):
        '''
        Envia para o servidor a requisição de adicionar uma garfada a uma receita avaliada pelo usuario logado.
        '''
        self.objeto_remoto = self.get_objeto_remoto()
        self.objeto_remoto.set_garfadas()
        self._update_garfadas()
    
    
    def _update_garfadas(self):
        '''
        Busca no srevidor o numero de garfadas que a receita tem, caso a quantidade de garfadas tenha sido alterada.
        '''
        self.objeto_remoto = self.get_objeto_remoto()
        self.garfadas = self.objeto_remoto.get_garfadas()
        