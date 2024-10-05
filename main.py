from flask import Flask, render_template, request, redirect
from database import executar_comando, consultar_comando
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

#FUNCIONALIDADE 1 - Cadastramento de chamados -> tabela chamados_suporte
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome_cliente = request.form['nome_cliente']
        descricao_problema = request.form['descricao_problema']
        data_abertura = date.today()
        status = 'aberto'
        
        comando = "INSERT INTO chamados_suporte (nome_cliente, descricao_problema, data_abertura, status) VALUES (%s, %s, %s, %s)"
        dados = (nome_cliente, descricao_problema, data_abertura, status)
        executar_comando(comando, dados)
        
        return redirect('/')
    return render_template('cadastrar.html')

#FUNCIONALIDADE 2 - Atualização da tabela chamados_suporte
@app.route('/atualizar', methods=['GET', 'POST'])
def atualizar():
    if request.method == 'POST':
        nome_cliente = request.form['nome_cliente']
        data_abertura = request.form['data_abertura']
        novo_status = request.form['status']
        descricao_problema = request.form['descricao_problema']

        comando = "UPDATE chamados_suporte SET status = %s, descricao_problema = %s WHERE nome_cliente = %s AND data_abertura = %s"
        dados = (novo_status, descricao_problema, nome_cliente, data_abertura)
        executar_comando(comando, dados)

        return redirect('/')
    return render_template('atualizar.html')

@app.route('/excluir', methods=['GET', 'POST'])
def excluir():
    if request.method == 'POST':
        nome_cliente = request.form['nome_cliente']
        data_abertura = request.form['data_abertura']
        
        comando = "DELETE FROM chamados_suporte WHERE nome_cliente = %s AND data_abertura = %s"
        dados = (nome_cliente, data_abertura)
        executar_comando(comando, dados)

        return redirect('/')
    return render_template('excluir.html')

@app.route('/reabrir', methods=['GET', 'POST'])
def reabrir():
    if request.method == 'POST':
        nome_cliente = request.form['nome_cliente']
        data_abertura = request.form['data_abertura']
        
        comando = "UPDATE chamados_suporte SET status = 'aberto' WHERE nome_cliente = %s AND data_abertura = %s AND status = 'resolvido'"
        dados = (nome_cliente, data_abertura)
        executar_comando(comando, dados)

        return redirect('/')
    return render_template('reabrir.html')

if __name__ == '__main__':
    app.run(debug=True)
