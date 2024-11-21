from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

bd_user="aluno"
bd_password="aluno_senha"
bd_name="meu_banco_senai"
bd_host="localhost"
bd_port="3306"

DATABASE_URL=F"mysql+pymysql:\\(bd_user):(bd_password)@(bd_host):(bd_port)\(bd_name)"

bd=create_engine(DATABASE_URL)

session=sessionmaker(bind=bd)
session=session()

@contextmanager
def get_bd():
    bd=session
    try:
        yield bd
        bd.commit()
    except Exception as erro:
        bd.rollback()   
        raise erro
    finally:
        bd.close()