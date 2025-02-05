from sqlalchemy import Text, TIMESTAMP
from sqlalchemy.sql import func
from models.conexao import *


class Cliente(Base):
    __tablename__ = "clientes"

    client_id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(100), nullable=False)
    cpf = Column("cpf", String(14), unique=True, nullable=False)
    email = Column("email", String(100), nullable=False)
    phone = Column("phone", String(15), nullable=False)
    address = Column("address", Text, nullable=False)
    created_at = Column("created at", TIMESTAMP, server_default=func.current_timestamp())

    def __init__(self, name, cpf, email, phone, address):
        self.name = name
        self.cpf = cpf
        self.email = email
        self.phone = phone
        self.address = address


Base.metadata.create_all(bind=engine)