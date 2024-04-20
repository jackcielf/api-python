from validators import validate_email, validate_telefone
from sqlalchemy.orm import validates
from config import db
import uuid

class User(db.Model):
  __tablename__ = 'tb_usuario' # Define um nome para a tabela (Opcional)
  id_usuario = db.Column(db.String(32), primary_key=True, default=lambda: str(uuid.uuid4()).replace('-', ''))
  nome = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  telefone = db.Column(db.String(15))
  genero = db.Column(db.Enum('masculino', 'feminino'))
  
  @validates('email')
  def validate_email(self, key, email): # "key" não é usado, mas precisa estar na função
    return validate_email(email)

  @validates('telefone')
  def validate_telefone(self, key, telefone):
    return validate_telefone(telefone)