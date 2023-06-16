# Ativar o ambiente virtual
activate:
	. vomaria/bin/activate

# Instalar as dependências do requirements.txt
install:
	pip install -r requirements.txt

# Executar os scripts em terminais separados
run:
	gnome-terminal --tab --title="Script 1" -- bash -c "source vomaria/bin/activate && python vomaria/Codigo/Cliente/main.py"
	gnome-terminal --tab --title="Script 2" -- bash -c "source vomaria/bin/activate && python vomaria/Codigo/Servidor/servirdor_teste.py"

# Executar os scripts em terminais separados no macOS
run-mac:
	osascript -e 'tell application "Terminal" to do script "cd $(PWD) && source vomaria/bin/activate && python vomaria/Codigo/Cliente/main.py"'
	osascript -e 'tell application "Terminal" to do script "cd $(PWD) && source vomaria/bin/activate && python vomaria/Codigo/Servidor/servidor_teste.py"'


.PHONY: activate install run run-mac
