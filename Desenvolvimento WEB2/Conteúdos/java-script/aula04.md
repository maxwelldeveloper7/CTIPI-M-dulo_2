### Semana 4: Manipulação do DOM e Eventos em JavaScript

Durante esta semana, exploraremos a manipulação do Document Object Model (DOM) e a interação com eventos em JavaScript. O DOM é uma representação hierárquica de todos os elementos de uma página web, e aprender a manipulá-lo é essencial para criar páginas interativas e dinâmicas. Vamos aprender como acessar elementos HTML, modificar seu conteúdo e estilo, e responder a eventos do usuário.

#### 1. Introdução ao DOM

O DOM é uma interface de programação que representa a estrutura de um documento HTML/XML como uma árvore de nós. Cada elemento HTML é representado por um nó no DOM, e podemos acessar esses nós para realizar manipulações.

```javascript
// Exemplo de acesso a um elemento pelo ID
const titulo = document.getElementById("titulo");

// Modificando o conteúdo do elemento
titulo.textContent = "Novo Título";

// Modificando o estilo do elemento
titulo.style.color = "blue";
```

#### 2. Manipulação do Conteúdo

Podemos modificar o conteúdo de elementos HTML diretamente através do DOM. Isso inclui alterar texto, atributos e até mesmo adicionar ou remover elementos.

```javascript
// Exemplo de adição de um novo parágrafo
const paragrafo = document.createElement("p");
paragrafo.textContent = "Novo parágrafo";
document.body.appendChild(paragrafo); // Adiciona o parágrafo ao final do body
```

#### 3. Manipulação de Eventos

Eventos são ações que ocorrem no navegador que podemos capturar e responder em JavaScript. Podemos adicionar ouvintes de eventos a elementos HTML para responder a interações do usuário.

```javascript
// Exemplo de adição de um ouvinte de evento
const botao = document.getElementById("botao");
botao.addEventListener("click", function() {
    console.log("Botão clicado!");
});
```

#### 4. Atualização Dinâmica de Conteúdo

Com a manipulação do DOM e eventos, podemos criar interfaces dinâmicas que respondem às ações do usuário em tempo real.

```javascript
// Exemplo de atualização dinâmica de conteúdo com base em um evento
const input = document.getElementById("input");
const resposta = document.getElementById("resposta");

input.addEventListener("keyup", function() {
    resposta.textContent = "Digitado: " + input.value;
});
```

#### Exercícios Práticos

#### Exercício 1: Crie uma página HTML com um botão. Ao clicar no botão, exiba uma mensagem na página.

HTML:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercício 1</title>
</head>
<body>
    <button id="botao">Clique aqui</button>
    <p id="mensagem"></p>

    <script src="exercicio1.js"></script>
</body>
</html>
```

JavaScript (exercicio1.js):
```javascript
const botao = document.getElementById("botao");
const mensagem = document.getElementById("mensagem");

botao.addEventListener("click", function() {
    mensagem.textContent = "Botão clicado!";
});
```

#### Exercício 2: Adicione um formulário com um campo de entrada de texto e um botão. Ao enviar o formulário, exiba o conteúdo do campo de texto em um parágrafo abaixo do formulário.
HTML:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercício 2</title>
</head>
<body>
    <form id="formulario">
        <input type="text" id="texto" placeholder="Digite algo">
        <button type="submit">Enviar</button>
    </form>
    <p id="conteudo"></p>

    <script src="exercicio2.js"></script>
</body>
</html>
```

JavaScript (exercicio2.js):
```javascript
const formulario = document.getElementById("formulario");
const texto = document.getElementById("texto");
const conteudo = document.getElementById("conteudo");

formulario.addEventListener("submit", function(event) {
    event.preventDefault(); // Evita o comportamento padrão de envio do formulário
    conteudo.textContent = texto.value;
});
```

#### Exercício 3: Adicione uma lista não ordenada (ul) à página HTML. Adicione um ouvinte de evento ao documento que adiciona um novo item de lista (li) à lista sempre que a tecla "Enter" for pressionada no campo de entrada de texto do exercício anterior.
HTML:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercício 3</title>
</head>
<body>
    <input type="text" id="entrada" placeholder="Digite e pressione Enter">
    <ul id="lista"></ul>

    <script src="exercicio3.js"></script>
</body>
</html>
```

JavaScript (exercicio3.js):
```javascript
const entrada = document.getElementById("entrada");
const lista = document.getElementById("lista");

entrada.addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        const novoItem = document.createElement("li");
        novoItem.textContent = entrada.value;
        lista.appendChild(novoItem);
        entrada.value = ""; // Limpa o campo de entrada após adicionar o item
    }
});
```
