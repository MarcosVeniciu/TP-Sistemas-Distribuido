import Pyro5.api

# Obtém uma referência ao objeto remoto registrado no Name Server
uri = Pyro5.api.locate_ns().lookup("servidor")
objeto_remoto = Pyro5.api.Proxy(uri)

# Chama o método remoto do objeto
resultado = objeto_remoto.adicionar(3, 4)
print("Resultado:", resultado)
