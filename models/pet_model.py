import uuid
from sqlalchemy import Date, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.conexao import *

class Pet(Base):
    __tablename__ = "pets"

    pet_id = Column("pet_id", String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column("name", String(100), nullable=False)
    species = Column("species", String(50), nullable=False)
    breed = Column("breed", String(50), nullable=False)
    birth_date = Column("birth_date", Date, nullable=False)
    client_id = Column(String(36), ForeignKey('cliente.client_id'), nullable=False)
    created_at = Column("created_at",TIMESTAMP, server_default=func.current_timestamp())

    # Relacionamento reverso com o Cliente
    cliente = relationship("Cliente", back_populates="pets")

    def __init__(self, name, species, breed, birth_date, client_id):
        self.name = name
        self.species = species
        self.breed = breed
        self.birth_date = birth_date
        self.client_id = client_id