from sqlalchemy import Numeric, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.conexao import *


class Funcionario(Base):
    __tablename__ = "funcionario"

    employee_id = Column("client_id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(100), nullable=False)
    role = Column("role", String(50), nullable=False)
    phone = Column("phone", String(15), nullable=False)
    salary = Column("salary", Numeric(10, 2), nullable=False)
    created_at = Column("created at", TIMESTAMP, server_default=func.current_timestamp())

    def __init__(self, name, role, phone, salary):
        self.name = name
        self.role = role
        self.phone = phone
        self.salary = salary

Base.metadata.create_all(bind=engine)