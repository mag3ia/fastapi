from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import session

# Se connecter à la base de données
# structure de l'URL pour Postgres : postgresql://<username>:<password>@<ip-address/hostname>/<database_name>
# To-Do: Secrets !
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:2YuHHakD7fy6tK88aHm2jd7cuKZMFbjsEBYoYGZtMHtX8BPBsLedxEx3mxvANaNWM8zQdqvPjE7oXZzp37KwhRv7iAd3LNwEVjJj58A27GPHeBPvwyBjWfNQwNvygg79@localhost/fastapi'

# Création du moteur (qui va connecter SQLAlchemy a la base Postgres)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative Mapping: Définie la classe 'Base', tous les modèles que nous définirons pour creer nos tables dans Postgress utiliseront cette classe.
Base = declarative_base()

# Dépendance :
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
