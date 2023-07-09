# Obter o diretório atual
CURRENT_DIR := $(shell pwd)

# Instalar as dependências do requirements.txt
install:
	gnome-terminal --tab --title="Install Requirements" -- bash -c "source bin/activate && pip install -r requirements.txt; read -p 'Pressione Enter para sair...'"

# Instalar as dependências no sistema operacional
run_dependencies:
	sudo apt-get install -y python3-tk
	sudo apt-get install -y libsqlite3-dev

# Executar os scripts em terminais separados no Linux
run:
	gnome-terminal --tab --title="API Flask" --working-directory="$(CURRENT_DIR)/web_service" -- bash -c " \
		export FLASK_APP=calorias; \
		export FLASK_ENV=development; \
		source ../bin/activate; \
		flask run; \
		read -p 'Pressione Enter para sair...'"
	gnome-terminal --tab --title="Name Server" -- bash -c "source bin/activate && pyro5-ns"
	gnome-terminal --tab --title="Servidor" --working-directory="$(CURRENT_DIR)/servidor" -- bash -c "source ../bin/activate && python3 rmi.py; read -p 'Pressione Enter para sair...'"
	gnome-terminal --tab --title="Cliente" -- bash -c "source bin/activate && python3 cliente/main.py; read -p 'Pressione Enter para sair...'"

.PHONY: install run_dependencies run
