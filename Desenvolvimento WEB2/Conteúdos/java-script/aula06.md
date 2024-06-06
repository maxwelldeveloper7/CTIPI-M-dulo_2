### Semana 11-12: Desenvolvimento de Aplicações Back-end com Node.js

#### Objetivos
- Construir servidores e rotas em Node.js.
- Usar módulos e middleware no desenvolvimento back-end.

### Construindo Servidores e Rotas em Node.js

#### Configurando o Projeto

1. **Inicialize um novo projeto Node.js:**
   ```sh
   mkdir backend-project
   cd backend-project
   npm init -y
   ```

2. **Instale o Express, um framework para criar servidores em Node.js:**
   ```sh
   npm install express
   ```

### Criando um Servidor Básico com Express

#### Estrutura do Projeto
```
backend-project/
│
├── package.json
├── package-lock.json
└── app.js
```

#### Código do Servidor (app.js)
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Rota raiz
app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}/`);
});
```

Para executar o servidor:
```sh
node app.js
```
Abra um navegador e vá para `http://localhost:3000/`. Você verá a mensagem `Hello, World!`.

### Rotas em Node.js com Express

#### Definindo Múltiplas Rotas
Vamos adicionar mais algumas rotas ao nosso servidor.

```javascript
// Rota para sobre
app.get('/about', (req, res) => {
    res.send('Sobre nós');
});

// Rota para contato
app.get('/contact', (req, res) => {
    res.send('Contato');
});

// Rota com parâmetro
app.get('/users/:id', (req, res) => {
    const userId = req.params.id;
    res.send(`Usuário ID: ${userId}`);
});
```

### Usando Módulos no Node.js

Node.js permite que você organize seu código em módulos reutilizáveis. Vamos criar um módulo simples.

#### Criando um Módulo
1. **Crie uma pasta chamada `routes` e dentro dela um arquivo chamado `users.js`:**
   ```
   backend-project/
   ├── routes/
   │   └── users.js
   └── app.js
   ```

2. **Defina as rotas de usuários em `users.js`:**
   ```javascript
   const express = require('express');
   const router = express.Router();

   router.get('/', (req, res) => {
       res.send('Lista de usuários');
   });

   router.get('/:id', (req, res) => {
       const userId = req.params.id;
       res.send(`Usuário ID: ${userId}`);
   });

   module.exports = router;
   ```

3. **Importe e use o módulo em `app.js`:**
   ```javascript
   const express = require('express');
   const app = express();
   const port = 3000;

   const userRoutes = require('./routes/users');

   app.use('/users', userRoutes);

   app.get('/', (req, res) => {
       res.send('Hello, World!');
   });

   app.listen(port, () => {
       console.log(`Servidor rodando em http://localhost:${port}/`);
   });
   ```

### Middleware em Node.js com Express

Middleware são funções que têm acesso ao objeto de solicitação (req), ao objeto de resposta (res) e à próxima função de middleware no ciclo de solicitação-resposta. Eles podem executar código, modificar objetos de solicitação e resposta, encerrar o ciclo de solicitação-resposta ou chamar o próximo middleware na pilha.

#### Exemplo de Middleware

```javascript
// Middleware de registro de solicitações
app.use((req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();
});

// Middleware de autenticação (simulação)
app.use('/users', (req, res, next) => {
    const auth = true; // Simulação de autenticação
    if (auth) {
        next();
    } else {
        res.status(401).send('Não autorizado');
    }
});
```

### Exercícios Práticos

1. **Crie um servidor Express e defina rotas para `/`, `/about`, e `/contact`.**
   - A rota `/` deve responder com "Hello, World!".
   - A rota `/about` deve responder com "Sobre nós".
   - A rota `/contact` deve responder com "Contato".

2. **Crie um módulo chamado `products` que define rotas para listar produtos e obter detalhes de um produto por ID.**
   - `/products` deve responder com "Lista de produtos".
   - `/products/:id` deve responder com "Produto ID: [id]".

3. **Adicione um middleware de registro de solicitações que registre o método e a URL de cada solicitação no console.**

4. **Adicione um middleware de autenticação simulado que permite acesso às rotas `/products` apenas se uma condição de autenticação for verdadeira. Caso contrário, deve responder com "Não autorizado".**

### Resolução dos Exercícios Práticos

#### Exercício 1
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.get('/about', (req, res) => {
    res.send('Sobre nós');
});

app.get('/contact', (req, res) => {
    res.send('Contato');
});

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}/`);
});
```

#### Exercício 2

**Estrutura do Projeto:**
```
backend-project/
├── routes/
│   ├── users.js
│   └── products.js
└── app.js
```

**Código do Módulo `products` (`products.js`):**
```javascript
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
    res.send('Lista de produtos');
});

router.get('/:id', (req, res) => {
    const productId = req.params.id;
    res.send(`Produto ID: ${productId}`);
});

module.exports = router;
```

**Importando e Usando o Módulo em `app.js`:**
```javascript
const express = require('express');
const app = express();
const port = 3000;

const userRoutes = require('./routes/users');
const productRoutes = require('./routes/products');

app.use('/users', userRoutes);
app.use('/products', productRoutes);

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}/`);
});
```

#### Exercício 3

**Middleware de Registro de Solicitações:**
```javascript
app.use((req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();
});
```

#### Exercício 4

**Middleware de Autenticação Simulada:**
```javascript
app.use('/products', (req, res, next) => {
    const auth = true; // Simulação de autenticação
    if (auth) {
        next();
    } else {
        res.status(401).send('Não autorizado');
    }
});
```

Com esta introdução ao desenvolvimento de back-end com Node.js, você está pronto para criar servidores robustos e escaláveis, usar módulos para organizar seu código e aplicar middleware para adicionar funcionalidades ao ciclo de solicitação-resposta. Nos próximos módulos, exploraremos mais funcionalidades avançadas do Node.js e a integração com bancos de dados.