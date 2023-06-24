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
        
        self.descricao = objeto_remoto.get_user_description(self.nome)
        self.lista_amigos = objeto_remoto.get_friends(self.nome)
        self.lista_receita = objeto_remoto.get_recipes(self.nome)
        
    def get_objeto_remoto(self):
        # Obtém uma referência ao objeto remoto registrado no Name Server
        uri = Pyro5.api.locate_ns().lookup("servidor")
        return Pyro5.api.Proxy(uri)
    
    def _update_lista_amigos(self):
        '''
        Quando é adicionado um novo amigo, a lista de amigos é atualizada, então deve buscar no servidor a nova lista.
        '''
        objeto_remoto = self.get_objeto_remoto()
        self.lista_amigos = objeto_remoto.get_friends(self.n)
               
    def _update_lista_receitas(self):
        '''
        Quando uma receita é adicionada, a lista de receita deve ser atualizada.
        '''
        objeto_remoto = self.get_objeto_remoto()
        self.lista_receita = objeto_remoto.get_recipes(self.nome)
    
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
        res = objeto_remoto.follow_user(usuario, name)
        if res:
            self._update_lista_amigos()
            resposta = res
        return resposta
    
    def add_receita(self, usuario, receita_name, ingredientes, modo_preparo):
        '''
        Envia a requisição para adicionar um receita na lista de receitas do usuario logado.
        '''
        objeto_remoto = self.get_objeto_remoto()
        objeto_remoto.add_recipe(usuario, receita_name, ingredientes, modo_preparo)
        self._update_lista_receitas()
    
    def logar(self, nome, senha):
        objeto_remoto = self.get_objeto_remoto()
        if objeto_remoto.login(nome, senha):
            self.nome = nome
            self.senha = senha
            self.get_usuario()
            return True
        return False