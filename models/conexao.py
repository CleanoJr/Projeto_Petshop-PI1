from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


# URL de conexão com o banco de dados MySQL no XAMPP
DATABASE_URL = "mysql+pymysql://root:@localhost/petshop_db"


# Conexão com o banco de dados MySQL usando SQLAlchemy
engine = create_engine(DATABASE_URL, echo=False)

# Configura o gerenciador de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os modelos
Base = declarative_base()