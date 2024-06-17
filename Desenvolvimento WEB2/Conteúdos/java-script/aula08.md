### Semana 15-16: Bancos de Dados e Node.js

#### Objetivos
- Compreender como integrar bancos de dados com Node.js.
- Utilizar a biblioteca Mongoose para interação com bancos de dados NoSQL (MongoDB).

### Introdução

Node.js é uma plataforma poderosa para o desenvolvimento de aplicações backend. Uma das tarefas mais comuns é integrar a aplicação com um banco de dados. MongoDB, um banco de dados NoSQL orientado a documentos, é uma escolha popular para desenvolvedores Node.js devido à sua flexibilidade e escalabilidade.

### Configurando o Ambiente

#### Passo 1: Criar uma Conta no MongoDB Atlas

1. Acesse sua conta do [MongoDB Atlas](https://www.mongodb.com/cloud/atlas). Crie uma caso ainda não o tenha feito.
2. Crie um novo cluster com o nome mongooseTeste, e anote as credenciais de acesso e o URI de conexão.

#### Passo 2: Inicializar um Novo Projeto Node.js

1. Crie um diretório para o seu projeto e inicialize o Node.js:
   ```sh
   mkdir mongo-project
   cd mongo-project
   npm init -y
   ```

2. Instale as dependências necessárias:
   ```sh
   npm install express mongoose body-parser
   ```

### Estrutura do Projeto

```
mongo-project/
├── models/
│   └── product.js
├── routes/
│   └── products.js
├── app.js
└── package.json
```

### Conectando ao MongoDB com Mongoose

#### app.js
```javascript
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const productRoutes = require('./routes/products');

const app = express();
const port = 3000;

// Substitua <username>, <password> e <dbname> com suas credenciais e nome do banco de dados
const mongoURI = 'mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority';

mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Conectado ao MongoDB Atlas'))
    .catch(err => console.error('Erro ao conectar ao MongoDB Atlas:', err));

app.use(bodyParser.json());

app.use('/products', productRoutes);

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}/`);
});
```

### Criando o Modelo de Produto

#### models/product.js
```javascript
const mongoose = require('mongoose');

const productSchema = new mongoose.Schema({
    name: { type: String, required: true },
    price: { type: Number, required: true },
    stock: { type: Number, required: true }
});

module.exports = mongoose.model('Product', productSchema);
```

### Criando Rotas para a API

#### routes/products.js
```javascript
const express = require('express');
const router = express.Router();
const Product = require('../models/product');

// Recuperar todos os produtos
router.get('/', async (req, res) => {
    try {
        const products = await Product.find();
        res.json(products);
    } catch (err) {
        res.status(500).send('Erro ao recuperar produtos');
    }
});

// Recuperar um produto por ID
router.get('/:id', async (req, res) => {
    try {
        const product = await Product.findById(req.params.id);
        if (product) {
            res.json(product);
        } else {
            res.status(404).send('Produto não encontrado');
        }
    } catch (err) {
        res.status(500).send('Erro ao recuperar produto');
    }
});

// Criar um novo produto
router.post('/', async (req, res) => {
    const newProduct = new Product({
        name: req.body.name,
        price: req.body.price,
        stock: req.body.stock
    });
    try {
        const savedProduct = await newProduct.save();
        res.status(201).json(savedProduct);
    } catch (err) {
        res.status(400).send('Erro ao criar produto');
    }
});

// Atualizar um produto existente
router.put('/:id', async (req, res) => {
    try {
        const updatedProduct = await Product.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (updatedProduct) {
            res.json(updatedProduct);
        } else {
            res.status(404).send('Produto não encontrado');
        }
    } catch (err) {
        res.status(400).send('Erro ao atualizar produto');
    }
});

// Excluir um produto
router.delete('/:id', async (req, res) => {
    try {
        const deletedProduct = await Product.findByIdAndDelete(req.params.id);
        if (deletedProduct) {
            res.status(204).send();
        } else {
            res.status(404).send('Produto não encontrado');
        }
    } catch (err) {
        res.status(500).send('Erro ao excluir produto');
    }
});

module.exports = router;
```

### Testando a API

Você pode testar sua API usando ferramentas como Postman ou curl. Aqui estão algumas instruções para chamar as rotas:

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
       "_id": "5f5f5f5f5f5f5f5f5f5f5f",
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
       "_id": "5f5f5f5f5f5f5f5f5f5f5f",
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

1. **Crie um novo modelo de dados para representar clientes em uma loja online, com atributos como nome, email e endereço. Implemente as rotas CRUD para este modelo.**

2. **Adicione validação de dados para as rotas de produtos utilizando a biblioteca `joi` para garantir que os campos `name`, `price`, e `stock` são fornecidos e possuem valores válidos.**

3. **Implemente uma rota para buscar produtos por nome utilizando uma query string.**

4. **Implemente paginação para a rota que recupera todos os produtos.**

5. **Crie um sistema de autenticação básico utilizando tokens JWT para proteger as rotas de criação, atualização e exclusão de produtos.**

### Resolução dos Exercícios Práticos

#### Exercício 1: Modelo de Clientes

**models/customer.js**
```javascript
const mongoose = require('mongoose');

const customerSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    address: { type: String, required: true }
});

module.exports = mongoose.model('Customer', customerSchema);
```

**routes/customers.js**
```javascript
const express = require('express');
const router = express.Router();
const Customer = require('../models/customer');

// Recuperar todos os clientes
router.get('/', async (req, res) => {
    try {
        const customers = await Customer.find();
        res.json(customers);
    } catch (err) {
        res.status(500).send('Erro ao recuperar clientes');
    }
});

// Recuperar um cliente por ID
router.get('/:id', async (req, res) => {
    try {
        const customer = await Customer.findById(req.params.id);
        if (customer) {
            res.json(customer);
        } else {
            res.status(404).send('Cliente não encontrado');
        }
    } catch (err) {
        res.status(500).send('Erro ao recuperar cliente');
    }
});

// Criar um novo cliente
router.post('/', async (req, res) => {
    const newCustomer = new Customer({
        name: req.body.name,
        email: req.body.email,
        address: req.body.address
    });
    try {
        const savedCustomer = await newCustomer.save();
        res.status(201).json(savedCustomer);
    } catch (err

) {
        res.status(400).send('Erro ao criar cliente');
    }
});

// Atualizar um cliente existente
router.put('/:id', async (req, res) => {
    try {
        const updatedCustomer = await Customer.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (updatedCustomer) {
            res.json(updatedCustomer);
        } else {
            res.status(404).send('Cliente não encontrado');
        }
    } catch (err) {
        res.status(400).send('Erro ao atualizar cliente');
    }
});

// Excluir um cliente
router.delete('/:id', async (req, res) => {
    try {
        const deletedCustomer = await Customer.findByIdAndDelete(req.params.id);
        if (deletedCustomer) {
            res.status(204).send();
        } else {
            res.status(404).send('Cliente não encontrado');
        }
    } catch (err) {
        res.status(500).send('Erro ao excluir cliente');
    }
});

module.exports = router;
```

**Atualize o app.js para incluir as rotas de clientes:**
```javascript
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const productRoutes = require('./routes/products');
const customerRoutes = require('./routes/customers');

const app = express();
const port = 3000;

const mongoURI = 'mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority';

mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Conectado ao MongoDB Atlas'))
    .catch(err => console.error('Erro ao conectar ao MongoDB Atlas:', err));

app.use(bodyParser.json());

app.use('/products', productRoutes);
app.use('/customers', customerRoutes);

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}/`);
});
```

#### Exercício 2: Validação de Dados

**Instale a biblioteca joi:**
```sh
npm install joi
```

**middleware/validation.js**
```javascript
const Joi = require('joi');

const productSchema = Joi.object({
    name: Joi.string().required(),
    price: Joi.number().required(),
    stock: Joi.number().required()
});

const validateProduct = (req, res, next) => {
    const { error } = productSchema.validate(req.body);
    if (error) {
        return res.status(400).send(error.details[0].message);
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
const mongoose = require('mongoose');
const productRoutes = require('./routes/products');
const customerRoutes = require('./routes/customers');
const { validateProduct } = require('./middleware/validation');

const app = express();
const port = 3000;

const mongoURI = 'mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority';

mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Conectado ao MongoDB Atlas'))
    .catch(err => console.error('Erro ao conectar ao MongoDB Atlas:', err));

app.use(bodyParser.json());

app.use('/products', validateProduct, productRoutes);
app.use('/customers', customerRoutes);

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}/`);
});
```

#### Exercício 3: Busca por Nome

**Atualize routes/products.js:**
```javascript
// Buscar produtos por nome
router.get('/search', async (req, res) => {
    const name = req.query.name;
    try {
        const products = await Product.find({ name: new RegExp(name, 'i') });
        res.json(products);
    } catch (err) {
        res.status(500).send('Erro ao buscar produtos');
    }
});
```

Para buscar produtos por nome, use a rota:
```
GET http://localhost:3000/products/search?name=NomeDoProduto
```

#### Exercício 4: Paginação

**Atualize routes/products.js:**
```javascript
// Recuperar todos os produtos com paginação
router.get('/', async (req, res) => {
    const { page = 1, limit = 10 } = req.query;
    try {
        const products = await Product.find()
            .skip((page - 1) * limit)
            .limit(Number(limit));
        res.json(products);
    } catch (err) {
        res.status(500).send('Erro ao recuperar produtos');
    }
});
```

Para recuperar produtos com paginação, use a rota:
```
GET http://localhost:3000/products?page=1&limit=10
```

#### Exercício 5: Autenticação com JWT

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
const mongoose = require('mongoose');
const productRoutes = require('./routes/products');
const customerRoutes = require('./routes/customers');
const { validateProduct } = require('./middleware/validation');
const { authenticateToken } = require('./middleware/auth');

const app = express();
const port = 3000;

const mongoURI = 'mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority';

mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Conectado ao MongoDB Atlas'))
    .catch(err => console.error('Erro ao conectar ao MongoDB Atlas:', err));

app.use(bodyParser.json());

app.use('/products', authenticateToken, validateProduct, productRoutes);
app.use('/customers', authenticateToken, customerRoutes);

app.post('/login', (req, res) => {
    const user = {
        id: 1,
        username: 'user',
        email: 'user@example.com'
    };
    const token = jwt.sign(user, 'your-secret-key');
    res.json({ token });
});

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}/`);
});
```

Para gerar um token de autenticação, use a rota:
```
POST http://localhost:3000/login
```
Body da requisição:
```json
{
    "username": "user",
    "password": "password"
}
```

Na resposta, você receberá um token que pode ser usado para acessar as rotas protegidas.