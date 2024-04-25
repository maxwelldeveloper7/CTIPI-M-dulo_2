**Semana 1-2: Fundamentos de JavaScript**

JavaScript é uma linguagem de programação essencial para o desenvolvimento web. Ela permite que você adicione interatividade e dinamicidade a páginas web. Nesta primeira semana, você aprenderá sobre os fundamentos do JavaScript, incluindo variáveis, tipos de dados e operadores.

### 1. Variáveis em JavaScript
Variáveis são usadas para armazenar valores ou dados. Em JavaScript, você pode declarar variáveis usando três palavras-chave: `var`, `let` e `const`.

- `var`: É a forma tradicional de declarar variáveis. Tem escopo de função ou global.
- `let`: Introduzido no ES6, tem escopo de bloco (mais seguro e recomendado que `var`).
- `const`: Semelhante a `let`, mas o valor não pode ser reatribuído após a inicialização.

Exemplo de declaração de variáveis:

```javascript
var nome = "Alice"; // Declaração com 'var'
let idade = 25;     // Declaração com 'let'
const PI = 3.14;    // Declaração com 'const'
```

### 2. Tipos de Dados
JavaScript possui vários tipos de dados. Alguns dos mais comuns são:

- **String**: Sequência de caracteres.
- **Number**: Pode ser um número inteiro ou decimal.
- **Boolean**: Pode ser `true` ou `false`.
- **Array**: Lista de valores indexados.
- **Object**: Estrutura de dados com pares chave-valor.
- **Null e Undefined**: Representam ausência de valor.

Exemplos de tipos de dados:

```javascript
let nome = "Bob";  // String
let idade = 30;    // Number
let casado = true; // Boolean
let cores = ["vermelho", "azul", "verde"]; // Array
let pessoa = { nome: "Charlie", idade: 28 }; // Object
```

### 3. Operadores em JavaScript
Operadores permitem realizar operações sobre variáveis ou valores. Alguns dos principais operadores são:

- **Aritméticos**: Usados para operações matemáticas (e.g., `+`, `-`, `*`, `/`, `%`).
- **Comparação**: Usados para comparar valores (e.g., `==`, `!=`, `===`, `!==`, `>`, `<`, `>=`, `<=`).
- **Lógicos**: Usados para operações lógicas (e.g., `&&`, `||`, `!`).

Exemplos de operadores:

```javascript
let soma = 5 + 3;        // Soma
let subtracao = 10 - 4;  // Subtração
let produto = 2 * 6;     // Multiplicação
let divisao = 20 / 4;    // Divisão
let resto = 10 % 3;      // Resto da divisão (módulo)

let igual = (5 == "5");  // Comparação de valor (true)
let estritamenteIgual = (5 === "5"); // Comparação de tipo e valor (false)

let eLogico = (true && false); // Operador 'E' (false)
let ouLogico = (true || false); // Operador 'OU' (true)
```

### Exercícios Práticos
Para concluir esta seção, tente resolver os exercícios:


1. **Código Prático**: Crie uma variável `nome` e defina seu valor para "Alice". Em seguida, crie uma variável `idade` e defina seu valor para 28. Mostre essas variáveis no console.

```javascript
// Criando as variáveis
let nome = "Alice";
let idade = 28;

// Exibindo no console
console.log("Nome:", nome);
console.log("Idade:", idade);
```

2. **Código Prático**: Defina um array chamado `cores` com as cores "vermelho", "azul" e "verde". Adicione uma nova cor "amarelo" ao final do array e mostre o resultado no console.

```javascript
// Criando o array com cores
let cores = ["vermelho", "azul", "verde"];

// Adicionando uma nova cor ao final do array
cores.push("amarelo");

// Exibindo o array no console
console.log("Cores:", cores);
```

3. **Código Prático**: Crie uma expressão lógica que retorne `true` se uma variável `x` for maior que 10 e menor que 20.
```javascript
// Definindo a variável x
let x = 15; // Exemplo de valor para x

// Criando a expressão lógica
let resultado = (x > 10 && x < 20);

// Exibindo o resultado no console
console.log("A expressão é:", resultado);
```


## Atividade Avaliativa Complementar: Aula 01 - Fundamentos de JavaScript

### Questão 1: Declaração de Variáveis
Qual é a diferença principal entre `var`, `let`, e `const` em JavaScript?

a) `var` e `let` são escopos de função, enquanto `const` tem escopo global.

b) `var` é global, `let` é escopo de bloco, e `const` não permite reatribuição após a inicialização.

c) `var` é mais rápido que `let` e `const`.

d) `var` é usado para números, `let` para strings e `const` para booleanos.


### Questão 2: Tipos de Dados
Qual dos seguintes não é um tipo de dado em JavaScript?

a) String

b) Number

c) Boolean

d) Char


### Questão 3: Operadores de Comparação
Qual é a diferença entre os operadores `==` e `===` em JavaScript?

a) `==` compara apenas valores, enquanto `===` compara valores e tipos.

b) `==` compara valores e tipos, enquanto `===` compara apenas valores.

c) `==` é usado para comparação numérica, enquanto `===` é para comparação de strings.

d) Não há diferença, ambos comparam valores e tipos.


### Questão 4: Operadores Lógicos
Qual dos seguintes operadores lógicos representa o operador "E" em JavaScript?

a) `&&`

b) `||`

c) `!`

d) `&`


### Questão 5: Arrays
Qual comando adiciona um elemento ao final de um array em JavaScript?

a) `push()`

b) `pop()`

c) `unshift()`

d) `shift()`
