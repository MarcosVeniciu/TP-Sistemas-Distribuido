from flask import Flask
import datetime


app = Flask(__name__)

@app.route('/hello/<string:ingrediente>/<int:quantidade>')
def calorias(ingrediente, quantidade):
    print(ingrediente)
    print(quantidade)
    print()
    #hora_atual = f"Olá, usario {ingrediente} de {quantidade} anos! A hora atual é: " + str(datetime.datetime.now())
    return "100"


# link de teste: http://127.0.0.1:5000/hello/John/25
# pode mudar o nome john e a idade 25 
