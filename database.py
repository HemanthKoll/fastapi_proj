from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
DATABASE_USER="postgres"
DATABASE_PASSWORD="xelpmoc"
DATABASE_NAME="newone"
engine=create_engine(f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}",
    echo=True

)

Base=declarative_base()

Session=sessionmaker()