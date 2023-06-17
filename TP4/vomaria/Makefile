# Instalar as dependências do requirements.txt
install:
	gnome-terminal --tab --title="Install Reqirements" -- bash -c "source bin/activate && pip install -r reqirements.txt; read -p 'Pressione Enter para sair...'"

# Executar os scripts em terminais separados no linux
run:
	gnome-terminal --tab --title="Name Server" -- bash -c "source bin/activate && pyro5-ns"
	gnome-terminal --tab --title="Servidor" -- bash -c "source bin/activate && python3 servidor/servidor.py; read -p 'Pressione Enter para sair...'"
	gnome-terminal --tab --title="Cliente" -- bash -c "source bin/activate && python3 cliente/main.py; read -p 'Pressione Enter para sair...'"

# Executar os scripts em terminais separados no macOS
run-mac:
	osascript -e 'tell application "Terminal" to do script "cd $(PWD) && source vomaria/bin/activate && pyro5-ns"'
	osascript -e 'tell application "Terminal" to do script "cd $(PWD) && source vomaria/bin/activate && python cliente/main.py"'
	osascript -e 'tell application "Terminal" to do script "cd $(PWD) && source vomaria/bin/activate && python servidor/servidor.py"'

.PHONY: activate install run run-mac
