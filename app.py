from flask import Flask, render_template

app = Flask("hello")

@app.route("/") #rotas 
@app.route("/hello") #rotas 
def hello():
    return "Hello word carai"

@app.route("/meucontato")
def meuContato():
    return render_template('indexcontato.html')

