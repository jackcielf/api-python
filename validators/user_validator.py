import re

def validate_email(email):
  assert len(email) <= 120, "O email deve ter no máximo 120 caracteres."
  assert re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email), "E-mail inválido." # Ex: exemplo@dominio.com
  return email

def validate_telefone(telefone):
  assert len(telefone) <= 15, "O telefone deve ter no máximo 15 caracteres."
  assert re.match(r"^[1-9][0-9]{10}$", telefone), "Telefone inválido." # Ex: +55 (11) 98888-7777 ou 11988887777
  return telefone