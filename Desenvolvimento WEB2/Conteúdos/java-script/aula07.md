### Semana 13-14: API RESTful com Node.js e Express

#### Objetivos
- Desenvolver uma API RESTful utilizando o framework Express.
- Explorar boas práticas no desenvolvimento de APIs.

### Introdução às APIs RESTful

APIs RESTful (Representational State Transfer) são uma abordagem de desenvolvimento de serviços web que utilizam métodos HTTP para realizar operações CRUD (Create, Read, Update, Delete) sobre recursos. As principais operações são:

- **GET:** Recuperar dados.
- **POST:** Criar novos dados.
- **PUT:** Atualizar dados existentes.
- **DELETE:** Excluir dados.

### Configurando o Projeto

1. **Inicialize um novo projeto Node.js:**
   ```sh
   mkdir api-project
   cd api-project
   npm init -y
   ```

2. **Instale o Express e o Body-parser:**
   ```sh
   npm install express body-parser
   ```

### Estrutura do Projeto
```
api-project/
├── routes/
│   └── products.js
├── models/
│   └── product.js
├── app.js
└── package.json
```

### Criando um Modelo de Produto

Crie um modelo simples para produtos utilizando um arquivo JavaScript.

#### models/product.js
```javascript
let products = [];

const getAllProducts = () => products;

const getProductById = (id) => products.find(product => product.id === id);

const addProduct = (product) => {
    products.push(product);
};

const updateProduct = (id, updatedProduct) => {
    const index = products.findIndex(product => product.id === id);
    if (index !== -1) {
        products[index] = { ...products[index], ...updatedProduct };
    }
};

const deleteProduct = (id) => {
    products = products.filter(product => product.id !== id);
};

module.exports = {
    getAllProducts,
    getProductById,
    addProduct,
    updateProduct,
    deleteProduct
};
```

### Criando Rotas para a API

Defina as rotas para os produtos.

#### routes/products.js
```javascript
const express = require('express');
const router = express.Router();
const productModel = require('../models/product');

// Recuperar todos os produtos
router.get('/', (req, res) => {
    res.json(productModel.getAllProducts());
});

// Recuperar um produto por ID
router.get('/:id', (req, res) => {
    const product = productModel.getProductById(req.params.id);
    if (product) {
        res.json(product);
    } else {
        res.status(404).send('Produto não encontrado');
    }
});

// Criar um novo produto
router.post('/', (req, res) => {
    const newProduct = {
        id: Date.now().toString(),
        name: req.body.name,
        price: req.body.price,
        stock: req.body.stock
    };
    productModel.addProduct(newProduct);
    res.status(201).json(newProduct);
});

// Atualizar um produto existente
router.put('/:id', (req, res) => {
    const updatedProduct = {
        name: req.body.name,
        price: req.body.price,
        stock: req.body.stock
    };
    productModel.updateProduct(req.params.id, updatedProduct);
    res.json(updatedProduct);
});

// Excluir um produto
router.delete('/:id', (req, res) => {
    productModel.deleteProduct(req.params.id);
    res.status(204).send();
});

module.exports = router;
```

### Configurando o Servidor

#### app.js
```javascript
const express = require('express');
const bodyParser = require('body-parser');
const productRoutes = require('./routes/products');
const app = express();
const port = 3000;

app.use(bodyParser.json());

app.use('/products', productRoutes);

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}/`);
});
```

### Boas Práticas no Desenvolvimento de APIs

1. **Estrutura Clara e Consistente:**
   - Utilize verbos HTTP corretamente (GET, POST, PUT, DELETE).
   - Organize seus endpoints de forma lógica e consistente.

2. **Respostas HTTP Apropriadas:**
   - Utilize os códigos de status HTTP adequados (200 OK, 201 Created, 404 Not Found, 500 Internal Server Error).
   - Inclua mensagens de erro detalhadas.

3. **Documentação da API:**
   - Documente seus endpoints, parâmetros, e tipos de respostas.
   - Utilize ferramentas como Swagger para gerar documentação automática.

4. **Validação de Dados:**
   - Valide a entrada de dados do usuário para evitar inconsistências e vulnerabilidades de segurança.

5. **Autenticação e Autorização:**
   - Proteja endpoints sensíveis com autenticação (ex.: JWT).
   - Controle o acesso a recursos com base em permissões do usuário.

### Testando a API

Para testar sua API, você pode usar ferramentas como Postman ou curl. Aqui estão algumas instruções para chamar as rotas na barra de endereço do navegador ou utilizando uma ferramenta de teste de API:

1. **Recuperar todos os produtos:**
   - **GET** request para `http://localhost:3000/products`
   - Resposta esperada:
     ```json
     []
     ```

2. **Recuperar um produto por ID:**
   - **GET** request para `http://localhost:3000/products/:id`
   - Substitua `:id` pelo ID do produto desejado.

3. **Criar um novo produto:**
   - **POST** request para `http://localhost:3000/products`
   - Body da requisição:
     ```json
     {
       "name": "Produto 1",
       "price": 100,
       "stock": 10
     }
     ```
   - Resposta esperada:
     ```json
     {
       "id": "1598573538195",
       "name": "Produto 1",
       "price": 100,
       "stock": 10
     }
     ```

4. **Atualizar um produto existente:**
   - **PUT** request para `http://localhost:3000/products/:id`
   - Substitua `:id` pelo ID do produto.
   - Body da requisição:
     ```json
     {
       "name": "Produto 1 atualizado",
       "price": 150,
       "stock": 5
     }
     ```
   - Resposta esperada:
     ```json
     {
       "name": "Produto 1 atualizado",
       "price": 150,
       "stock": 5
     }
     ```

5. **Excluir um produto:**
   - **DELETE** request para `http://localhost:3000/products/:id`
   - Substitua `:id` pelo ID do produto a ser excluído.
   - Resposta esperada: status 204 No Content.

### Exercícios Práticos

1. **Crie um novo modelo de dados para representar pedidos em uma loja online, com atributos como ID do pedido, ID do produto, quantidade e status. Implemente as rotas CRUD para este modelo.**

2. **Adicione validação de dados para as rotas de produtos utilizando um middleware de validação. Verifique se os campos `name`, `price`, e `stock` são fornecidos e possuem valores válidos.**

3. **Implemente autenticação básica utilizando tokens JWT para proteger as rotas de criação, atualização e exclusão de produtos.**

4. **Crie documentação da sua API utilizando Swagger e disponibilize-a em um endpoint `/docs`.**

### Resolução dos Exercícios Práticos

#### Exercício 1: Modelo de Pedidos

**models/order.js**
```javascript
let orders = [];

const getAllOrders = () => orders;

const getOrderById = (id) => orders.find(order => order.id === id);

const addOrder = (order) => {
    orders.push(order);
};

const updateOrder = (id, updatedOrder) => {
    const index = orders.findIndex(order => order.id === id);
    if (index !== -1) {
        orders[index] = { ...orders[index], ...updatedOrder };
    }
};

const deleteOrder = (id) => {
    orders = orders.filter(order => order.id !== id);
};

module.exports = {
    getAllOrders,
    getOrderById,
    addOrder,
    updateOrder,
    deleteOrder
};
```

**routes/orders.js**
```javascript
const express = require('express');
const router = express.Router();
const orderModel = require('../models/order');

// Recuperar todos os pedidos
router.get('/', (req, res) => {
    res.json(orderModel.getAllOrders());
});

// Recuperar um pedido por ID
router.get('/:id', (req, res) => {
    const order = orderModel.getOrderById(req.params.id);
    if (order) {
        res.json(order);
    } else {
        res.status(404).send('Pedido não encontrado');
    }
});

// Criar um novo pedido
router.post('/', (req, res) => {
    const newOrder = {
        id: Date.now().toString(),
        productId: req.body.productId,
        quantity: req.body.quantity,
        status: req.body.status
    };
    orderModel.addOrder(newOrder);
    res.status(201).json(newOrder);
});

// Atualizar um pedido existente
router.put('/:id', (req, res) => {
    const updatedOrder = {
        productId: req.body.productId,
        quantity: req.body.quantity,
        status: req.body.status
    };
    orderModel.update

Order(req.params.id, updatedOrder);
    res.json(updatedOrder);
});

// Excluir um pedido
router.delete('/:id', (req, res) => {
    orderModel.deleteOrder(req.params.id);
    res.status(204).send();
});

module.exports = router;
```

**Atualize o app.js para incluir as rotas de pedidos:**
```javascript
const express = require('express');
const bodyParser = require('body-parser');
const productRoutes = require('./routes/products');
const orderRoutes = require('./routes/orders');
const app = express();
const port = 3000;

app.use(bodyParser.json());

app.use('/products', productRoutes);
app.use('/orders', orderRoutes);

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}/`);
});
```

#### Exercício 2: Validação de Dados

**middleware/validation.js**
```javascript
const validateProduct = (req, res, next) => {
    const { name, price, stock } = req.body;
    if (!name || !price || !stock) {
        return res.status(400).send('Todos os campos são obrigatórios');
    }
    if (typeof price !== 'number' || typeof stock !== 'number') {
        return res.status(400).send('Preço e estoque devem ser números');
    }
    next();
};

module.exports = {
    validateProduct
};
```

**Atualize o app.js para incluir o middleware de validação:**
```javascript
const express = require('express');
const bodyParser = require('body-parser');
const productRoutes = require('./routes/products');
const orderRoutes = require('./routes/orders');
const { validateProduct } = require('./middleware/validation');
const app = express();
const port = 3000;

app.use(bodyParser.json());

app.use('/products', validateProduct, productRoutes);
app.use('/orders', orderRoutes);

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}/`);
});
```

#### Exercício 3: Autenticação com JWT

**Instale os pacotes necessários:**
```sh
npm install jsonwebtoken
```

**middleware/auth.js**
```javascript
const jwt = require('jsonwebtoken');
const secretKey = 'your-secret-key';

const authenticateToken = (req, res, next) => {
    const token = req.header('Authorization');
    if (!token) return res.status(401).send('Acesso negado');

    try {
        const verified = jwt.verify(token, secretKey);
        req.user = verified;
        next();
    } catch (err) {
        res.status(400).send('Token inválido');
    }
};

module.exports = {
    authenticateToken
};
```

**app.js**
```javascript
const express = require('express');
const bodyParser = require('body-parser');
const productRoutes = require('./routes/products');
const orderRoutes = require('./routes/orders');
const { validateProduct } = require('./middleware/validation');
const { authenticateToken } = require('./middleware/auth');
const app = express();
const port = 3000;

app.use(bodyParser.json());

app.use('/products', authenticateToken, validateProduct, productRoutes);
app.use('/orders', authenticateToken, orderRoutes);

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}/`);
});
```

**Geração de Token (rota adicional para fins de demonstração):**
```javascript
app.post('/login', (req, res) => {
    const user = {
        id: 1,
        username: 'user',
        email: 'user@example.com'
    };
    const token = jwt.sign(user, secretKey);
    res.json({ token });
});
```

#### Exercício 4: Documentação com Swagger

**Instale os pacotes necessários:**
```sh
npm install swagger-jsdoc swagger-ui-express
```

**app.js**
```javascript
const express = require('express');
const bodyParser = require('body-parser');
const swaggerJsDoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');
const productRoutes = require('./routes/products');
const orderRoutes = require('./routes/orders');
const { validateProduct } = require('./middleware/validation');
const { authenticateToken } = require('./middleware/auth');
const app = express();
const port = 3000;

const swaggerOptions = {
    swaggerDefinition: {
        info: {
            title: 'API de Produtos e Pedidos',
            description: 'API para gerenciar produtos e pedidos',
            version: '1.0.0',
        },
    },
    apis: ['./routes/*.js'],
};

const swaggerDocs = swaggerJsDoc(swaggerOptions);

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocs));
app.use(bodyParser.json());

app.use('/products', authenticateToken, validateProduct, productRoutes);
app.use('/orders', authenticateToken, orderRoutes);

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}/`);
});
```

**Comentário para Swagger na rota `products.js` (exemplo):**
```javascript
/**
 * @swagger
 * /products:
 *   get:
 *     summary: Retorna todos os produtos
 *     responses:
 *       200:
 *         description: Uma lista de produtos
 *         content:
 *           application/json:
 *             schema:
 *               type: array
 *               items:
 *                 type: object
 *                 properties:
 *                   id:
 *                     type: string
 *                   name:
 *                     type: string
 *                   price:
 *                     type: number
 *                   stock:
 *                     type: number
 */
router.get('/', (req, res) => {
    res.json(productModel.getAllProducts());
});
```

### Testando a API

Para testar sua API, você pode usar ferramentas como Postman ou curl. Aqui estão algumas instruções para chamar as rotas na barra de endereço do navegador ou utilizando uma ferramenta de teste de API:

1. **Recuperar todos os produtos:**
   - **GET** request para `http://localhost:3000/products`
   - Resposta esperada:
     ```json
     []
     ```

2. **Recuperar um produto por ID:**
   - **GET** request para `http://localhost:3000/products/:id`
   - Substitua `:id` pelo ID do produto desejado.

3. **Criar um novo produto:**
   - **POST** request para `http://localhost:3000/products`
   - Body da requisição:
     ```json
     {
       "name": "Produto 1",
       "price": 100,
       "stock": 10
     }
     ```
   - Resposta esperada:
     ```json
     {
       "id": "1598573538195",
       "name": "Produto 1",
       "price": 100,
       "stock": 10
     }
     ```

4. **Atualizar um produto existente:**
   - **PUT** request para `http://localhost:3000/products/:id`
   - Substitua `:id` pelo ID do produto.
   - Body da requisição:
     ```json
     {
       "name": "Produto 1 atualizado",
       "price": 150,
       "stock": 5
     }
     ```
   - Resposta esperada:
     ```json
     {
       "name": "Produto 1 atualizado",
       "price": 150,
       "stock": 5
     }
     ```

5. **Excluir um produto:**
   - **DELETE** request para `http://localhost:3000/products/:id`
   - Substitua `:id` pelo ID do produto a ser excluído.
   - Resposta esperada: status 204 No Content.