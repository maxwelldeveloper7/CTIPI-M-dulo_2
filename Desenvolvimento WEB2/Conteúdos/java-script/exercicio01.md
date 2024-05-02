Aqui estão 10 exercícios fáceis de lógica de programação em JavaScript:

### Exercício 1:
Declare duas variáveis, `numero1` e `numero2`, e atribua a elas dois números inteiros diferentes. Em seguida, exiba a soma dos dois números.

### Exercício 2:
Declare uma variável `nome` e atribua a ela seu nome completo como uma string. Em seguida, exiba uma mensagem de boas-vindas concatenando seu nome com a mensagem "Bem-vindo!".

### Exercício 3:
Declare uma variável `idade` e atribua a ela sua idade como um número inteiro. Em seguida, use uma estrutura de decisão para verificar se você é maior de idade (idade >= 18) ou não. Exiba uma mensagem apropriada com base no resultado.

### Exercício 4:
Declare uma variável `diaSemana` e atribua a ela o nome de um dia da semana como uma string (por exemplo, "segunda-feira"). Use uma estrutura de decisão `switch` para exibir uma mensagem diferente com base no dia da semana.

### Exercício 5:
Use uma estrutura de repetição `for` para exibir os números de 1 a 10 no console.

### Exercício 6:
Declare um array de strings chamado `frutas` e adicione algumas frutas como elementos do array. Use uma estrutura de repetição `for` para exibir cada elemento do array no console.

### Exercício 7:
Declare uma variável `contador` e atribua a ela o valor 0. Use uma estrutura de repetição `while` para incrementar o contador até que ele atinja o valor 5. Exiba o valor do contador a cada iteração.

### Exercício 8:
Declare duas variáveis, `numero` e `parOuImpar`, e atribua a `numero` um número inteiro qualquer. Use uma estrutura de decisão `if-else` para verificar se `numero` é par ou ímpar. Atribua a `parOuImpar` uma string indicando se `numero` é par ou ímpar e exiba-a no console.

### Exercício 9:
Declare uma variável `ano` e atribua a ela um ano como um número inteiro. Use uma estrutura de decisão `if-else` para verificar se o ano é bissexto ou não. Exiba uma mensagem apropriada no console com base no resultado.

### Exercício 10:
Declare uma variável `senha` e atribua a ela uma senha como uma string. Use uma estrutura de decisão `if-else` para verificar se a senha tem pelo menos 8 caracteres de comprimento. Exiba uma mensagem indicando se a senha é válida ou não.

---

### Exercício 1: Soma de Dois Números
**Requisito:** Declare duas variáveis, `numero1` e `numero2`, e exiba a soma dos dois números.

**Solução:**
```javascript
// Declarar duas variáveis com números inteiros
let numero1 = 5;
let numero2 = 10;

// Calcular a soma
let soma = numero1 + numero2;

// Exibir a soma no console
console.log("A soma de", numero1, "e", numero2, "é:", soma);
```

Para executar este código no VSCode, abra o terminal integrado e execute:

```bash
node nome_do_arquivo.js
```

Substitua `nome_do_arquivo.js` pelo nome do seu arquivo, por exemplo, `exercicio1.js`.

### Exercício 2: Mensagem de Boas-vindas
**Requisito:** Declare uma variável `nome` e exiba uma mensagem de boas-vindas concatenando com "Bem-vindo!".

**Solução:**
```javascript
// Declarar uma variável com o nome
let nome = "Alice";

// Concatenar com a mensagem de boas-vindas
let mensagem = "Bem-vindo, " + nome + "!";

// Exibir a mensagem no console
console.log(mensagem);
```

Execute o código no VSCode conforme explicado anteriormente.

### Exercício 3: Estrutura de Decisão (Maior de Idade)
**Requisito:** Declare uma variável `idade` e verifique se é maior de idade.

**Solução:**
```javascript
// Declarar a variável idade
let idade = 17;

// Verificar se é maior de idade
if (idade >= 18) {
    console.log("Você é maior de idade.");
} else {
    console.log("Você é menor de idade.");
}
```

### Exercício 4: Estrutura de Decisão (Dias da Semana)
**Requisito:** Use um `switch` para exibir uma mensagem com base no dia da semana.

**Solução:**
```javascript
// Declarar a variável com o dia da semana
let diaSemana = "segunda-feira";

// Usar switch para exibir mensagens com base no dia da semana
switch (diaSemana) {
    case "segunda-feira":
        console.log("Início da semana. Muita energia!");
        break;
    case "terça-feira":
        console.log("Continuando a semana. Vamos com tudo!");
        break;
    case "quarta-feira":
        console.log("Meio da semana. Continue firme!");
        break;
    case "quinta-feira":
        console.log("Quase lá!");
        break;
    case "sexta-feira":
        console.log("Sextou! Preparado para o fim de semana?");
        break;
    case "sábado":
    case "domingo":
        console.log("É fim de semana! Hora de relaxar.");
        break;
    default:
        console.log("Dia desconhecido.");
}
```

### Exercício 5: Loop `for` para Números de 1 a 10
**Requisito:** Use um loop `for` para exibir os números de 1 a 10.

**Solução:**
```javascript
// Usar loop for para exibir números de 1 a 10
for (let i = 1; i <= 10; i++) {
    console.log(i);
}
```

### Exercício 6: Iterar sobre um Array de Frutas
**Requisito:** Declare um array de frutas e use um loop para exibir cada fruta.

**Solução:**
```javascript
// Declarar um array de frutas
let frutas = ["maçã", "banana", "laranja", "manga"];

// Iterar sobre o array e exibir cada fruta
for (let i = 0; i < frutas.length; i++) {
    console.log("Fruta:", frutas[i]);
}
```

### Exercício 7: Loop `while` para Incrementar um Contador
**Requisito:** Use um loop `while` para incrementar um contador até 5.

**Solução:**
```javascript
// Declarar um contador
let contador = 0;

// Usar loop while para incrementar o contador
while (contador < 5) {
    console.log("Contador:", contador);
    contador++; // Incrementar o contador
}
```

### Exercício 8: Estrutura de Decisão para Par ou Ímpar
**Requisito:** Verificar se um número é par ou ímpar usando um `if-else`.

**Solução:**
```javascript
// Declarar um número
let numero = 9; // Você pode mudar para testar outros casos

// Verificar se é par ou ímpar
if (numero % 2 === 0) {
    console.log("O número", numero, "é par.");
} else {
    console.log("O número", numero, "é ímpar.");
}
```

### Exercício 9: Estrutura de Decisão para Ano Bissexto
**Requisito:** Verificar se um ano é bissexto.

**Solução:**
```javascript
// Declarar uma variável com o ano
let ano = 2024; // Substitua pelo ano desejado

// Verificar se o ano é bissexto
if ((ano % 4 === 0 && ano % 100 !== 0) || (ano % 400 === 0)) {
    console.log("O ano", ano, "é bissexto.");
} else {
    console.log("O ano", ano, "não é bissexto.");
}
```

### Exercício 10: Verificar Tamanho de Senha
**Requisito:** Use um `if-else` para verificar se uma senha tem pelo menos 8 caracteres.

**Solução:**
```javascript
// Declarar uma variável com a senha
let senha = "minhasenha123"; // Mude para testar outras senhas

// Verificar se a senha tem pelo menos 8 caracteres
if (senha.length >= 8) {
    console.log("A senha é válida.");
} else {
    console.log("A senha não é válida.");
}
```

Para executar cada exercício no VSCode, salve o código em um arquivo `.js` e use o terminal integrado para rodar o arquivo com `node nome_do_arquivo.js`. Substitua `nome_do_arquivo.js` pelo nome do arquivo correspondente ao exercício. 

Estes exercícios cobrem uma variedade de conceitos, como variáveis, tipos de dados, operadores, estruturas de decisão, e repetição, fornecendo uma boa base para a prática de lógica de programação em JavaScript.