from sqlalchemy import Text, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.conexao import *


class Servico(Base):
    __tablename__ = "servicos"

    service_id = Column("service_id", Integer, primary_key=True, autoincrement=True)
    service_name = Column("service_name", String(100), nullable=False)
    price = Column("price", String(15), unique=True, nullable=False)
    description = Column("description", Text, nullable=False)
    


    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description


Base.metadata.create_all(bind=engine)