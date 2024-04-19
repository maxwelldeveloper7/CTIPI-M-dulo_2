from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loja_online.db'
db = SQLAlchemy(app)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade_estoque = db.Column(db.Integer, nullable=False, default=0)


@app.route('/adicionar_produto', methods=['GET', 'POST'])
def adicionar_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])
        quantidade_estoque = int(request.form['quantidade_estoque'])
        novo_produto = Produto(nome=nome, preco=preco, quantidade_estoque=quantidade_estoque)
        db.create_all()
        db.session.add(novo_produto)
        db.session.commit()
        return redirect(url_for('listar_produtos'))
    return render_template('adicionar_produto.html')

@app.route('/produtos')
def listar_produtos():
    produtos = Produto.query.all()
    return render_template('produtos.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)