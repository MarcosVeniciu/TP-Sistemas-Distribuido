import database


def decodificar_mensagem(mensagem):
    '''Recebe a mensagem em bytes e a converte para string
       :param mensagem: mensagem recebida do cliente no formarto de bytes
       :return: mensagem convertida para string'''
    
    encoding = 'utf-8' # pretendo converter para string
    return str(mensagem, encoding) # converte a mensagem recebida de byte para string   



def split_mensagem(data):
    '''Recebe a mensagem enviada pelo cliente e converte para string e depois envia uma lista com as palavras separadas por espaço.
       :param data: mensagem enviada pelo cliente
       :return: lista de strings, cada string é uma palavra que foi separada por espaço'''
       
    mensagem = decodificar_mensagem(data)
    return mensagem.split(" ")# gera uma lista separando as strings pelo espaço


########################## Requisições dos Clientes ########################## 
# pronto
def requisicao_login(data):
    '''Verifica se o nome de usuario existe e se a senha esta correta.
       :param data: mensagem enviada pelo cliente
       :return: retorna True se o nome e a senha estiverem corretos, caso contrario False
    '''
    valid = False
    lista = split_mensagem(data)
    nome = lista[1] # nome recebido
    senha = lista[2] # senha recebida    
    
    senha_real = str(database.senhas.get(nome))    

    if senha_real != None: # usuario exite, logo a senha existe. Mas a senha esta certa?
        if senha_real == senha:
            valid = True
    database.lista_respostas.append(str(valid))
    #return str(valid)

# pronto
def requisicao_adicionar_receita(data):   
    '''Adiciona uma nova receita ao banco de dados do usuario.
       :param data: mensagem recebida com o nome do usuairo que esta adicionando a receita
                    e a receita que sera adicionada
        :return: true caso tenha sido salva com sucesso ou false caso contrario'''
    # "1 " + nome + " " + titulo + " " + ingredientes + preparo
    
    valid = True
    lista = split_mensagem(data)
    nome = lista[1] # nome do usuario que vai adicionar a receita
    titulo_receita = lista[2] # titulo da receita
    
    receita = lista[3]
    for partes in lista[4:]:
        receita += " " + partes
    
    database.receitas_preparo[titulo_receita] = receita
    
    receitas_salvas = database.receitas.get(nome)
    receitas_salvas += "|" + titulo_receita.replace("_", " ")
    database.receitas[nome] = receitas_salvas
    database.garfadas[titulo_receita] = 0
    
    print("usuario: " + nome)
    print()
    print("Titulo da receita: " + titulo_receita)
    print()
    print("Modo de Preparo: " + receita)
    #return str(valid)
    print("adicionado")
    database.lista_respostas.append(str(valid))

#pronto
def requisicao_adicionar_amigo(data):
    '''Adiciona um novo amigo a lista de amigos do usuario.
       :param data: mensagem recebido do cliente, contmdo o nomeo do usuario que ira adicionar o amigo e o nome do amigo.
       :return true caso seja adicionado com sucesso e false caso contrario.'''
       
    valid = "Usuario nao encontrado!"
    lista = split_mensagem(data)
    usuario = lista[1]
    nome_amigo = lista[2]
    
    if database.lista_usuarios.get(nome_amigo) != None: # verifica se o amigo existe no banco de dados
        print("\n" + nome_amigo + " adicionado a lista de amigos do usuario: " + usuario + "\n")
        valid = "adicionado"

    #return valid
    database.lista_respostas.append(valid)
    
# pronto
def requisicao_perfil_proprio(data):
    lista = split_mensagem(data)
    usuario = lista[1] #Dono do perfil
    
    resposta = "vazio" # resposta padrão
    descrisao = database.descricoes.get(usuario)
    lista_amigos = database.amigos.get(usuario)
        
    # verifica se ele existe no banco de dados
    resposta = descrisao + " " + lista_amigos
    
    #return resposta
    database.lista_respostas.append(resposta)
       
# pronto      
def requisicao_buscar_perfil_amigo(data):   
    lista = split_mensagem(data)
    usuario = lista[1] 
    usuario_buscado = lista[2]
    resposta = "vazio" # resposta padrão
    
     
    
    if e_amigo(usuario, usuario_buscado): #verifica se o usuario buscado é amigo do que esta buscando ele
        # deve retornar uma string: descricao nome_receita_1 nome_receita_2 nome_receita_3  
        descrisao = database.descricoes.get(usuario_buscado)
        lista_receitas = database.receitas.get(usuario_buscado) 
        
        # verifica se o amigo exite no banco de dados
        resposta = descrisao + " " + lista_receitas        
    #return resposta
    database.lista_respostas.append(resposta)

# pronto
def requisicao_get_garfada(data):
    mensagem = split_mensagem(data)
    dono_receita = mensagem[1]
    receita = mensagem[2]
    
    #return str(database.garfadas.get(receita))
    database.lista_respostas.append(str(database.garfadas.get(receita)))
    
def requisicao_add_garfada(data):
    valid = False
    lista = split_mensagem(data)  
    
    usuario_avaliador = lista[1]
    usuario_avaliado = lista[2]
    receita_avaliada = lista[3]
    
    qtd_garfadas = database.garfadas.get(receita_avaliada)
    database.garfadas[receita_avaliada] = qtd_garfadas +1
      
    print("receita: " + receita_avaliada + " do usuario: " + usuario_avaliado + ". Foi avaliada pelo usuario: " + usuario_avaliador)
    resposta = True
    
    
    #return str(valid)
    database.lista_respostas.append(str(valid))

# pronto
def requisicao_get_receita(data):
    resposta = "" # resposta padrão
    lista = split_mensagem(data)
    dono_receita = lista[1]
    nome_receita = lista[2]
    for i in range(3, len(lista)):
        nome_receita += " " + lista[i]
    
    receita = database.receitas_preparo.get(nome_receita.replace(" ", "_"))
    print(receita)
    if receita != None:
        resposta = receita
        
    #return resposta
    database.lista_respostas.append(resposta)

def e_amigo(usuario, usuario_buscado):
    return True