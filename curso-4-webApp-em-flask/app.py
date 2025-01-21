from flask import Flask,render_template,request


class Jogo:
    def __init__(self,nome,categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Fallout 4', 'sobrevivencia', 'PC')
jogo2 = Jogo('Kenshi','RPG','PC')
jogo3 = Jogo('Valorant','fps online','PC')
    
lista_jogos= [jogo1,jogo2,jogo3]


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Lista.html', titulo='jogos', jogos=lista_jogos)

@app.route('/novo')

def novo():
    return render_template('novo.html',titulo='jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista_jogos.append(jogo)
    return render_template('lista.html',titulo='jogos', jogos=lista_jogos)

app.run(debug=True)


# # trecho da app
# app.run(host='0.0.0.0', port=8080)


