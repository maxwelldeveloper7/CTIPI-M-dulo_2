**Vamos refatorar o CRUD em funções para melhor organizar o Código**

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

# Função para criar o banco de dados e as tabelas
def criar_banco_e_tabelas():
    Base.metadata.create_all(engine)

# Funções para inserir, consultar, atualizar e excluir registros
def inserir_responsavel():
    pass  # Implemente a função para inserir um responsável

def inserir_crianca():
    pass  # Implemente a função para inserir uma criança

def consultar_responsaveis():
    pass  # Implemente a função para consultar todos os responsáveis e suas crianças

def atualizar_responsavel():
    pass  # Implemente a função para atualizar um responsável

def excluir_crianca():
    pass  # Implemente a função para excluir uma criança

# Função para exibir o menu e interagir com o usuário
def exibir_menu():
    while True:
        print("\n=== Menu ===")
        print("1. Inserir Responsável")
        print("2. Inserir Criança")
        print("3. Consultar Responsáveis e Crianças")
        print("4. Atualizar Responsável")
        print("5. Excluir Criança")
        print("6. Sair do Programa")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_responsavel()
        elif opcao == '2':
            inserir_crianca()
        elif opcao == '3':
            consultar_responsaveis()
        elif opcao == '4':
            atualizar_responsavel()
        elif opcao == '5':
            excluir_crianca()
        elif opcao == '6':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamada do menu para iniciar o programa
if __name__ == "__main__":
    criar_banco_e_tabelas()
    exibir_menu()

```

Agora a função `criar_banco_e_tabelas()` será chamada automaticamente quando o programa for iniciado, antes do menu ser exibido.