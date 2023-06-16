import Pyro5.api

# Classe do objeto remoto
class MeuObjetoRemoto:
    @Pyro5.api.expose # permite acessar o metodo remotamente, precisa coloca-lo sobre todos os metodos de acesso remoto
    def adicionar(self, a, b):
        return a + b

# Inicializa o servidor Pyro5
daemon = Pyro5.api.Daemon()

# Registra o objeto remoto no servidor Pyro5
objeto_remoto = MeuObjetoRemoto()
uri = daemon.register(objeto_remoto)

# Obtém uma referência ao Name Server
ns = Pyro5.api.locate_ns()

# Registra a URI do objeto remoto no Name Server
ns.register("servidor", uri) # registra o name server como servidor

# Inicia o servidor Pyro5
print("Servidor aguardando conexões...")
daemon.requestLoop()
