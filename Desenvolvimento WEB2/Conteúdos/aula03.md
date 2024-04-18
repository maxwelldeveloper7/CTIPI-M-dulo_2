**Semana 5-6: Introdução ao Flask**

Nesta etapa, mergulharemos no mundo do desenvolvimento web com Python, explorando o framework Flask. Flask é conhecido por sua simplicidade e flexibilidade, tornando-o uma escolha popular para a construção de aplicativos web.

**1. O que é Flask?**

Flask é um microframework web escrito em Python. Ele permite construir aplicações web de forma rápida e fácil, oferecendo uma estrutura mínima e flexível para desenvolvimento.

**2. Configuração do Ambiente de Desenvolvimento**

Antes de começar a trabalhar com Flask, é necessário configurar um ambiente de desenvolvimento. Isso geralmente envolve a instalação do Python e do Flask.


Primeiro, verifique se o Python está instalado em seu sistema. Abra um terminal e execute o seguinte comando:

```bash
python3 --version
```

Se o Python estiver instalado corretamente, você verá a versão instalada.


Em algumas distribuições Linux, o `venv` pode não estar instalado por padrão. Você pode instalar usando o gerenciador de pacotes da sua distribuição. Por exemplo, no Ubuntu, você pode usar o `apt`:

```bash
sudo apt update
sudo apt install python3-venv
```

Navegue até o diretório onde deseja criar o ambiente virtual. Por exemplo, se você estiver em seu diretório de projetos, pode executar:

```bash
cd caminho/do/seu/diretorio/de/projetos
```

Agora, para criar um novo ambiente virtual, execute o seguinte comando:

```bash
python -m venv nome_do_ambiente
```

Isso criará um novo diretório com o nome especificado (`nome_do_ambiente` neste exemplo), contendo o ambiente virtual.

Agora, ative o ambiente virtual. Isso é necessário sempre que você desejar trabalhar em seu projeto usando este ambiente virtual. No terminal, execute:


```bash
source nome_do_ambiente/bin/activate
```

Agora que o ambiente virtual está ativado, qualquer instalação de pacotes Python ou execução de scripts Python será isolada neste ambiente. Você pode instalar pacotes usando `pip`, executar scripts Python e assim por diante.

Quando terminar de trabalhar no ambiente virtual, você pode desativá-lo. No terminal, execute:

```bash
deactivate
```

Com estes passos, você pode criar e gerenciar ambientes virtuais em Python usando o `venv`. Isso é útil para isolar as dependências de diferentes projetos e evitar conflitos entre elas.

Agora com o ambiente criado e ativado, instale o Flask com o comando abaixo:

```bash
pip install flask
```

**3. Criando uma Aplicação Flask Simples**

Vamos começar criando uma aplicação Flask simples que exibe "Olá, Mundo!" em uma página web.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá, Mundo!'

if __name__ == '__main__':
    app.run(debug=True)
```

**4. Explorando Rotas e Views em Flask**

Flask utiliza rotas para direcionar requisições HTTP para funções específicas, conhecidas como views. Vamos criar mais rotas e views para nossa aplicação.

```python
@app.route('/sobre')
def sobre():
    return 'Página Sobre'

@app.route('/contato')
def contato():
    return 'Página de Contato'
```

**Exercícios Práticos:**

1. Crie uma aplicação Flask que exiba seu nome em uma página web.
2. Adicione uma rota para exibir sua idade.
3. Crie uma página que liste seus hobbies.
4. Implemente uma rota que exiba uma mensagem personalizada de acordo com o horário do dia (bom dia, boa tarde, boa noite).

Esses exercícios práticos ajudarão a consolidar seus conhecimentos sobre Flask. Experimente criar diferentes rotas e views, explorando a flexibilidade e simplicidade que o framework oferece. O Flask é uma excelente escolha para começar a desenvolver aplicações web com Python, e esta é apenas a primeira etapa de nossa jornada na construção de aplicações web poderosas e dinâmicas.