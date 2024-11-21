from models.usuario_model import usuario
from slqlalchemy.orm import session

class usuario repository:
 def _init_(self,usuario:usuario):
  self.session.add(usuario)
  self.session.connit