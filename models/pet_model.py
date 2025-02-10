from sqlalchemy import Date, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.conexao import *

class Pets(Base):
    __tablename__ = "pets"

    pet_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    species = Column(String(50), nullable=False)
    breed = Column(String(50), nullable=False)
    birth_date = Column(Date, nullable=False)
    client_id = Column(Integer, ForeignKey("clientes.client_id"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())

    # Relacionamento reverso com o Cliente
    pets = relationship("Pets", back_populates="cliente")

    def __init__(self, name, species, breed, birth_date, client_id):
        self.name = name
        self.species = species
        self.breed = breed
        self.birth_date = birth_date
        self.client_id = client_id