from passlib.context import CryptContext
from datetime import datetime
import re

crypt_context = CryptContext(schemes=['bcrypt_sha256'])

def validate_name(name):
  assert len(name) >= 3, "O nome deve ter no mínimo 3 caracteres"
  assert len(name) <= 100, "O nome deve ter no máximo 100 caracteres"
  return name

def validate_email(email):
  assert len(email) <= 120, "O email deve ter no máximo 120 caracteres"
  assert re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email), "E-mail inválido"
  return email

def validate_password(password):
  assert len(password) >= 7, "A senha deve ter no mínimo 7 caracteres"
  assert len(password) <= 255, "A senha deve ter no máximo 255 caracteres"
  password = crypt_context.hash(password)
  return password

def validate_fone(fone):
  assert len(fone) == 11, "O telefone deve ter 11 caracteres"
  assert re.match(r"^[1-9][0-9]{10}$", fone), "Telefone inválido"
  return fone

def validate_gender(gender):
  assert gender in [None, "1", "2"], "Gênero inválido"
  return gender

def validate_date_birth(date):
    try:
        date_obj = datetime.strptime(date, '%d-%m-%Y')
        assert date_obj <= datetime.now(), "Data de nascimento inválida"
        return date
    except ValueError:
        raise AssertionError("Data de nascimento inválida")