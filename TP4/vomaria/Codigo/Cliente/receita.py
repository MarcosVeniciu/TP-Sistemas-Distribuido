    
class Receita():
    def __init__(self):        
        self.titulo = "receita de bacalhau"
        self.lista_ingredientes = ["bacalhau", "vinagre"]
        self.modo_preparo = "joga tudo na panela e torce pra dar certo"
        self.garfadas = 12
    
    def get_titulo():
        '''
        Retorna o titulo da receita.
        '''
        ...
        
    def get_lista_ingredientes():
        '''
        Retorna a lista de ingredientes da receita
        '''
        ...
    
    def get_modo_preparo():
        '''
        Retorna a string com o modo de preparo da receita.
        '''
        ...
        
    def get_garfadas():
        '''
        Retorna o numero de garfadas da receita.
        '''
        ...
    
    def set_garfada(self):
        '''
        Envia para o servidor a requisição de adicionar uma garfada a uma receita avaliada pelo usuario logado.
        '''
        self._update_garfadas()
    
    
    def _update_garfadas():
        '''
        Busca no srevidor o numero de garfadas que a receita tem, caso a quantidade de garfadas tenha sido alterada.
        '''
        ...