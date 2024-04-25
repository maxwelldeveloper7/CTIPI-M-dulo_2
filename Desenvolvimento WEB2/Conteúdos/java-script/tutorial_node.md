**Tutorial: Preparando o Ambiente Node.js no Ubuntu e Configuração do Visual Studio Code**

Para começar a programar com Node.js no Ubuntu e usar o Visual Studio Code como editor, você precisará configurar o ambiente e instalar algumas extensões úteis. Este tutorial guiará você pelo processo.

### 1. Instalando Node.js no Ubuntu
Node.js é uma plataforma para execução de JavaScript no lado do servidor. Para instalá-lo no Ubuntu, siga estas etapas:

#### 1.1. Atualize os Pacotes do Sistema
Abra o terminal e execute o comando para garantir que seu sistema está atualizado:

```bash
sudo apt update && sudo apt upgrade
```

#### 1.2. Instale Node.js e npm
Node.js vem com o npm (Node Package Manager), que é usado para gerenciar pacotes e dependências do Node.js. Para instalar Node.js e npm, use o seguinte comando:

```bash
sudo apt install nodejs npm
```

Para verificar se a instalação foi bem-sucedida, execute:

```bash
node -v
npm -v
```

Esses comandos devem retornar as versões do Node.js e do npm instaladas no sistema.

### 2. Criando e Executando Arquivos JavaScript
Agora que você tem o Node.js e o VSCode instalados, vamos criar e executar um arquivo JavaScript simples.

#### 2.1. Crie um Novo Projeto
Crie uma nova pasta para seu projeto e abra-a no VSCode:

```bash
mkdir meu-projeto-node
cd meu-projeto-node
code .
```

#### 2.2. Crie um Arquivo JavaScript
No VSCode, clique em "Arquivo > Novo Arquivo" ou use o atalho `Ctrl+N`. Salve-o como `app.js`.

Adicione o seguinte código para um exemplo básico:

```javascript
console.log("Olá, mundo!");
```

#### 2.3. Execute o Arquivo JavaScript
Para executar um arquivo JavaScript com o Node.js, abra o terminal integrado no VSCode (`Ctrl+``) e execute:

```bash
node app.js
```

Você deve ver a saída "Olá, mundo!" no terminal.

### 3. Extensões Úteis para Visual Studio Code
Para melhorar sua experiência de desenvolvimento com Node.js no VSCode, considere instalar as seguintes extensões:

- **ESLint**: Para verificar erros de sintaxe e estilo de código.
- **Prettier - Code Formatter**: Para formatar automaticamente seu código.
- **Path Intellisense**: Para fornecer autocompletar para caminhos de arquivos e diretórios.
- **Node.js Extension Pack**: Um pacote com extensões úteis para desenvolvimento com Node.js.

### Conclusão
Seguindo este tutorial, você configurou um ambiente Node.js no Ubuntu e aprendeu a criar e executar arquivos JavaScript. As extensões recomendadas ajudarão a melhorar sua produtividade e qualidade do código. Boa sorte com seu desenvolvimento com Node.js!