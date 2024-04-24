## Tutorial: Instalação e Configuração do PostgreSQL e pgAdmin no Ubuntu 22.04

Este tutorial apresenta um passo a passo para a instalação e configuração do PostgreSQL e do pgAdmin no Ubuntu 22.04. Inclui também instruções para alterar a senha do usuário "postgres" e configurar o PostgreSQL para acesso remoto.

### Parte 1: Instalação do PostgreSQL

1. **Atualize o Sistema**
   Abra um terminal e atualize o sistema para garantir que todos os pacotes estejam atualizados:
   ```bash
   sudo apt update && sudo apt upgrade
   ```

2. **Instale o PostgreSQL e Componentes Adicionais**
   Para instalar o PostgreSQL e seus componentes adicionais, execute o seguinte comando:
   ```bash
   sudo apt install postgresql postgresql-contrib
   ```

3. **Verifique a Instalação**
   Após a instalação, verifique se o serviço do PostgreSQL está em execução:
   ```bash
   sudo systemctl status postgresql
   ```

   Se o serviço estiver ativo e em execução, você verá uma mensagem indicando que o PostgreSQL está funcionando corretamente.

### Parte 2: Configuração para Acesso Remoto no PostgreSQL

1. **Edite o Arquivo 'pg_hba.conf'**
   Para permitir conexões remotas, é necessário editar o arquivo 'pg_hba.conf':
   ```bash
   sudo mousepad /etc/postgresql/14/main/pg_hba.conf
   ```

2. **Adicione uma Entrada para Acesso Remoto**
   No arquivo 'pg_hba.conf', adicione uma linha que permita conexões de uma faixa de endereços IP. Por exemplo, para permitir conexões de qualquer endereço na rede local (como 192.168.0.0/24), adicione:
   ```bash
   host all all 192.168.0.0/24 md5
   ```

   Após adicionar a linha, salve e feche o arquivo (Ctrl+O para salvar, Ctrl+X para sair).

3. **Edite o Arquivo 'postgresql.conf'**
   Para permitir que o PostgreSQL escute em todos os endereços IP, edite o arquivo 'postgresql.conf':
   ```bash
   sudo mousepad /etc/postgresql/14/main/postgresql.conf
   ```

   Encontre a linha `#listen_addresses = 'localhost'` e altere para:
   ```bash
   listen_addresses = '*'
   ```

   Salve e feche o arquivo.

4. **Reinicie o PostgreSQL**
   Para aplicar as alterações, reinicie o serviço do PostgreSQL:
   ```bash
   sudo systemctl restart postgresql
   ```

### Parte 3: Alteração da Senha do Usuário 'postgres'

1. **Acesse o Shell do PostgreSQL**
   Para alterar a senha do usuário "postgres", primeiro acesse o shell do PostgreSQL:
   ```bash
   sudo -i -u postgres
   psql
   ```

2. **Altere a Senha do Usuário 'postgres'**
   No shell do PostgreSQL, altere a senha do usuário "postgres":
   ```sql
   ALTER ROLE postgres WITH PASSWORD 'nova_senha_segura';
   ```

3. **Saia do Shell do PostgreSQL**
   Após alterar a senha, saia do shell:
   ```bash
   \q
   exit
   ```

4. **Reinicie o PostgreSQL**
   Reinicie o PostgreSQL para garantir que a alteração seja aplicada corretamente:

   ```bash
   sudo systemctl restart postgresql
   ```


### Parte 4: Instalação e Configuração do pgAdmin

1. **Adicione a Chave do Repositório do pgAdmin**
   Antes de adicionar o repositório, obtenha a chave de autenticação:
   ```bash
   wget --quiet -O - https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add -
   ```

2. **Adicione o Repositório do pgAdmin**
   Após adicionar a chave, adicione o repositório oficial ao Ubuntu:
   ```bash
   sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/jammy pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
   ```

3. **Instale o pgAdmin**
   Com o repositório adicionado, instale o pgAdmin:
   ```bash
   sudo apt install pgadmin4
   ```

4. **Inicie o pgAdmin**
   Para iniciar o pgAdmin, procure pelo ícone do aplicativo no menu do Ubuntu ou execute o comando a seguir:
   ```bash
   pgadmin4
   ```


### Parte 5: Conexão ao PostgreSQL via pgAdmin

1. **Adicione um Novo Servidor**
   No pgAdmin, clique em "Add New Server" para adicionar um novo servidor PostgreSQL.

2. **Configuração do Servidor**
   - **Name:** Escolha um nome para o servidor (por exemplo, "Meu PostgreSQL").
   - **Connection:** 
     - **Host name/address:** Insira o endereço IP do servidor PostgreSQL.
     - **Port:** Mantenha a porta padrão (5432).
     - **Username:** Insira "postgres".
     - **Password:** Insira a senha que você acabou de alterar.

3. **Teste a Conexão**
   Após preencher as informações, clique em "Save" para testar a conexão. Se tudo estiver configurado corretamente, você verá o servidor adicionado ao pgAdmin.

---

### Questionário de Avaliação: Instalação e Configuração do PostgreSQL e pgAdmin no Ubuntu 22.04

Aluno: ________________________________________________________

#### Questão 1
Qual é o comando para instalar o PostgreSQL e seus componentes no Ubuntu 22.04?
- A) `sudo apt-get install postgresql`
- B) `sudo apt install postgresql postgresql-contrib`
- C) `sudo apt install postgresql-server`
- D) `sudo apt-get install postgresql-client`

**Resposta correta:** B) `sudo apt install postgresql postgresql-contrib`

#### Questão 2
Qual comando permite trocar para o usuário "postgres" no terminal do Ubuntu?
- A) `sudo -u postgres`
- B) `sudo -s postgres`
- C) `sudo -i -u postgres`
- D) `su postgres`

**Resposta correta:** C) `sudo -i -u postgres`

#### Questão 3
Para permitir conexões remotas ao PostgreSQL, qual linha deve ser alterada no arquivo 'postgresql.conf'?
- A) `listen_addresses = '*'`
- B) `#listen_addresses = 'localhost'`
- C) `listen_addresses = '0.0.0.0'`
- D) `listen_addresses = '127.0.0.1'`

**Resposta correta:** A) `listen_addresses = '*'`

#### Questão 4
Qual arquivo deve ser editado para configurar a permissão de conexões remotas por faixa de IP no PostgreSQL?
- A) `postgresql.conf`
- B) `pg_hba.conf`
- C) `pg_ident.conf`
- D) `pg_network.conf`

**Resposta correta:** B) `pg_hba.conf`

#### Questão 5
Qual comando é usado para alterar a senha do usuário "postgres" no shell do PostgreSQL?
- A) `UPDATE ROLE postgres SET PASSWORD 'nova_senha';`
- B) `ALTER USER postgres WITH PASSWORD 'nova_senha';`
- C) `ALTER ROLE postgres WITH PASSWORD 'nova_senha_segura';`
- D) `SET PASSWORD 'nova_senha';`

**Resposta correta:** C) `ALTER ROLE postgres WITH PASSWORD 'nova_senha_segura';`

#### Questão 6
Para adicionar um repositório do pgAdmin no Ubuntu, qual comando é necessário?
- A) `sudo add-apt-repository 'deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/jammy pgadmin4 main'`
- B) `sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/jammy pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'`
- C) `sudo apt-add-repository 'deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/jammy pgadmin4 main'`
- D) `sudo add-apt-repository pgadmin4 && apt update`

**Resposta correta:** B) `sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/jammy pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'`

---

Essas questões cobrem aspectos importantes da instalação e configuração do PostgreSQL e pgAdmin no Ubuntu 22.04, ajudando a fixar os conceitos básicos apresentados na atividade. Se precisar de mais questões ou atividades, posso criar mais para você.