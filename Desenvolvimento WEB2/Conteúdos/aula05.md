**Semana 9-10: Banco de Dados e SQLAlchemy**

Nesta semana, mergulharemos no emocionante mundo dos bancos de dados em aplicações web com Python. Veremos como integrar bancos de dados em nossos projetos Flask usando SQLAlchemy, uma poderosa biblioteca de mapeamento objeto-relacional (ORM) que simplifica o acesso e manipulação de dados.

**1. Introdução aos Bancos de Dados**

Antes de começarmos a trabalhar com bancos de dados em nossas aplicações Flask, é importante entender os conceitos básicos dos bancos de dados relacionais e como eles são utilizados no contexto do desenvolvimento web.

**2. Configuração do Banco de Dados**

Vamos configurar e conectar nosso aplicativo Flask a um banco de dados SQLite, que é uma excelente escolha para desenvolvimento local. SQLAlchemy nos permite configurar essa conexão de forma rápida e fácil.

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_banco_de_dados.db'
db = SQLAlchemy(app)
```

**3. Definindo Modelos de Dados**

Com o SQLAlchemy, podemos definir nossos modelos de dados como classes Python. Cada classe representa uma tabela no banco de dados e seus atributos correspondem às colunas dessa tabela.

```python
from datetime import datetime

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Usuario {self.nome}>'
```

**4. Operações CRUD**

Com os modelos de dados definidos, podemos realizar operações CRUD (Create, Read, Update, Delete) no banco de dados usando SQLAlchemy. Vamos explorar como realizar essas operações em nossas tabelas.

```python
# Criar um novo usuário
novo_usuario = Usuario(nome='Alice', email='alice@example.com')
db.session.add(novo_usuario)
db.session.commit()

# Ler todos os usuários
usuarios = Usuario.query.all()
for usuario in usuarios:
    print(usuario.nome, usuario.email)

# Atualizar um usuário existente
usuario = Usuario.query.filter_by(nome='Alice').first()
usuario.email = 'novo_email@example.com'
db.session.commit()

# Excluir um usuário
usuario = Usuario.query.filter_by(nome='Alice').first()
db.session.delete(usuario)
db.session.commit()
```

**Exercícios Práticos:**

1. Defina um modelo de dados para representar produtos em uma loja online, com atributos como nome, preço e quantidade em estoque.
2. Implemente uma rota em sua aplicação Flask para exibir todos os produtos cadastrados no banco de dados.
3. Crie uma função para adicionar novos produtos ao banco de dados e teste-a com alguns produtos fictícios.
4. Desenvolva uma rota para permitir a atualização do preço de um produto específico no banco de dados.

Estes exercícios práticos ajudarão a solidificar seus conhecimentos sobre integração de bancos de dados em aplicações Flask usando SQLAlchemy. Ao concluir estes exercícios, você estará mais confortável com o gerenciamento de dados em suas aplicações web e estará pronto para enfrentar desafios mais complexos no desenvolvimento de software.

**Resolução dos Exercícios**

***Exercício 01:***


```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade_estoque = db.Column(db.Integer, nullable=False, default=0)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Produto {self.nome}>'
```

Neste modelo de dados, definimos a classe `Produto`, que representa a tabela de produtos em nosso banco de dados. Esta classe possui os seguintes atributos:

- `id`: Um identificador único para cada produto (chave primária).
- `nome`: O nome do produto (limite de 100 caracteres, obrigatório).
- `preco`: O preço do produto (obrigatório).
- `quantidade_estoque`: A quantidade disponível em estoque do produto (obrigatório, valor padrão de 0).
- `data_criacao`: A data e hora em que o produto foi criado (valor padrão definido como a data e hora atual).

Com este modelo de dados, podemos representar produtos de uma loja online de forma eficiente e realizar operações como criar, ler, atualizar e excluir produtos no banco de dados.

***Exercício 02:***

Para implementar uma rota em nossa aplicação Flask para exibir todos os produtos cadastrados no banco de dados, podemos usar o SQLAlchemy para buscar todos os registros da tabela de produtos e, em seguida, renderizar um template HTML para exibir esses produtos. Abaixo está a implementação:

```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loja_online.db'
db = SQLAlchemy(app)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade_estoque = db.Column(db.Integer, nullable=False, default=0)

@app.route('/produtos')
def listar_produtos():
    produtos = Produto.query.all()
    return render_template('produtos.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)
```

Neste exemplo, criamos uma rota `/produtos` que chama a função `listar_produtos()`. Dentro desta função, usamos `Produto.query.all()` para buscar todos os produtos cadastrados no banco de dados e passamos esses produtos para um template HTML chamado `produtos.html`.

Aqui está um exemplo de como seria o template `produtos.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Produtos</title>
</head>
<body>
    <h1>Produtos Disponíveis</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Preço</th>
                <th>Quantidade em Estoque</th>
            </tr>
        </thead>
        <tbody>
            {% for produto in produtos %}
            <tr>
                <td>{{ produto.id }}</td>
                <td>{{ produto.nome }}</td>
                <td>{{ produto.preco }}</td>
                <td>{{ produto.quantidade_estoque }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

Este template renderiza uma tabela HTML que exibe os detalhes de cada produto, incluindo o ID, nome, preço e quantidade em estoque. Ao acessar a rota `/produtos` em nosso aplicativo Flask, esta página será exibida com todos os produtos cadastrados no banco de dados.

***Exercício 03:***

Para criar uma função que adiciona novos produtos ao banco de dados, podemos definir uma rota em nosso aplicativo Flask que aceita solicitações POST com os dados do novo produto. Vamos implementar isso abaixo:

```python
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
```

Neste exemplo, criamos uma nova rota `/adicionar_produto` que aceita tanto solicitações GET quanto POST. Quando recebemos uma solicitação POST com dados de um novo produto, extraímos esses dados do formulário enviado, criamos uma nova instância do modelo `Produto` com esses dados e a adicionamos ao banco de dados.

Aqui está um exemplo de como seria o template `adicionar_produto.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adicionar Produto</title>
</head>
<body>
    <h1>Adicionar Novo Produto</h1>
    <form method="post">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required><br>
        <label for="preco">Preço:</label>
        <input type="number" id="preco" name="preco" step="0.01" min="0" required><br>
        <label for="quantidade_estoque">Quantidade em Estoque:</label>
        <input type="number" id="quantidade_estoque" name="quantidade_estoque" min="0" required><br>
        <button type="submit">Adicionar Produto</button>
    </form>
</body>
</html>
```

Este formulário HTML permite que os usuários adicionem novos produtos fornecendo o nome, preço e quantidade em estoque. Quando o formulário é enviado, os dados são enviados para a rota `/adicionar_produto`, onde são processados pela função `adicionar_produto()` e o novo produto é adicionado ao banco de dados.

***Exercício 04***

Para permitir a atualização do preço de um produto específico no banco de dados, podemos criar uma rota em nosso aplicativo Flask que aceita solicitações POST com o ID do produto e o novo preço. Em seguida, podemos usar o SQLAlchemy para encontrar o produto pelo ID e atualizar seu preço. Aqui está a implementação:

```python
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

@app.route('/atualizar_preco/<int:id>', methods=['GET', 'POST'])
def atualizar_preco(id):
    produto = Produto.query.get_or_404(id)
    if request.method == 'POST':
        novo_preco = float(request.form['novo_preco'])
        produto.preco = novo_preco
        db.session.commit()
        return redirect(url_for('listar_produtos'))
    return render_template('atualizar_preco.html', produto=produto)

@app.route('/produtos')
def listar_produtos():
    produtos = Produto.query.all()
    return render_template('produtos.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)
```

Neste exemplo, criamos uma nova rota `/atualizar_preco/<int:id>`, onde `<int:id>` é um parâmetro de rota que representa o ID do produto que queremos atualizar. Quando recebemos uma solicitação POST com o novo preço do produto, buscamos o produto pelo ID usando `Produto.query.get_or_404(id)`, atualizamos seu preço e comitamos as mudanças no banco de dados.

Aqui está um exemplo de como seria o template `atualizar_preco.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Atualizar Preço</title>
</head>
<body>
    <h1>Atualizar Preço do Produto: {{ produto.nome }}</h1>
    <form method="post">
        <label for="novo_preco">Novo Preço:</label>
        <input type="number" id="novo_preco" name="novo_preco" step="0.01" min="0" required><br>
        <button type="submit">Atualizar Preço</button>
    </form>
</body>
</html>
```

Este formulário HTML permite que os usuários atualizem o preço de um produto específico fornecendo o novo preço. Quando o formulário é enviado, os dados são enviados para a rota `/atualizar_preco/<int:id>`, onde são processados pela função `atualizar_preco()` e o preço do produto é atualizado no banco de dados.