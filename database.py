
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
load_dotenv()

# Configuración de conexión
# Reemplazá 'TU_PASSWORD' con la contraseña de tu usuario root de MySQL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:admin123@127.0.0.1:3306/cafeteria_db"

# Motor de SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Fábrica de sesiones para interactuar con la DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base de la que heredarán nuestros modelos
Base = declarative_base()

# Dependencia para usar en los endpoints (FastAPI)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()