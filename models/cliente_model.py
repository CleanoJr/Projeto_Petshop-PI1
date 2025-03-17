import uuid
from sqlalchemy import Text, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.conexao import *
from models.pet_model import Pet


class Cliente(Base):
    __tablename__ = "cliente"

    client_id = Column("client_id", String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column("name", String(100), nullable=False)
    cpf = Column("cpf", String(14), unique=True, nullable=False)
    email = Column("email", String(100), nullable=False)
    phone = Column("phone", String(15), nullable=False)
    address = Column("address", Text, nullable=False)
    created_at = Column("created at", TIMESTAMP, server_default=func.current_timestamp())
    
     #Relacionamento 1:N
    pets = relationship("Pet", back_populates="cliente", cascade="all, delete-orphan")

    def __init__(self, name, cpf, email, phone, address):
        self.name = name
        self.cpf = cpf
        self.email = email
        self.phone = phone
        self.address = address


Base.metadata.create_all(bind=engine)