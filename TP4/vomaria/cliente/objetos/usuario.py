import Pyro5.api

class Usuario:
    '''
    O objeto usuario, possui todos os atributos do usuario, e devera busca os dados no servidor quando
    o objeto é criado e quando a lista de amigos ou a lista de receitas forem alteradas, ja que o nome
    e a descrisão não iram mudar.   
    '''
    def __init__(self):
        '''
        Monta o objeto usuario
        '''
   
        self.nome = "" 
        self.descricao = ""
        self.lista_amigos = []
        self.lista_receita = []
    
    def get_usuario(self):
        '''
        Monta o objeto usuario, buscando os seus atributos no servidor
        '''
        objeto_remoto = self.get_objeto_remoto()
        
        self.nome = objeto_remoto.get_nome() 
        self.descricao = objeto_remoto.get_descricao()
        self.lista_amigos = objeto_remoto.get_lista_amigos()
        self.lista_receita = objeto_remoto.get_lista_receitas()
        
    def get_objeto_remoto(self):
        # Obtém uma referência ao objeto remoto registrado no Name Server
        uri = Pyro5.api.locate_ns().lookup("servidor")
        return Pyro5.api.Proxy(uri)
    
    def _update_lista_amigos(self):
        '''
        Quando é adicionado um novo amigo, a lista de amigos é atualizada, então deve buscar no servidor a nova lista.
        '''
        objeto_remoto = self.get_objeto_remoto()
        self.lista_amigos = objeto_remoto.get_lista_amigos()
               
    def _update_lista_receitas(self):
        '''
        Quando uma receita é adicionada, a lista de receita deve ser atualizada.
        '''
        objeto_remoto = self.get_objeto_remoto()
        self.lista_receita = objeto_remoto.get_lista_receitas()
    
    def get_nome(self):
        '''
        Retorna o nome do usuario logado.
        '''
        return self.nome
    
    def get_descricao(self):
        '''
        Retorna a descrição do perfil do usuario logado.
        '''
        return self.descricao
    
    def get_lista_amigos(self):
        '''
        Retorna a lisa de amigos do usuario logado.
        '''
        return self.lista_amigos
    
    def get_lista_receitas(self):
        '''
        Retorna a lista com o nome das receitas do usuario logado.
        '''
        return self.lista_receita
    
    def add_amigo(self, usuario, name):
        '''
        Envia a requisição para adicionar amigo a lista de amigos do usuario logado.
        '''
        resposta = "Usuario, não encontrado!"
        objeto_remoto = self.get_objeto_remoto()
        resposta = objeto_remoto.add_amigo(usuario, name)
        self._update_lista_amigos()
        return resposta
    
    def add_receita(self, usuario, receita_name, ingredientes, modo_preparo):
        '''
        Envia a requisição para adicionar um receita na lista de receitas do usuario logado.
        '''
        objeto_remoto = self.get_objeto_remoto()
        objeto_remoto.add_receita(usuario, receita_name, ingredientes, modo_preparo)
        self._update_lista_receitas()
    
    