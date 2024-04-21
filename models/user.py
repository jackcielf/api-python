from passlib.context import CryptContext
from sqlalchemy.orm import validates
from sqlalchemy.sql import func
from validators import *
from config import db
import uuid

crypt_context = CryptContext(schemes=['bcrypt_sha256'])

class User(db.Model):
  __tablename__ = 'tb_usuario'
  id_usuario = db.Column(db.String(32), primary_key=True, default=lambda: str(uuid.uuid4()).replace('-', ''))
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(255), nullable=False)
  fone = db.Column(db.String(11))
  gender = db.Column(db.Enum('1', '2'))
  date_birth = db.Column(db.Date)
  created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)

  def __init__(self, name, email, password, fone, gender, date_birth):
    self.name = name
    self.email = email
    self.password = password
    self.fone = fone
    self.gender = gender
    self.date_birth = date_birth

  def verify_password(self, password) -> bool:
    return crypt_context.verify(password, self.password)
  
  @validates('name')
  def validate_name(self, key, name):
    return validate_name(name)
  
  @validates('email')
  def validate_email(self, key, email):
    return validate_email(email)

  @validates('password')
  def validate_password(self, key, password):
    return validate_password(password)
  
  @validates('fone')
  def validate_fone(self, key, fone):
    return validate_fone(fone)
  
  @validates('gender')
  def validate_gender(self, key, gender):
    return validate_gender(gender)
  
  @validates('date_birth')
  def validate_date_birth(self, key, date_birth):
    return validate_date_birth(date_birth)