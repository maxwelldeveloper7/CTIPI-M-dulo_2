### Semana 9-10: Introdução ao Node.js

#### Objetivos
- Compreender os conceitos fundamentais do ambiente de execução Node.js.
- Configurar e instalar o ambiente Node.js.

### O que é Node.js?

Node.js é um ambiente de execução JavaScript baseado no motor V8 do Google Chrome. Ele permite que você execute JavaScript no lado do servidor, fora do navegador. Node.js é amplamente utilizado para criar aplicativos de rede escaláveis e de alto desempenho.

#### Características do Node.js
- **Event-driven**: Node.js usa um modelo de E/S assíncrono baseado em eventos, tornando-o eficiente e leve.
- **Single-threaded**: Utiliza um único thread para gerenciar todas as operações, mas usa operações assíncronas para lidar com múltiplas conexões simultaneamente.
- **Non-blocking I/O**: Permite que operações de entrada e saída sejam executadas em segundo plano sem bloquear o thread principal.

### Instalação do Node.js

#### Passo 1: Verificar a versão do Node.js

Antes de instalar o Node.js, verifique se ele já está instalado no seu sistema. Abra o terminal e digite:
```sh
node -v
```
Se Node.js estiver instalado, ele retornará a versão instalada. Caso contrário, você verá um erro indicando que o comando não foi encontrado.

#### Passo 2: Instalar o Node.js no Ubuntu

1. **Atualize o gerenciador de pacotes:**
   ```sh
   sudo apt update
   ```

2. **Instale o Node.js e npm (Node Package Manager):**
   ```sh
   sudo apt install nodejs npm
   ```

3. **Verifique a instalação:**
   ```sh
   node -v
   npm -v
   ```

### Primeiro Script em Node.js

Crie um novo arquivo chamado `app.js` e adicione o seguinte código:
```javascript
console.log('Hello, Node.js!');
```

Para executar o script, abra o terminal, navegue até o diretório onde o arquivo está localizado e digite:
```sh
node app.js
```
Você deverá ver a mensagem `Hello, Node.js!` no terminal.

### Módulos em Node.js

Node.js possui um sistema de módulos que permite incluir módulos no seu aplicativo. Um dos módulos mais comuns é o `http`, que permite criar um servidor web simples.

#### Exemplo de Servidor HTTP

Crie um novo arquivo chamado `server.js` e adicione o seguinte código:
```javascript
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
```

Para executar o servidor, digite:
```sh
node server.js
```
Abra um navegador e vá para `http://127.0.0.1:3000/`. Você verá a mensagem `Hello, World!`.

### Trabalhando com Pacotes usando npm

O npm (Node Package Manager) é o gerenciador de pacotes padrão para Node.js. Ele permite que você instale pacotes de terceiros e gerencie dependências do seu projeto.

#### Inicializando um Projeto Node.js

1. **Crie um diretório para seu projeto:**
   ```sh
   mkdir myproject
   cd myproject
   ```

2. **Inicialize o projeto com npm:**
   ```sh
   npm init -y
   ```
   Isso criará um arquivo `package.json` com as configurações padrão.

#### Instalando um Pacote

Vamos instalar o pacote `express`, um framework para Node.js:
```sh
npm install express
```

### Exemplo de Aplicativo com Express

Crie um arquivo chamado `app.js` e adicione o seguinte código:
```javascript
const express = require('express');
const app = express();

const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello, Express!');
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
```

Para executar o aplicativo, digite:
```sh
node app.js
```
Abra um navegador e vá para `http://localhost:3000/`. Você verá a mensagem `Hello, Express!`.

### Exercícios Práticos

1. **Instale Node.js e npm no seu sistema, se ainda não o fez. Verifique as versões instaladas.**
   - Comando para verificar a versão do Node.js: `node -v`
   - Comando para verificar a versão do npm: `npm -v`

- Verificação das versões do Node.js e npm:
   ```sh
   node -v
   npm -v
   ```

2. **Crie um script Node.js simples que exiba a data e hora atuais no console.**
   - Dica: Use `console.log(new Date())` para obter a data e hora atuais.

- Script Node.js para exibir data e hora atuais (`date.js`):
   ```javascript
   console.log(new Date());
   ```
-Executar no terminal:
   ```sh
   node date.js
   ```

3. **Crie um servidor HTTP básico que responda com "Olá, Mundo!" para qualquer requisição.**
   - Use o módulo `http` do Node.js.

- Servidor HTTP básico (`server.js`):
   ```javascript
   const http = require('http');

   const hostname = '127.0.0.1';
   const port = 3000;

   const server = http.createServer((req, res) => {
     res.statusCode = 200;
     res.setHeader('Content-Type', 'text/plain');
     res.end('Olá, Mundo!\n');
   });

   server.listen(port, hostname, () => {
     console.log(`Server running at http://${hostname}:${port}/`);
   });
   ```
   Executar no terminal:
   ```sh
   node server.js
   ```


4. **Inicialize um novo projeto Node.js e instale o pacote `express`. Crie um aplicativo básico que responda com "Hello, Express!" para requisições na raiz ("/").**

- Inicialização de projeto e instalação do pacote `express`:
   ```sh
   mkdir myproject
   cd myproject
   npm init -y
   npm install express
   ```

5. **Personalize a resposta do seu servidor Express para exibir "Bem-vindo ao meu site!" na página inicial.**

- Personalização da resposta do servidor Express (`app.js`):**
   ```javascript
   const express = require('express');
   const app = express();

   const port = 3000;

   app.get('/', (req, res) => {
     res.send('Bem-vindo ao meu site!');
   });

   app.listen(port, () => {
     console.log(`Server running at http://localhost:${port}/`);
   });
   ```
- Executar no terminal:
   ```sh
   node app.js
   ```
