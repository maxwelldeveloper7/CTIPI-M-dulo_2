**Semana 5-6: Funções Avançadas em JavaScript**

Funções são um conceito fundamental em JavaScript, permitindo encapsular lógica para reutilização e modularização. Nesta semana, exploraremos funções avançadas, incluindo closures, callbacks, e promises. Vamos abordar esses tópicos de maneira progressiva, com exemplos de código e exercícios práticos para ajudar a consolidar o aprendizado.

### 1. Funções Avançadas em JavaScript
Uma função em JavaScript é um bloco de código projetado para realizar uma tarefa específica. Você pode defini-la e chamá-la quando necessário.

```javascript
// Definição de uma função simples
function saudacao(nome) {
    console.log("Olá, " + nome + "!");
}

// Chamando a função
saudacao("Carlos");
```

### 2. Closures
Closures são uma característica poderosa em JavaScript. Elas permitem que uma função "lembre" o escopo em que foi definida, mesmo quando executada em um contexto diferente.

```javascript
function contador() {
    let contagem = 0; // Variável do escopo da função externa

    return function () {
        contagem++; // Modifica a variável do escopo externo
        console.log("Contagem:", contagem);
    };
}

const minhaContagem = contador(); // Retorna uma função que "lembra" da variável contagem
minhaContagem(); // Contagem: 1
minhaContagem(); // Contagem: 2
```

Neste exemplo, a função retornada "lembra" da variável `contagem`, mesmo depois que a função externa terminou sua execução.

### 3. Callbacks
Um callback é uma função passada como argumento para outra função. Callbacks são amplamente usados para operações assíncronas ou para fornecer lógica customizada para uma função.

```javascript
// Função que recebe um callback como argumento
function processarArray(array, callback) {
    for (let i = 0; i < array.length; i++) {
        callback(array[i]); // Chama o callback para cada elemento do array
    }
}

// Callback que exibe o elemento
function exibirElemento(elemento) {
    console.log("Elemento:", elemento);
}

const numeros = [1, 2, 3, 4, 5];
processarArray(numeros, exibirElemento); // Chama o callback para cada elemento
```

### 4. Promises
Promises são um mecanismo para lidar com operações assíncronas em JavaScript. Elas representam um valor que pode estar disponível agora, no futuro, ou nunca. Promises podem ter três estados: pendente, resolvida ou rejeitada.

```javascript
// Função que retorna uma promise
function esperarSegundos(segundos) {
    return new Promise((resolve, reject) => {
        if (segundos > 0) {
            setTimeout(() => {
                resolve("Esperou " + segundos + " segundos");
            }, segundos * 1000); // Converte para milissegundos
        } else {
            reject("O tempo deve ser maior que 0");
        }
    });
}

// Usando uma promise
esperarSegundos(2)
    .then((mensagem) => {
        console.log(mensagem);
    })
    .catch((erro) => {
        console.log("Erro:", erro);
    });
```

Neste exemplo, a função `esperarSegundos` retorna uma promise que é resolvida após um tempo especificado, ou rejeitada se o tempo for inválido.

### Exercícios Práticos
Para consolidar o conhecimento sobre funções avançadas, closures, callbacks e promises, experimente os exercícios a seguir:

### Exercício 1: Closure para Contagem
**Requisito:** Crie uma função que retorna outra função que "lembra" da contagem e a incrementa cada vez que é chamada.

**Solução:**
```javascript
function criarContador() {
    // Variável do escopo externo, que será "lembrada"
    let contagem = 0;

    // Retorna uma função que incrementa e exibe a contagem
    return function () {
        contagem++; // Incrementa a contagem
        console.log("Contagem:", contagem); // Exibe a contagem
    };
}

const contador = criarContador(); // Cria um contador

// Chamadas ao contador, que "lembra" da variável contagem
contador(); // Contagem: 1
contador(); // Contagem: 2
contador(); // Contagem: 3
```

Neste exercício, a função `criarContador` retorna uma função interna que tem acesso à variável `contagem` do escopo externo. Isso é um exemplo clássico de closure em JavaScript.

### Exercício 2: Callback para Processar Arrays
**Requisito:** Crie uma função que recebe um array e um callback, e chama o callback para cada elemento do array.

**Solução:**
```javascript
function processarArray(array, callback) {
    // Itera sobre o array e chama o callback para cada elemento
    for (let i = 0; i < array.length; i++) {
        callback(array[i]); // Chama o callback passando o elemento
    }
}

// Callback para exibir o elemento
function exibirElemento(elemento) {
    console.log("Elemento:", elemento);
}

// Testando com um array de números
const numeros = [10, 20, 30, 40, 50];

processarArray(numeros, exibirElemento); // Chama o callback para cada elemento do array
```

Aqui, o uso de callbacks permite personalizar a operação realizada para cada elemento do array. A função `processarArray` recebe um array e um callback como argumentos e executa o callback para cada elemento do array.

### Exercício 3: Promise para Verificação
**Requisito:** Crie uma promise que resolve se um número é par e rejeita se for ímpar.

**Solução:**
```javascript
function verificarNumero(numero) {
    return new Promise((resolve, reject) => {
        // Verifica se o número é par ou ímpar
        if (numero % 2 === 0) {
            resolve("O número " + numero + " é par.");
        } else {
            reject("O número " + numero + " é ímpar.");
        }
    });
}

// Testando a promise com um número par
verificarNumero(4)
    .then((mensagem) => {
        console.log(mensagem); // O número 4 é par.
    })
    .catch((erro) => {
        console.log("Erro:", erro); // Não é chamado, pois 4 é par
    });

// Testando a promise com um número ímpar
verificarNumero(7)
    .then((mensagem) => {
        console.log(mensagem); // Não é chamado, pois 7 é ímpar
    })
    .catch((erro) => {
        console.log("Erro:", erro); // Erro: O número 7 é ímpar.
    });
```

Neste exemplo, a função `verificarNumero` retorna uma promise que resolve se o número é par e rejeita se for ímpar. A promise usa os métodos `then` e `catch` para definir o comportamento após a resolução ou rejeição.

### Exercício 4: Promise para Operação Assíncrona
**Requisito:** Crie uma promise que simule um tempo de espera e resolva com uma mensagem após 3 segundos.

**Solução:**
```javascript
function esperarTresSegundos() {
    return new Promise((resolve, reject) => {
        // Simula uma operação assíncrona com setTimeout
        setTimeout(() => {
            resolve("A espera de 3 segundos terminou."); // Resolve após 3 segundos
        }, 3000); // 3 segundos em milissegundos
    });
}

// Testando a promise
esperarTresSegundos()
    .then((mensagem) => {
        console.log(mensagem); // A espera de 3 segundos terminou.
    })
    .catch((erro) => {
        console.log("Erro:", erro); // Não é chamado neste caso
    });
```

Nesta solução, a função `esperarTresSegundos` retorna uma promise que é resolvida após um tempo de espera de 3 segundos. A promise usa `setTimeout` para simular uma operação assíncrona. Quando a promise é resolvida, ela retorna uma mensagem, e o método `then` lida com a resolução.

Estas soluções demonstram a implementação de funções avançadas, closures, callbacks e promises em JavaScript. Cada exercício fornece um exemplo prático para consolidar o entendimento dos alunos sobre esses conceitos.