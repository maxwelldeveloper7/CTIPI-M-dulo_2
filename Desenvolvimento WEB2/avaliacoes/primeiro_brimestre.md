### CONTEXTO:

Este passo a passo destina-se a orientar os alunos na criação de um ambiente de desenvolvimento para um sistema de cadastro de livros em Python utilizando o framework Flask. O ambiente de desenvolvimento será configurado em um ambiente virtual Python (`venv`) para garantir a isolamento de dependências e facilitar a gestão do projeto. O sistema será armazenado em memória e não em um banco de dados para simplificar o desenvolvimento.

### ROTEIRO:

#### 1. Criação do Projeto:

1.1. Abra o terminal no Xubuntu.

1.2. Crie uma pasta para o projeto de cadastro de livros:
```bash
mkdir cadastro-de-livros
```

#### 2. Estrutura do Projeto:

2.1. Dentro da pasta do projeto, crie a estrutura de pastas necessária:
```bash
cd cadastro-de-livros
mkdir templates static
touch app.py static/style.css templates/index.html
```

#### 3. Configuração do Ambiente de Desenvolvimento:

3.1. Abra o VSCode na pasta do projeto:
```bash
code .
```

3.2. No VSCode, abra o terminal integrado (Ctrl + `).

3.3. Crie e ative o ambiente virtual (`venv`):
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 4. Instalação do Flask:

4.1. No terminal do VSCode (com o `venv` ativado), instale o Flask:
```bash
pip install Flask
```

#### 5. Implementação do Código:

5.1. Implemente o código HTML da página inicial (`index.html`) dentro da pasta `templates`.

5.2. Implemente o código CSS da página inicial (`style.css`) dentro da pasta `static`.

5.3. Implemente o código Python da aplicação (`app.py`) para configurar o Flask e fornecer as rotas necessárias para o sistema de cadastro de livros.

### Exemplo de Implementação do Código:

#### `templates/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Livros</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Cadastro de Livros</h1>
    <!-- Formulário de cadastro de livros -->
    <form action="/adicionar_livro" method="post">
        <label for="titulo">Título:</label>
        <input type="text" id="titulo" name="titulo" required><br>
        <label for="autor">Autor:</label>
        <input type="text" id="autor" name="autor" required><br>
        <label for="ano">Ano:</label>
        <input type="number" id="ano" name="ano" required><br>
        <button type="submit">Adicionar Livro</button>
    </form>
    <!-- Lista de livros cadastrados -->
    <h2>Livros Cadastrados:</h2>
    <ul>
        {% for livro in livros %}
            <li>{{ livro.titulo }} - {{ livro.autor }} ({{ livro.ano }})</li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `static/style.css`:

```css
body {
    font-family: Arial, sans-serif;
}

h1 {
    color: #333;
}

form {
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="number"],
button {
    margin-bottom: 10px;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    margin-bottom: 5px;
}
```

#### `app.py`:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

livros = []

@app.route('/')
def index():
    return render_template('index.html', livros=livros)

@app.route('/adicionar_livro', methods=['POST'])
def adicionar_livro():
    titulo = request.form['titulo']
    autor = request.form['autor']
    ano = request.form['ano']
    livros.append({'titulo': titulo, 'autor': autor, 'ano': ano})
    return index()

if __name__ == '__main__':
    app.run(debug=True)
```

Este roteiro fornece os passos necessários para configurar um ambiente de desenvolvimento para um sistema de cadastro de livros em Python utilizando Flask no Xubuntu. Certifique-se de seguir cada passo com cuidado e adaptar o código conforme necessário para atender aos requisitos específicos do projeto.