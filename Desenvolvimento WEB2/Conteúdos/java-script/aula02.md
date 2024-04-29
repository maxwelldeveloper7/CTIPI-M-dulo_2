**Aula 02: Estruturas de Controle em JavaScript**

JavaScript oferece uma variedade de estruturas de controle que permitem tomar decisões e repetir ações com base em condições específicas. Nesta aula, exploraremos as estruturas de decisão (como `if-else` e `switch`) e as estruturas de repetição (como `for`, `while`, e `do-while`). Também veremos como manipular arrays e objetos para realizar operações comuns em JavaScript.

### 1. Estruturas de Decisão em JavaScript
As estruturas de decisão permitem que você execute diferentes blocos de código com base em condições específicas. Vamos começar com a mais básica: o `if-else`.

#### 1.1. `if-else`
O `if-else` é usado para executar um bloco de código se uma condição for verdadeira, e um bloco alternativo se for falsa.

```javascript
let idade = 20;

if (idade >= 18) {
    console.log("Você é maior de idade.");
} else {
    console.log("Você é menor de idade.");
}
```

#### 1.2. `switch`
O `switch` é uma alternativa ao `if-else` para cenários com várias condições. Ele permite testar um valor contra múltiplas opções.

```javascript
let cor = "vermelho";

switch (cor) {
    case "vermelho":
        console.log("A cor é vermelho.");
        break;
    case "azul":
        console.log("A cor é azul.");
        break;
    case "verde":
        console.log("A cor é verde.");
        break;
    default:
        console.log("Cor desconhecida.");
}
```

### 2. Estruturas de Repetição em JavaScript
As estruturas de repetição permitem que você execute um bloco de código várias vezes. Vamos explorar as mais comuns.

#### 2.1. `for`
O `for` é uma estrutura de repetição com uma condição inicial, uma condição de parada e uma atualização. É útil para iterar sobre arrays ou executar um bloco de código um número específico de vezes.

```javascript
for (let i = 0; i < 5; i++) {
    console.log("Iteração:", i);
}
```

#### 2.2. `while`
O `while` repete um bloco de código enquanto uma condição for verdadeira. Cuidado com loops infinitos!

```javascript
let contador = 0;

while (contador < 3) {
    console.log("Contador:", contador);
    contador++;
}
```

#### 2.3. `do-while`
O `do-while` é semelhante ao `while`, mas garante que o bloco de código seja executado pelo menos uma vez antes de verificar a condição.

```javascript
let numero = 0;

do {
    console.log("Número:", numero);
    numero++;
} while (numero < 3);
```

### 3. Manipulação de Arrays e Objetos
Arrays e objetos são estruturas de dados comuns em JavaScript. Vamos ver como manipulá-los.

#### 3.1. Iterar Sobre Arrays
Para iterar sobre elementos de um array, você pode usar um loop `for`, `forEach`, ou outras técnicas de iteração.

```javascript
let frutas = ["maçã", "banana", "laranja"];

frutas.forEach((fruta) => {
    console.log("Fruta:", fruta);
});
```

#### 3.2. Acessar Propriedades de Objetos
Objetos armazenam dados como pares chave-valor. Você pode acessar valores usando a notação de ponto ou colchetes.

```javascript
let pessoa = {
    nome: "Carlos",
    idade: 25,
    profissao: "Desenvolvedor"
};

console.log("Nome:", pessoa.nome);
console.log("Profissão:", pessoa["profissao"]);
```

### Exercícios Práticos
Para concluir esta seção, aqui estão alguns exercícios práticos para você resolver:



### Exercício 1: Estruturas de Decisão
**Requisito:** Crie um código que determina se um número é par ou ímpar usando um `if-else`.

**Solução:**
```javascript
let numero = 7; // Você pode mudar o número para testar outros casos

if (numero % 2 === 0) {
    console.log("O número", numero, "é par.");
} else {
    console.log("O número", numero, "é ímpar.");
}
```

### Exercício 2: Estruturas de Repetição
**Requisito:** Use um loop `for` para exibir os números de 1 a 10.

**Solução:**
```javascript
for (let i = 1; i <= 10; i++) {
    console.log(i);
}
```

### Exercício 3: Manipulação de Arrays
**Requisito:** Crie um array de números e use um loop `for` para calcular a soma dos elementos.

**Solução:**
```javascript
let numeros = [1, 2, 3, 4, 5]; // Array com números para somar
let soma = 0;

for (let i = 0; i < numeros.length; i++) {
    soma += numeros[i]; // Adiciona cada número ao valor total da soma
}

console.log("A soma dos números é:", soma);
```

### Exercício 4: Manipulação de Objetos
**Requisito:** Crie um objeto representando um livro, com propriedades como `título`, `autor` e `ano de publicação`. Acesse essas propriedades e exiba-as no console.

**Solução:**
```javascript
let livro = {
    titulo: "JavaScript: The Good Parts",
    autor: "Douglas Crockford",
    anoPublicacao: 2008
};

console.log("Título do livro:", livro.titulo);
console.log("Autor do livro:", livro.autor);
console.log("Ano de publicação do livro:", livro.anoPublicacao);
```

Essas soluções implementam o que foi solicitado nos exercícios. Elas mostram como usar estruturas de decisão (`if-else`), repetição (`for`), e manipulação de arrays e objetos para resolver problemas comuns em JavaScript. Tente rodar esses códigos para verificar se os resultados são os esperados.

Aqui está uma atividade avaliativa com questões de múltipla escolha de 4 alternativas sobre a aula "Semana 3-4: Estruturas de Controle em JavaScript":

---

## Atividade Avaliativa: Semana 3-4 - Estruturas de Controle em JavaScript

### Questão 1: Estruturas de Decisão
Qual das seguintes opções é verdadeira sobre a estrutura `if-else` em JavaScript?

a) O bloco `else` é opcional e é executado se a condição do `if` for falsa.  
b) O `if-else` pode ter apenas duas condições.  
c) O `if` é usado para repetir um bloco de código enquanto uma condição for verdadeira.  
d) A condição no `if` deve ser um número.

---

### Questão 2: Estruturas de Repetição
Qual loop deve ser usado se você quiser executar um bloco de código pelo menos uma vez, independentemente da condição?

a) `for`  
b) `while`  
c) `do-while`  
d) `forEach`

---

### Questão 3: Estruturas de Repetição
Qual é o resultado do seguinte código?

```javascript
let contador = 0;

while (contador < 3) {
    console.log(contador);
    contador++;
}
```

a) Imprime 1, 2, 3  
b) Imprime 0, 1, 2  
c) Imprime 0, 1  
d) Imprime 0, 1, 2, 3  

---

### Questão 4: Estruturas de Decisão
Para qual propósito o `switch` é usado em JavaScript?

a) Para decidir qual código executar com base no valor de uma variável.  
b) Para repetir um bloco de código um número específico de vezes.  
c) Para verificar a igualdade entre duas variáveis.  
d) Para declarar variáveis dentro de um bloco.

---

### Questão 5: Manipulação de Arrays
Qual método é usado para adicionar um elemento ao início de um array em JavaScript?

a) `push()`  
b) `pop()`  
c) `unshift()`  
d) `shift()`  