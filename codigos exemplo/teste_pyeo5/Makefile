# Ativar o ambiente virtual
activate:
	. vomaria/bin/activate

# Instalar as dependências do requirements.txt
install:
	pip install -r requirements.txt

# Executar os scripts em terminais separados
run:
	gnome-terminal --tab --title="Name Server" -- bash -c "source vomaria/bin/activate && pyro5-ns"
	gnome-terminal --tab --title="Servidor" -- bash -c "source vomaria/bin/activate && python vomaria/servidor.py" 
	gnome-terminal --tab --title="Cliente" -- bash -c "source vomaria/bin/activate && python vomaria/cliente.py; exec bash"
	 
.PHONY: activate install run-server run-cliente
