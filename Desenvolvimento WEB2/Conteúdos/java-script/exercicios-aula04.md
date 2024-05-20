### Mais Exercícios Sobre Manipulação do DOM e Eventos em JavaScript

#### Exercício 1: Contador de Cliques
Crie um contador que incremente cada vez que um botão é clicado.

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
    <p id="contador">0</p>

    <script src="exercicio1.js"></script>
</body>
</html>
```

JavaScript (exercicio1.js):
```javascript
const botao = document.getElementById("botao");
const contador = document.getElementById("contador");
let count = 0;

botao.addEventListener("click", function() {
    count++;
    contador.textContent = count;
});
```

#### Exercício 2: Validador de Formulário
Crie um formulário com campos de entrada e um botão de envio. Valide se todos os campos estão preenchidos antes de enviar o formulário.

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
        <input type="text" id="nome" placeholder="Nome">
        <input type="email" id="email" placeholder="E-mail">
        <button type="submit">Enviar</button>
    </form>

    <script src="exercicio2.js"></script>
</body>
</html>
```

JavaScript (exercicio2.js):
```javascript
const formulario = document.getElementById("formulario");

formulario.addEventListener("submit", function(event) {
    event.preventDefault(); // Evita o comportamento padrão de envio do formulário

    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;

    if (nome.trim() === "" || email.trim() === "") {
        alert("Por favor, preencha todos os campos.");
    } else {
        alert("Formulário enviado com sucesso!");
        formulario.reset(); // Limpa os campos do formulário
    }
});
```

#### Exercício 3: Troca de Cores
Crie um botão que alterne a cor de fundo da página entre vermelho e azul quando clicado.

HTML:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercício 3</title>
    <style>
        body {
            background-color: red;
        }
    </style>
</head>
<body>
    <button id="botao">Trocar Cor</button>

    <script src="exercicio3.js"></script>
</body>
</html>
```

JavaScript (exercicio3.js):
```javascript
const botao = document.getElementById("botao");
const body = document.body;

botao.addEventListener("click", function() {
    if (body.style.backgroundColor === "red") {
        body.style.backgroundColor = "blue";
    } else {
        body.style.backgroundColor = "red";
    }
});
```

#### Exercício 4: Ocultar e Exibir Elemento
Crie um botão que oculte e exiba um parágrafo quando clicado.

HTML:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercício 4</title>
</head>
<body>
    <button id="botao">Ocultar/Exibir Parágrafo</button>
    <p id="paragrafo">Este é um parágrafo.</p>

    <script src="exercicio4.js"></script>
</body>
</html>
```

JavaScript (exercicio4.js):
```javascript
const botao = document.getElementById("botao");
const paragrafo = document.getElementById("paragrafo");

botao.addEventListener("click", function() {
    if (paragrafo.style.display === "none") {
        paragrafo.style.display = "block";
    } else {
        paragrafo.style.display = "none";
    }
});
```

#### Exercício 5: Contador de Caracteres
Crie um campo de entrada de texto e exiba um contador de caracteres que atualize conforme o usuário digita.

HTML:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercício 5</title>
</head>
<body>
    <input type="text" id="entrada" placeholder="Digite algo">
    <p id="contador">0 caracteres</p>

    <script src="exercicio5.js"></script>
</body>
</html>
```

JavaScript (exercicio5.js):
```javascript
const entrada = document.getElementById("entrada");
const contador = document.getElementById("contador");

entrada.addEventListener("input", function() {
    contador.textContent = entrada.value.length + " caracteres";
});
```

