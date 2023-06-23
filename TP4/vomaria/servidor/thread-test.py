import Pyro5.api
from threading import Thread

@Pyro5.api.expose
class MeuObjetoRemoto(object):
    def devolve_42(self):
        em_uso = None
        while 1:
            em_uso = True
            #funcao()
            em_uso = False
            
    def infinito(self):
        while True:
            # Realize as operações necessárias aqui
            pass

# Inicialize o servidor Pyro5
Pyro5.api.init()

# Crie uma instância da classe do objeto remoto
objeto_remoto = MeuObjetoRemoto()

# Registre o objeto remoto com o nome no servidor Pyro5
daemon = Pyro5.api.Daemon()
uri = daemon.register(objeto_remoto)
nameserver = Pyro5.api.locate_ns()
nameserver.register("meu_objeto_remoto", uri)

# Inicie uma thread para executar o servidor Pyro5
thread = Thread(target=daemon.requestLoop)
thread.daemon = True
thread.start()

# Agora o servidor Pyro5 está em execução e pronto para receber solicitações dos clientes