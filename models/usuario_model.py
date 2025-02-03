from models.conexao import *


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(200))
    login = Column("login", String(200))
    senha = Column("senha", String(15))
    email = Column("email", String(100))
    telefone = Column("telefone", String(15))
    
    #A funçao __init__ serve para inicializar a classe (construtor da classe)
    def __init__(self, nome, login, senha, email, telefone):
        self.nome = nome
        self.login  = login
        self.senha = senha
        self.email = email
        self.telefone = telefone


# Criando as tabelas no banco de dados (caso não existam)
Base.metadata.create_all(bind=engine)