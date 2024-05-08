Criar uma atividade prática passo a passo é uma ótima maneira de envolver os alunos e permitir que eles aprendam por meio da prática. Vou preparar uma atividade detalhada que mostra como usar SQLAlchemy para criar e manipular um banco de dados SQLite para um sistema de inscrições em creches, seguindo o contexto da Secretaria Municipal de Educação.

---

## Atividade Prática: Criar um Sistema de Inscrição para Creches usando SQLAlchemy e SQLite

### Objetivo
Nesta atividade, você criará um sistema básico de inscrições para creches usando SQLAlchemy com SQLite. Você aprenderá a criar tabelas, inserir registros, consultar dados e realizar operações CRUD (Criar, Ler, Atualizar, Excluir).

### Pré-requisitos
- Python instalado
- SQLAlchemy instalado (instale com `pip install sqlalchemy`)
- Um ambiente para escrever e executar código Python (como Jupyter Notebook, Google Colab, ou um editor de texto com terminal)

### Passo 1: Configurar o Banco de Dados e a Sessão
Comece configurando a conexão com o banco de dados SQLite e criando a base para os modelos de dados.

```python
# Importar as bibliotecas necessárias
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Conectar ao banco de dados SQLite (cria se não existir)
engine = create_engine('sqlite:///creche.db')

# Base para nossos modelos
Base = declarative_base()

# Criar uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()
```

### Passo 2: Definir as Tabelas
Você criará duas tabelas: uma para "Responsáveis" (quem inscreve as crianças) e outra para "Crianças".

```python
# Definir a tabela para 'Responsáveis'
class Responsavel(Base):
    __tablename__ = 'responsaveis'

    id = Column(Integer, primary_key=True)  # Chave primária
    nome = Column(String, nullable=False)  # Nome do responsável
    endereco = Column(String)  # Endereço
    telefone = Column(String)  # Telefone

    # Relacionamento com crianças
    criancas = relationship("Crianca", back_populates="responsavel")

# Definir a tabela para 'Crianças'
class Crianca(Base):
    __tablename__ = 'criancas'

    id = Column(Integer, primary_key=True)  # Chave primária
    nome = Column(String, nullable=False)  # Nome da criança
    idade = Column(Integer, nullable=False)  # Idade da criança
    responsavel_id = Column(Integer, ForeignKey('responsaveis.id'))  # Chave estrangeira

    # Relacionamento com o responsável
    responsavel = relationship("Responsavel", back_populates="criancas")
```

### Passo 3: Criar as Tabelas no Banco de Dados
Agora, crie as tabelas no banco de dados para garantir que você tenha um local para armazenar as informações.

```python
# Criar todas as tabelas definidas
Base.metadata.create_all(engine)
```

### Passo 4: Inserir Registros no Banco de Dados
Vamos adicionar alguns registros para testar o banco de dados.

```python
# Adicionar responsáveis
resp1 = Responsavel(nome='Ana', endereco='Rua A, 123', telefone='1234-5678')
resp2 = Responsavel(nome='Bruna', endereco='Rua B, 456', telefone='2345-6789')

# Adicionar crianças para esses responsáveis
crianca1 = Crianca(nome='Pedro', idade=3, responsavel=resp1)
crianca2 = Crianca(nome='Maria', idade=4, responsavel=resp2)
crianca3 = Crianca(nome='Lucas', idade=2, responsavel=resp1)

# Adicionar ao banco de dados e salvar
session.add(resp1)
session.add(resp2)
session.commit()  # Sempre realizar commit para persistir alterações
```

### Passo 5: Consultar Dados no Banco de Dados
Agora, consulte os dados inseridos para verificar se estão corretos.

```python
# Consultar todos os responsáveis e suas crianças
todos_responsaveis = session.query(Responsavel).all()

for resp in todos_responsaveis:
    print(f"Responsável: {resp.nome}")
    for crianca in resp.criancas:
        print(f"  - Criança: {crianca.nome}, Idade: {crianca.idade}")
```

### Passo 6: Atualizar Dados no Banco de Dados
Faça uma atualização para um registro existente.

```python
# Atualizar o telefone do responsável Ana
resp_para_atualizar = session.query(Responsavel).filter_by(nome='Ana').first()
resp_para_atualizar.telefone = '8765-4321'

# Commit para salvar a alteração
session.commit()
```

### Passo 7: Excluir Registros do Banco de Dados
Para remover um registro do banco de dados, faça o seguinte:

```python
# Excluir a criança chamada Pedro
crianca_para_excluir = session.query(Crianca).filter_by(nome='Pedro').first()
session.delete(crianca_para_excluir)

# Commit para salvar a remoção
session.commit()
```

### Passo 8: Encerrar a Sessão
Finalmente, sempre feche a sessão após terminar todas as operações para garantir que o banco de dados seja fechado corretamente.

```python
session.close()
```

---

## Conclusão
Você criou um sistema básico de inscrições para creches usando SQLAlchemy e SQLite. Agora, é possível adicionar mais funcionalidades, como relações entre tabelas, validação de dados, e interações mais complexas. Siga estas etapas para aprender a trabalhar com bancos de dados em Python e SQLAlchemy.