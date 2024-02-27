from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def homepage():
  return 'Página inicial'

@app.route('/contatos')
def contatos():
  return 'Página de contatos'

@app.route('/pegarvendas')
def pegarvendas():
  tabela = pd.read_csv('advertising.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)

app.run(host='0.0.0.0')

