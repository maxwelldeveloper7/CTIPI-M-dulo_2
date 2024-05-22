from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

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
    """
    Função para inserir um novo responsável no banco de dados.
    """
    # Obter dados do responsável
    nome = input("Digite o nome do responsável: ")
    endereco = input("Digite o endereço do responsável: ")
    telefone = input("Digite o telefone do responsável: ")

    # Criar uma nova instância de Responsavel
    novo_responsavel = Responsavel(
        nome=nome,
        endereco=endereco,
        telefone=telefone
    )

    # Adicionar à sessão e confirmar (commit)
    session.add(novo_responsavel)
    session.commit()
    print("Responsável inserido com sucesso!")


def inserir_crianca():
    """
    Função para inserir uma nova criança no banco de dados.
    """
    nome = input("Digite o nome da criança: ")
    idade = int(input("Digite a idade da criança: "))
    responsavel_id = int(input("Digite o ID do responsável: "))

    # Verificar se o responsável existe
    responsavel = session.query(Responsavel).filter_by(id=responsavel_id).first()
    if not responsavel:
        print("Responsável não encontrado. Por favor, insira um ID de responsável válido.")
        return

    # Criar uma nova instância de Crianca
    nova_crianca = Crianca(nome=nome, idade=idade, responsavel_id=responsavel_id)

    # Adicionar à sessão e confirmar (commit)
    session.add(nova_crianca)
    session.commit()
    print("Criança inserida com sucesso!")

def consultar_responsaveis():
    """
    Função para consultar todos os responsáveis e suas respectivas crianças.
    """
    responsaveis = session.query(Responsavel).all()

    if not responsaveis:
        print("Nenhum responsável encontrado.")
        return

    for responsavel in responsaveis:
        print(f"\nId: {responsavel.id}")
        print(f"Responsável: {responsavel.nome}")
        print(f"Endereço: {responsavel.endereco}")
        print(f"Telefone: {responsavel.telefone}")
        print(f"Crianças:")
        for crianca in responsavel.criancas:
            print(f"- {crianca.nome} ({crianca.idade} anos)")

def atualizar_responsavel():
    """
    Função para atualizar os dados de um responsável existente.
    """
    # Obter o ID do responsável
    responsavel_id = int(input("Digite o ID do responsável a ser atualizado: "))

    # Verificar se o responsável existe
    responsavel = session.query(Responsavel).filter_by(id=responsavel_id).first()
    if not responsavel:
        print(f"Responsável com ID {responsavel_id} não encontrado.")
        return

    # Obter novos dados do responsável
    novo_nome = input("Digite o novo nome do responsável (ou pressione Enter para manter o atual): ")
    novo_endereco = input("Digite o novo endereço do responsável (ou pressione Enter para manter o atual): ")
    novo_telefone = input("Digite o novo telefone do responsável (ou pressione Enter para manter o atual): ")

    # Atualizar os dados do responsável
    if novo_nome:
        responsavel.nome = novo_nome
    if novo_endereco:
        responsavel.endereco = novo_endereco
    if novo_telefone:
        responsavel.telefone = novo_telefone

    # Confirmar as alterações (commit)
    session.commit()
    print("Responsável atualizado com sucesso!")

def excluir_crianca():
    """
    Exclui uma criança do banco de dados, após confirmação do usuário.
    """
    crianca_id = int(input("Digite o ID da criança a ser excluída: "))
    crianca = session.query(Crianca).filter_by(id=crianca_id).first()

    if not crianca:
        print(f"Criança com ID {crianca_id} não encontrada.")
        return

    confirmar = input(f"Tem certeza que deseja excluir a criança {crianca.nome}? (sim/não): ")
    if confirmar.lower() != "sim":
        print("Exclusão cancelada.")
        return

    # Exclui a criança do banco de dados
    session.delete(crianca)
    session.commit()
    print(f"Criança {crianca.nome} excluída com sucesso!")

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
    try:
        criar_banco_e_tabelas()
        exibir_menu()
    finally:
        session.close()
        print("Sessão encerrada.")
