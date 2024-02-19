**Aula 1-2: Introdução ao Desenvolvimento Web e Flask**

*Bem-vindos à emocionante jornada do desenvolvimento web! Nesta aula introdutória, mergulharemos nos fundamentos do desenvolvimento web e começaremos a explorar o poderoso mundo do Flask.*

**Objetivos da Aula:**
- Compreender o papel do desenvolvimento web na criação de aplicações online interativas.
- Explorar os conceitos básicos que constituem uma aplicação web.
- Introdução ao Flask como um framework web em Python.

**O que é Desenvolvimento Web?**
O desenvolvimento web é a prática de criar aplicações acessíveis através de navegadores da web. Essas aplicações variam desde simples páginas estáticas até sistemas complexos e dinâmicos. O desenvolvimento web engloba diversas tecnologias, linguagens e frameworks que trabalham juntos para proporcionar experiências interativas aos usuários.

**Elementos Básicos de uma Aplicação Web:**
1. **HTML (Hypertext Markup Language):** A linguagem de marcação que define a estrutura de uma página web.
2. **CSS (Cascading Style Sheets):** Responsável pela estilização e aparência visual da página.
3. **JavaScript:** Linguagem de programação que torna as páginas interativas e dinâmicas.

**Introdução ao Flask:**
- Flask é um framework web em Python que facilita a construção de aplicações web de forma rápida e eficiente.
- Segue a abordagem "micro", fornecendo apenas as ferramentas essenciais para o desenvolvedor, permitindo maior flexibilidade.

**Por que Flask?**
- Facilidade de aprendizado e uso, ideal para iniciantes.
- Flexibilidade para escolher componentes adicionais conforme necessário.
- Amplamente utilizado na indústria, proporcionando uma valiosa habilidade para desenvolvedores.

**Demonstração Prática:**
1. **Instalação do Flask:** Utilizaremos o pip para instalar o Flask e configurar nosso ambiente de desenvolvimento.
   ```
   pip install Flask
   ```

2. **Estrutura Básica do Projeto:** Exploraremos a estrutura inicial de um projeto Flask, destacando pastas importantes como `templates` e `static`.

3. **Hello World em Flask:** Criaremos uma aplicação simples "Hello World" para entender o conceito básico de rotas e views em Flask.

**Desafio para os Alunos:**
- Instalar o Flask em seus próprios ambientes de desenvolvimento.
- Criar uma pequena aplicação Flask com uma rota que exiba uma mensagem personalizada.

Esta aula é apenas o começo de uma jornada incrível no desenvolvimento web com Flask. Preparem-se para explorar conceitos mais avançados nas próximas aulas e colocar em prática o conhecimento adquirido em projetos práticos. Boa codificação!

## Atividades
**Passo a Passo: Demonstração Prática - Aula 1-2: Introdução ao Desenvolvimento Web e Flask**

*Seguindo as regras fornecidas, vamos criar uma aplicação Flask simples "Hello World" e explorar a estrutura básica do projeto.*

### **1. Criando a Estrutura de Diretórios:**
```bash
# Crie uma pasta para o projeto
mkdir MeuProjetoFlask

# Navegue até a pasta do projeto
cd MeuProjetoFlask

# Crie subpastas para templates e arquivos estáticos
mkdir templates static
```

### **2. Criando o Ambiente Virtual com venv:**
```bash
# Crie o ambiente virtual dentro da pasta do projeto
python3 -m venv venv

# Ative o ambiente virtual (Linux/Mac)
source venv/bin/activate

# Ative o ambiente virtual (Windows)
.\venv\Scripts\activate
```

### **3. Abrindo o Projeto no VSCode:**
```bash
# Instale o VSCode se ainda não estiver instalado
# Abra o VSCode na pasta do projeto
code .
```
- Certifique-se de que o ambiente virtual esteja ativado.

### **4. Criando a Aplicação Flask "Hello World":**
1. Crie um arquivo chamado `app.py` na pasta principal do projeto.
2. Abra o arquivo `app.py` no VSCode.
3. Adicione o seguinte código ao `app.py`:
   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def hello_world():
       return 'Hello, World!'

   if __name__ == '__main__':
       app.run(debug=True)
   ```
4. Salve o arquivo.

### **Desafio para os Alunos:**
- Crie uma rota adicional em `app.py` que exiba uma mensagem personalizada.
- Atualize a rota padrão para exibir uma mensagem diferente.
- Execute a aplicação e acesse as rotas no navegador.

### **Desativação do Ambiente Virtual (Após a Prática):**
```bash
# Desativar o ambiente virtual
deactivate
```

Este passo a passo permitirá que os alunos criem um projeto Flask simples, explorem a estrutura básica e iniciem sua jornada de desenvolvimento web com Flask. O desafio incentivará a aplicação prática do que foi aprendido na aula. Boa codificação!