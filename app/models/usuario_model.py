from sqlalchemy import column,String,Integer
from sqlalchemy.orm import declarative_base
from config.database import bd

base=declarative_base()


class usuario(base):
    _tablename_="usuarios"

    id= column(Integer, primary_key=True, autoincrement=True)
    nome=column(String(150))
    email=column(String)(150)
    senha=column(String)(150)

    def _init_(self, nome:str, email: str,senha:str:):
self.nome=nome
self.email=email
self.senha=senha


base.matadata.cerate_all(bind_bd)


