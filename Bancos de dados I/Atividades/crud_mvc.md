Refatorar o código para seguir o padrão de projeto MVC (Model-View-Controller) para melhorar a organização e manutenção do código. Vamos dividir o código em três componentes principais:

1. **Model**: Contém as definições das tabelas e a lógica de banco de dados.
2. **View**: Responsável pela interface do usuário.
3. **Controller**: Contém a lógica de negócios e coordena as interações entre o Model e a View.

### Estrutura de Diretórios

Primeiro, vamos criar uma estrutura de diretórios:

```
project/
│
├── main.py
├── models/
│   └── __init__.py
│   └── models.py
├── views/
│   └── __init__.py
│   └── views.py
└── controllers/
    └── __init__.py
    └── controllers.py
```

### Model

`models/models.py`:

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# Conectar ao banco de dados SQLite (cria se não existir)
engine = create_engine('sqlite:///creche.db')

# Base para nossos modelos
Base = declarative_base()

# Criar uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Definir a tabela para 'Responsáveis'
class Responsavel(Base):
    __tablename__ = 'responsaveis'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    endereco = Column(String)
    telefone = Column(String)

    criancas = relationship("Crianca", back_populates="responsavel")

# Definir a tabela para 'Crianças'
class Crianca(Base):
    __tablename__ = 'criancas'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    responsavel_id = Column(Integer, ForeignKey('responsaveis.id'))

    responsavel = relationship("Responsavel", back_populates="criancas")

def criar_banco_e_tabelas():
    Base.metadata.create_all(engine)
```

### View

`views/views.py`:

```python
def menu_principal():
    print("\n=== Menu ===")
    print("1. Inserir Responsável")
    print("2. Inserir Criança")
    print("3. Consultar Responsáveis e Crianças")
    print("4. Atualizar Responsável")
    print("5. Excluir Criança")
    print("6. Sair do Programa")

    opcao = input("Escolha uma opção: ")
    return opcao

def input_responsavel():
    nome = input("Digite o nome do responsável: ")
    endereco = input("Digite o endereço do responsável: ")
    telefone = input("Digite o telefone do responsável: ")
    return nome, endereco, telefone

def input_crianca():
    nome = input("Digite o nome da criança: ")
    idade = int(input("Digite a idade da criança: "))
    responsavel_id = int(input("Digite o ID do responsável: "))
    return nome, idade, responsavel_id

def confirmar_exclusao(nome):
    confirmar = input(f"Tem certeza que deseja excluir a criança {nome}? (sim/não): ")
    return confirmar.lower() == 'sim'

def exibir_responsaveis(responsaveis):
    if not responsaveis:
        print("Nenhum responsável encontrado.")
    for responsavel in responsaveis:
        print(f"\nResponsável ID: {responsavel.id}")
        print(f"Nome: {responsavel.nome}")
        print(f"Endereço: {responsavel.endereco}")
        print(f"Telefone: {responsavel.telefone}")
        print("Crianças:")
        if not responsavel.criancas:
            print("  Nenhuma criança associada.")
        else:
            for crianca in responsavel.criancas:
                print(f"  Criança ID: {crianca.id}")
                print(f"  Nome: {crianca.nome}")
                print(f"  Idade: {crianca.idade}")

def input_id(mensagem):
    return int(input(mensagem))

def input_atualizacao(responsavel):
    novo_nome = input(f"Digite o novo nome (atual: {responsavel.nome}): ")
    novo_endereco = input(f"Digite o novo endereço (atual: {responsavel.endereco}): ")
    novo_telefone = input(f"Digite o novo telefone (atual: {responsavel.telefone}): ")
    return novo_nome, novo_endereco, novo_telefone
```

### Controller

`controllers/controllers.py`:

```python
from models.models import session, Responsavel, Crianca

def inserir_responsavel(nome, endereco, telefone):
    novo_responsavel = Responsavel(nome=nome, endereco=endereco, telefone=telefone)
    session.add(novo_responsavel)
    session.commit()

def inserir_crianca(nome, idade, responsavel_id):
    responsavel = session.query(Responsavel).filter_by(id=responsavel_id).first()
    if not responsavel:
        return False
    nova_crianca = Crianca(nome=nome, idade=idade, responsavel_id=responsavel_id)
    session.add(nova_crianca)
    session.commit()
    return True

def consultar_responsaveis():
    return session.query(Responsavel).all()

def atualizar_responsavel(responsavel_id, novo_nome, novo_endereco, novo_telefone):
    responsavel = session.query(Responsavel).filter_by(id=responsavel_id).first()
    if not responsavel:
        return False
    if novo_nome:
        responsavel.nome = novo_nome
    if novo_endereco:
        responsavel.endereco = novo_endereco
    if novo_telefone:
        responsavel.telefone = novo_telefone
    session.commit()
    return True

def excluir_crianca(crianca_id):
    crianca = session.query(Crianca).filter_by(id=crianca_id).first()
    if not crianca:
        return False
    session.delete(crianca)
    session.commit()
    return True
```

### Main

`main.py`:

```python
from models.models import criar_banco_e_tabelas
from views.views import (
    menu_principal, input_responsavel, input_crianca,
    confirmar_exclusao, exibir_responsaveis,
    input_id, input_atualizacao
)
import controllers.controllers as controller

def main():
    criar_banco_e_tabelas()

    while True:
        opcao = menu_principal()

        if opcao == '1':
            nome, endereco, telefone = input_responsavel()
            controller.inserir_responsavel(nome, endereco, telefone)
            print("Responsável inserido com sucesso!")

        elif opcao == '2':
            nome, idade, responsavel_id = input_crianca()
            if controller.inserir_crianca(nome, idade, responsavel_id):
                print("Criança inserida com sucesso!")
            else:
                print("Responsável não encontrado. Por favor, insira um ID de responsável válido.")

        elif opcao == '3':
            responsaveis = controller.consultar_responsaveis()
            exibir_responsaveis(responsaveis)

        elif opcao == '4':
            responsavel_id = input_id("Digite o ID do responsável a ser atualizado: ")
            responsavel = session.query(Responsavel).filter_by(id=responsavel_id).first()
            if not responsavel:
                print("Responsável não encontrado. Por favor, insira um ID de responsável válido.")
                continue
            novo_nome, novo_endereco, novo_telefone = input_atualizacao(responsavel)
            if controller.atualizar_responsavel(responsavel_id, novo_nome, novo_endereco, novo_telefone):
                print("Responsável atualizado com sucesso!")
            else:
                print("Erro ao atualizar o responsável.")

        elif opcao == '5':
            crianca_id = input_id("Digite o ID da criança a ser excluída: ")
            crianca = session.query(Crianca).filter_by(id=crianca_id).first()
            if not crianca:
                print("Criança não encontrada. Por favor, insira um ID de criança válido.")
                continue
            if confirmar_exclusao(crianca.nome):
                if controller.excluir_crianca(crianca_id):
                    print("Criança excluída com sucesso!")
                else:
                    print("Erro ao excluir a criança.")
            else:
                print("Exclusão cancelada.")

        elif opcao == '6':
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
```

### Resumo

1. **Model**: Define as classes e a lógica do banco de dados.
2. **View**: Contém todas as funções relacionadas à interface do usuário.
3. **Controller**: Implementa a lógica de negócios, manipulando os dados e atualizando a View.

Essa separação melhora a organização do código, facilita a manutenção e segue boas práticas de Clean Code e MVC.