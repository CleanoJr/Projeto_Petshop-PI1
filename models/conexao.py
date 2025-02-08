from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# URL de conexão com o banco de dados MySQL no XAMPP
DATABASE_URL = "mysql+pymysql://root:@localhost/petshop_db"


# Conexão com o banco de dados MySQL usando SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()