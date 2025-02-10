from sqlalchemy import Text, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.conexao import *
from models.pet_model import Pet
from models.cliente_model import Cliente
from models.servicos_model import Servicos


class Produtos(Base):
    __tablename__ = "produtos"

    product_id = Column("product_id", Integer, primary_key=True, autoincrement=True)
    product_name = Column("product_name", String(100), nullable=False)
    description = Column("description", Text, nullable=False)
    price = Column("price", String(15), unique=True, nullable=False)   
    quantity = Column("quantity", String(15), unique=True, nullable=False)
    
     #Relacionamento 1:N
    produtos = relationship("produtos", back_populates="produtos")

    def __init__(self, name, description, price, quantify):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantify


Base.metadata.create_all(bind=engine)