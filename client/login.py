import cliente

def logar(nome, senha):
    ''' Para logar no sistema, o usuario devera informar o nome e a senha.
        Se o nome de usuario exitir no banco de dados e a senha esitver correta o login sera validado
        :param nome: nome do usuario
        :param senha: senha do usuario
        
        :return: True se o nome e senha estiver certo e False caso contrario'''
    nome = max(nome.split(" "))# remove os espaços em branco caso tenha
    senha = max(senha.split(" "))# remove os espaços em branco caso tenha
    
    requisisao = "0 " + nome + " " + senha
    return cliente.requisicao(requisisao)



# Teste
#nome = input("Nome: ")
#senha = input("senha: ")
#sesult = logar(nome, senha)
#print(sesult)