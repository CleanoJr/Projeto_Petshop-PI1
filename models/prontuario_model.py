from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from models.conexao import Base, engine

class Prontuario(Base):
    __tablename__ = 'prontuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    paciente = Column(String(100), nullable=False)
    tutor = Column(String(100), nullable=False)
    raca = Column(String(50), nullable=False)
    especie = Column(String(50), nullable=False)
    peso = Column(Float, nullable=False)
    sexo = Column(String(10), nullable=False)
    nascimento = Column(DateTime, nullable=False)
    data_consulta = Column(DateTime, nullable=False)
    conteudo = Column(Text, nullable=False)

    def __init__(self, paciente, tutor, raca, especie, peso, sexo, nascimento, data_consulta, conteudo):
        self.paciente = paciente
        self.tutor = tutor
        self.raca = raca
        self.especie = especie
        self.peso = peso
        self.sexo = sexo
        self.nascimento = nascimento
        self.data_consulta = data_consulta
        self.conteudo = conteudo

# Cria a tabela no banco de dados
Base.metadata.create_all(bind=engine)