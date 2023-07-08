import Pyro5.api

# Classe do objeto remoto
class MeuObjetoRemoto:
    def __init__(self):
        self.nome = "mario"
        self.descricao = "Eu tenho 120 anos"
        self.lista_amigos = ["batman", "robin", "diarreiaCozinheiro", "SubmundoCulinaria"]
        self.lista_receitas = ["bacalhau com limão", "suco de goiaba"]
        self.titulo = "Receita de bacalhau"
        self.lista_ingredientes = ["bacalhau", "agua", "vinagre"]
        self.modo_preparo = "Joga tudo na panela e torce pra dar certo!"
        self.garfadas = 15
        
        
    @Pyro5.api.expose 
    def get_nome(self):
        return self.nome

    @Pyro5.api.expose 
    def get_descricao(self):
        return self.descricao

    @Pyro5.api.expose 
    def get_lista_amigos(self):
        return self.lista_amigos
    
    @Pyro5.api.expose 
    def get_lista_receitas(self):
        return self.lista_receitas
    
    @Pyro5.api.expose 
    def get_titulo(self):
        return self.titulo
    
    @Pyro5.api.expose 
    def get_lista_ingredientes(self):
        return self.lista_ingredientes
    
    @Pyro5.api.expose 
    def get_modo_preparo(self):
        return self.modo_preparo
    
    @Pyro5.api.expose 
    def get_garfadas(self):
        return self.garfadas
    
    @Pyro5.api.expose 
    def set_garfadas(self):
        self.garfadas += 1
    
    @Pyro5.api.expose 
    def add_amigo(self, usuario, name):
        self.lista_amigos.append(name)
        return "adicionado"
    
    @Pyro5.api.expose 
    def add_receita(self, usuario, receita_name, ingredientes, modo_preparo):
        self.titulo = receita_name
        self.lista_ingredientes = ingredientes
        self.modo_preparo = modo_preparo
        self.lista_receitas.append(receita_name)
    
if __name__ == '__main__':
    daemon = Pyro5.api.Daemon()

    objeto_remoto = MeuObjetoRemoto()
    uri = daemon.register(objeto_remoto)


    ns = Pyro5.api.locate_ns()


    ns.register("servidor", uri) 


    print("Servidor aguardando conexões...")
    daemon.requestLoop()
