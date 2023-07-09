from flask import Flask

calories_100g = {"arroz": 500, "fermento biologico" : 50, 
                 "creme de leite": 70, "ovos": 400, "batata": 300,
                 "oleo": 170, "queijo parmesao": 230, 
                 "polvilho doce": 103, "pimenta do reino": 114,
                 }

app = Flask(__name__)

@app.route('/hello/<string:ingrediente>/<int:quantidade>')
def calorias(ingrediente, quantidade):
    return str(calories_100g[str.lower(ingrediente)] * quantidade / 100)

# link de teste: http://127.0.0.1:5000/hello/John/25
# pode mudar o nome john e a idade 25 

# site de refeencia
# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
