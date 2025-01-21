from flask import Flask,render_template


app = Flask(__name__)


@app.route('/inicio')
def ola():
    lista_jogos= ['fallout 4','skyrim','kenshi']
    return render_template('Lista.html', titulo='jogos', jogos=lista_jogos)

app.run()


# # trecho da app
# app.run(host='0.0.0.0', port=8080)