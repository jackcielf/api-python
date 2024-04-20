from passlib.context import CryptContext
from validators import validate_email, validate_telefone
from sqlalchemy.orm import validates
from sqlalchemy.sql import func
from config import db
import uuid

# Cria um contexto de criptografia com o esquema bcrypt_sha256
crypt_context = CryptContext(schemes=['bcrypt_sha256'])

class User(db.Model):
  __tablename__ = 'tb_usuario' # Define um nome para a tabela (Opcional)
  id_usuario = db.Column(db.String(32), primary_key=True, default=lambda: str(uuid.uuid4()).replace('-', ''))
  nome = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  senha = db.Column(db.String(255), nullable=False)
  telefone = db.Column(db.String(15), nullable=False)
  genero = db.Column(db.Enum('masculino', 'feminino'))
  data_nas = db.Column(db.Date, nullable=False)
  created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)

  def __init__(self, nome, email, senha, telefone, genero, data_nas):
    self.nome = nome
    self.email = email
    self.senha = crypt_context.hash(senha)
    self.telefone = telefone
    self.genero = genero
    self.data_nas = data_nas

  def verify_senha(self, senha):
    return crypt_context.verify(senha, self.senha)
  
  def __repr__(self) -> str:
    return f"<User: { self.nome }>"
  
  @validates('email')
  def validate_email(self, key, email): # "key" não é usado, mas precisa estar na função
    return validate_email(email)

  @validates('telefone')
  def validate_telefone(self, key, telefone):
    return validate_telefone(telefone)