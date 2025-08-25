import database
import models

database.Base.metadata.create_all(bind=database.engine)
print("Banco de dados criado com sucesso.")