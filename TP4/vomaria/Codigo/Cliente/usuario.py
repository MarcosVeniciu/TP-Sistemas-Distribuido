class Usuario:
    '''
    O objeto usuario, possui todos os atributos do usuario, e devera busca os dados no servidor quando
    o objeto é criado e quando a lista de amigos ou a lista de receitas forem alteradas, ja que o nome
    e a descrisão não iram mudar.   
    '''
    def __init__(self):
        '''
        Monta o objeto usuario, buscando os seus atributos no servidor
        '''
        #objeto_remoto = clitente()
        self.nome = "Mario" 
        self.descricao = "Eu tenho 120 anos"
        self.lista_amigos = ["batman", "robin", "diarreiaCozinheiro", "SubmundoCulinaria"]
        self.lista_receita = ["bacalhau com limão", "suco de goiaba"]
    
        
    def _update_lista_amigos():
        '''
        Quando é adicionado um novo amigo, a lista de amigos é atualizada, então deve buscar no servidor a nova lista.
        '''
        ...
        
    def _update_lista_receitas():
        '''
        Quando uma receita é adicionada, a lista de receita deve ser atualizada.
        '''
        ...
    
    def get_nome():
        '''
        Retorna o nome do usuario logado.
        '''
        ...
    
    def get_descricao():
        '''
        Retorna a descrição do perfil do usuario logado.
        '''
        ...
    
    def get_lista_amigos():
        '''
        Retorna a lisa de amigos do usuario logado.
        '''
        ...
    
    def get_lista_receitas():
        '''
        Retorna a lista com o nome das receitas do usuario logado.
        '''
        ...
    
    def add_amigo(self):
        '''
        Envia a requisição para adicionar amigo a lista de amigos do usuario logado.
        '''
        self._update_lista_amigos()
    
    def add_receita(self):
        '''
        Envia a requisição para adicionar um receita na lista de receitas do usuario logado.
        '''
        self._update_lista_receitas()
    
    