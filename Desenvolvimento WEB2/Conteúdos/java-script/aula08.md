### Aula 8: Bancos de Dados e Node.js

#### Objetivos
- Integrar bancos de dados com Node.js.
- Utilizar a biblioteca Mongoose para interação com bancos MongoDB no MongoDB Atlas.

### Introdução

MongoDB é um banco de dados NoSQL popular, ideal para aplicações que lidam com grandes volumes de dados não estruturados. O Mongoose é uma biblioteca de Node.js que facilita a interação com MongoDB, proporcionando uma estrutura robusta para esquemas e validação de dados.

### Instalando Mongoose

Inicie um novo projeto Node.js e instale o Mongoose:

```sh
mkdir node-mongo
cd node-mongo
npm init -y
npm install mongoose
```

### Conectando ao MongoDB Atlas

#### app.js

```javascript
const mongoose = require('mongoose');

// Substitua '<username>', '<password>' e '<dbname>' com suas credenciais do MongoDB Atlas
const dbURI = 'mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority';

mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then((result) => console.log('Conectado ao MongoDB'))
    .catch((err) => console.log(err));

const express = require('express');
const app = express();
const port = 3000;

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}/`);
});
```

### Definindo um Modelo com Mongoose

Um modelo em Mongoose define a estrutura dos documentos no MongoDB.

#### models/product.js

```javascript
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const productSchema = new Schema({
    name: {
        type: String,
        required: true
    },
    price: {
        type: Number,
        required: true
    },
    stock: {
        type: Number,
        required: true
    }
}, { timestamps: true });

const Product = mongoose.model('Product', productSchema);

module.exports = Product;
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
        res.status(500).json({ message: err.message });
    }
});

// Recuperar um produto por ID
router.get('/:id', async (req, res) => {
    try {
        const product = await Product.findById(req.params.id);
        if (product == null) {
            return res.status(404).json({ message: 'Produto não encontrado' });
        }
        res.json(product);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Criar um novo produto
router.post('/', async (req, res) => {
    const product = new Product({
        name: req.body.name,
        price: req.body.price,
        stock: req.body.stock
    });

    try {
        const newProduct = await product.save();
        res.status(201).json(newProduct);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Atualizar um produto existente
router.put('/:id', async (req, res) => {
    try {
        const product = await Product.findById(req.params.id);
        if (product == null) {
            return res.status(404).json({ message: 'Produto não encontrado' });
        }

        if (req.body.name != null) {
            product.name = req.body.name;
        }
        if (req.body.price != null) {
            product.price = req.body.price;
        }
        if (req.body.stock != null) {
            product.stock = req.body.stock;
        }

        const updatedProduct = await product.save();
        res.json(updatedProduct);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Excluir um produto
router.delete('/:id', async (req, res) => {
    try {
        const product = await Product.findById(req.params.id);
        if (product == null) {
            return res.status(404).json({ message: 'Produto não encontrado' });
        }

        await product.remove();
        res.json({ message: 'Produto excluído' });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

module.exports = router;
```

### Integrando as Rotas ao Servidor

#### app.js (atualizado)

```javascript
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const productRoutes = require('./routes/products');

const app = express();
const port = 3000;

// Substitua '<username>', '<password>' e '<dbname>' com suas credenciais do MongoDB Atlas
const dbURI = 'mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority';

mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then((result) => console.log('Conectado ao MongoDB'))
    .catch((err) => console.log(err));

app.use(bodyParser.json());
app.use('/products', productRoutes);

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}/`);
});
```

### Exercícios Práticos

1. **Adicione um campo "categoria" ao modelo de produto e ajuste as rotas para manipular este novo campo.**

**models/product.js (atualizado)**
```javascript
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const productSchema = new Schema({
    name: {
        type: String,
        required: true
    },
    price: {
        type: Number,
        required: true,
        min: 0
    },
    stock: {
        type: Number,
        required: true,
        min: 0
    },
    category: {
        type: String,
        required: true
    }
}, { timestamps: true });

const Product = mongoose.model('Product', productSchema);

module.exports = Product;
```

**routes/products.js (atualizado)**
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
        res.status(500).json({ message: err.message });
    }
});

// Recuperar um produto por ID
router.get('/:id', async (req, res) => {
    try {
        const product = await Product.findById(req.params.id);
        if (product == null) {
            return res.status(404).json({ message: 'Produto não encontrado' });
        }
        res.json(product);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Criar um novo produto
router.post('/', async (req, res) => {
    const product = new Product({
        name: req.body.name,
        price: req.body.price,
        stock: req.body.stock,
        category: req.body.category
    });

    try {
        const newProduct = await product.save();
        res.status(201).json(newProduct);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Atualizar um produto existente
router.put('/:id', async (req, res) => {
    try {
        const product = await Product.findById(req.params.id);
        if (product == null) {
            return res.status(404).json({ message: 'Produto não encontrado' });
        }

        if (req.body.name != null) {
            product.name = req.body.name;
        }
        if (req.body.price != null) {
            product.price = req.body.price;
        }
        if (req.body.stock != null) {
            product.stock = req.body.stock;
        }
        if (req.body.category != null) {
            product.category = req.body.category;
        }

        const updatedProduct = await product.save();
        res.json(updatedProduct);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Excluir um produto
router.delete('/:id', async (req, res) => {
    try {
        const product = await Product.findById(req.params.id);
        if (product == null) {
            return res.status(404).json({ message: 'Produto não encontrado' });
        }

        await product.remove();
        res.json({ message

: 'Produto excluído' });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

module.exports = router;
```

2. **Crie um novo modelo para representar clientes, com atributos como nome, email e endereço. Implemente as rotas CRUD para este modelo.**

**models/client.js**
```javascript
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const clientSchema = new Schema({
    name: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true,
        unique: true
    },
    address: {
        type: String,
        required: true
    }
}, { timestamps: true });

const Client = mongoose.model('Client', clientSchema);

module.exports = Client;
```

**routes/clients.js**
```javascript
const express = require('express');
const router = express.Router();
const Client = require('../models/client');

// Recuperar todos os clientes
router.get('/', async (req, res) => {
    try {
        const clients = await Client.find();
        res.json(clients);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Recuperar um cliente por ID
router.get('/:id', async (req, res) => {
    try {
        const client = await Client.findById(req.params.id);
        if (client == null) {
            return res.status(404).json({ message: 'Cliente não encontrado' });
        }
        res.json(client);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Criar um novo cliente
router.post('/', async (req, res) => {
    const client = new Client({
        name: req.body.name,
        email: req.body.email,
        address: req.body.address
    });

    try {
        const newClient = await client.save();
        res.status(201).json(newClient);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Atualizar um cliente existente
router.put('/:id', async (req, res) => {
    try {
        const client = await Client.findById(req.params.id);
        if (client == null) {
            return res.status(404).json({ message: 'Cliente não encontrado' });
        }

        if (req.body.name != null) {
            client.name = req.body.name;
        }
        if (req.body.email != null) {
            client.email = req.body.email;
        }
        if (req.body.address != null) {
            client.address = req.body.address;
        }

        const updatedClient = await client.save();
        res.json(updatedClient);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Excluir um cliente
router.delete('/:id', async (req, res) => {
    try {
        const client = await Client.findById(req.params.id);
        if (client == null) {
            return res.status(404).json({ message: 'Cliente não encontrado' });
        }

        await client.remove();
        res.json({ message: 'Cliente excluído' });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

module.exports = router;
```

3. **Adicione validação de dados para garantir que o preço de um produto seja maior que zero e que o estoque não seja negativo.**

**models/product.js (atualizado)**
```javascript
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const productSchema = new Schema({
    name: {
        type: String,
        required: true
    },
    price: {
        type: Number,
        required: true,
        min: 0
    },
    stock: {
        type: Number,
        required: true,
        min: 0
    },
    category: {
        type: String,
        required: true
    }
}, { timestamps: true });

const Product = mongoose.model('Product', productSchema);

module.exports = Product;
```

4. **Implemente uma rota para pesquisar produtos por categoria.**

**routes/products.js (adicionar rota)**
```javascript
// Recuperar produtos por categoria
router.get('/category/:category', async (req, res) => {
    try {
        const products = await Product.find({ category: req.params.category });
        res.json(products);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});
```

### Conclusão

Nesta semana, você aprendeu a integrar bancos de dados MongoDB com Node.js usando Mongoose, criando e manipulando dados de forma eficiente. Esses conceitos são fundamentais para o desenvolvimento de aplicações web escaláveis e robustas.