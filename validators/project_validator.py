import unicodedata
import re

def validate_title(title):
  assert len(title) >= 3, "O título deve ter no mínimo 3 caracteres"
  assert len(title) <= 60, "O título deve ter no máximo 60 caracteres"
  return title

def validate_slug(slug):
  normalized_text = unicodedata.normalize('NFD', slug)
  text_without_diacritics = re.sub(r'[\u0300-\u036f]', '', normalized_text)
  lowercase_text = text_without_diacritics.lower()
  slug = re.sub(r'[^\w\s/-]', '', lowercase_text)
  slug = re.sub(r'[\s/]+', '-', slug)
  return slug

def validate_description(description):
  assert len(description) <= 255, "A descrição deve ter no máximo 255 caracteres"
  return  description

def validate_image(image):
  assert len(image) <= 255, "A imagem deve ter no máximo 255 caracteres"
  return image