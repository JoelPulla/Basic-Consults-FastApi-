import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



sql_file_name = '../database.sqlite'

#  (será nuestra url del archivo de sqlite).
base_dir = os.path.dirname(os.path.realpath(__file__))

# une un string adicional con lo que declarameos de la ruta y nombre del archivo
database_url = f"sqlite:///{os.path.join(base_dir, sql_file_name)}"

# crea una instancia del resultado de lo que devuelve la funcion create_engine(
engine = create_engine(database_url, echo= True)

# guarda la session creada a partir del engine.
Session = sessionmaker(bind=engine)



Base = declarative_base()