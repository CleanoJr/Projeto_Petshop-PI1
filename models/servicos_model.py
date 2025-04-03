import uuid
from sqlalchemy import Text, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.conexao import *


class Servico(Base):
    __tablename__ = "servicos"

    service_id = Column("service_id", String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column("service_name", String(100), nullable=False)
    price = Column("price", Numeric(10, 2), nullable=False)
    description = Column("description", Text, nullable=False)
    


    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description


Base.metadata.create_all(bind=engine)