**Semana 7-8: Desenvolvimento de Aplicações Web com Flask**

Bem-vindo à semana dedicada ao desenvolvimento avançado de aplicações web com Flask. Agora que você já está familiarizado com os conceitos básicos do Flask, é hora de explorar recursos mais avançados e criar aplicações web mais robustas.

**1. Templates em Flask**

Uma das características mais poderosas do Flask é sua integração com templates. Templates permitem criar páginas web dinâmicas, onde podemos inserir variáveis e lógica de controle de forma eficiente.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', nome='João')

if __name__ == '__main__':
    app.run(debug=True)
```

**2. Estruturação do Projeto**

À medida que nossas aplicações crescem, é importante organizar nosso código de forma eficiente. Flask não impõe uma estrutura específica de projeto, mas é comum dividir o código em módulos e pacotes para manutenção mais fácil.

```
meu_projeto/
    app.py
    templates/
        index.html
    static/
        style.css
```
**index.html**
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha Página</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Bem-vindo, {{ nome }}!</h1>
    <p>Esta é a sua página pessoal.</p>
</body>
</html>
```

**style.css**
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 0;
}

h1 {
    color: #333;
}

p {
    color: #666;
    font-size: 18px;
}

```


**3. Uso de Formulários em Flask**

Formulários são uma parte essencial de muitas aplicações web. Flask simplifica o processamento de formulários, permitindo que capturamos dados enviados pelo usuário de forma simples e eficaz.

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        # Lógica de autenticação
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
```

**Exercícios Práticos:**

1. Crie um template HTML para exibir informações pessoais de um usuário.
2. Implemente uma nova rota em sua aplicação Flask para processar um formulário de cadastro.
3. Adicione validação de formulário à sua aplicação, verificando se todos os campos obrigatórios foram preenchidos.
4. Estruture seu projeto Flask em módulos separados para as diferentes partes da aplicação, como autenticação, gerenciamento de usuários, etc.

## Resolução de exercícios
**Exercício 1:**
para resolver esse exercício, vamos criar um template HTML simples com o nome 'template_usuario.html', que exiba informações pessoais de um usuário, como nome, idade, e-mail, etc. Vamos supor que temos um dicionário chamado usuario com essas informações.
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Informações do Usuário</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Informações do Usuário</h1>
    <ul>
        <li><strong>Nome:</strong> {{ usuario.nome }}</li>
        <li><strong>Idade:</strong> {{ usuario.idade }}</li>
        <li><strong>E-mail:</strong> {{ usuario.email }}</li>
        <!-- Adicione outras informações aqui conforme necessário -->
    </ul>
</body>
</html>
```
Neste template, usamos a linguagem de modelo do Flask para inserir as informações do usuário dinamicamente. Por exemplo, {{ usuario.nome }} vai exibir o nome do usuário que foi passado para o template. Certifique-se de ajustar o nome dos campos de acordo com a estrutura do seu dicionário de usuário.
Com este template, podemos renderizar informações de usuário de forma dinâmica em nossas aplicações Flask.
```python
from flask import Flask, render_template

app = Flask(__name__)

# Rota para exibir as informações do usuário
@app.route('/')
def exibir_informacoes_usuario():
    # Dados do usuário (pode ser obtido de um banco de dados, por exemplo)
    usuario = {
        'nome': 'João da Silva',
        'idade': 30,
        'email': 'joao@example.com'
    }
    return render_template('template_usuario.html', usuario=usuario)

if __name__ == '__main__':
    app.run(debug=True)

```
Neste arquivo app.py, importamos a classe Flask do pacote flask. Em seguida, inicializamos uma instância do Flask e definimos uma rota para a raiz do aplicativo ('/'). Quando esta rota é acessada, a função exibir_informacoes_usuario() é chamada. Dentro dessa função, definimos um dicionário usuario com informações pessoais fictícias. Em seguida, usamos a função render_template() para renderizar o template HTML template_usuario.html, passando o dicionário usuario como contexto para o template.

Com isso, nosso aplicativo Flask está configurado para renderizar as informações do usuário na página inicial.

**Exercício 2**
Para resolver este exercício, vamos criar uma rota em nossa aplicação Flask que renderiza um formulário de cadastro e outra rota que processa os dados enviados pelo formulário.

1. Criando o formulário HTML:

Criaremos um formulário simples com campos para nome, e-mail e idade.
```html
<!-- formulario_cadastro.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Usuário</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Cadastro de Usuário</h1>
    <form action="/cadastrar" method="post">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required><br>
        <label for="email">E-mail:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="idade">Idade:</label>
        <input type="number" id="idade" name="idade" required><br>
        <button type="submit">Cadastrar</button>
    </form>
</body>
</html>
```

2. Criando as rotas no arquivo app.py:

Vamos criar uma rota para renderizar o formulário de cadastro e outra rota para processar os dados do formulário.

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/cadastro', methods=['GET'])
def mostrar_formulario_cadastro():
    return render_template('formulario_cadastro.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        idade = request.form['idade']
        # Salvar os dados do usuário no banco de dados ou em algum outro local
        return f'Usuário cadastrado com sucesso: {nome}, {email}, {idade} anos.'

if __name__ == '__main__':
    app.run(debug=True)

```

Neste exemplo, a rota /cadastro renderiza o formulário de cadastro quando acessada via método GET. A rota /cadastrar é responsável por processar os dados enviados pelo formulário via método POST.

Ao preencher o formulário e clicar em "Cadastrar", os dados são enviados para a rota /cadastrar, onde são recuperados e podem ser salvos em um banco de dados ou em outro local de armazenamento. Em seguida, uma mensagem de confirmação é exibida.

**Exercício 3**
**Exercício Prático 3: Adicionar validação de formulário à sua aplicação, verificando se todos os campos obrigatórios foram preenchidos**

Para adicionar validação ao formulário e garantir que todos os campos obrigatórios sejam preenchidos, vamos realizar uma verificação simples antes de processar os dados do formulário.

**1. Atualizando o arquivo HTML `formulario_cadastro.html`:**

Vamos adicionar o atributo `required` aos campos do formulário para indicar que são obrigatórios.

```html
<!-- formulario_cadastro.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Usuário</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Cadastro de Usuário</h1>
    <form action="/cadastrar" method="post">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required><br>
        <label for="email">E-mail:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="idade">Idade:</label>
        <input type="number" id="idade" name="idade" required><br>
        <button type="submit">Cadastrar</button>
    </form>
</body>
</html>
```

**2. Atualizando a rota no arquivo `app.py`:**

Vamos verificar se todos os campos obrigatórios foram preenchidos antes de processar os dados do formulário.

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/cadastro', methods=['GET'])
def mostrar_formulario_cadastro():
    return render_template('formulario_cadastro.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        # Verifica se todos os campos obrigatórios foram preenchidos
        if 'nome' in request.form and 'email' in request.form and 'idade' in request.form:
            nome = request.form['nome']
            email = request.form['email']
            idade = request.form['idade']
            # Salvar os dados do usuário no banco de dados ou em algum outro local
            return f'Usuário cadastrado com sucesso: {nome}, {email}, {idade} anos.'
        else:
            return 'Por favor, preencha todos os campos obrigatórios.'
    return redirect(url_for('mostrar_formulario_cadastro'))

if __name__ == '__main__':
    app.run(debug=True)
```

Agora, ao tentar enviar o formulário sem preencher algum dos campos obrigatórios, o usuário receberá uma mensagem solicitando que todos os campos sejam preenchidos antes de enviar o formulário. Isso garante uma validação básica no lado do servidor para garantir a integridade dos dados.