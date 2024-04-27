from sqlalchemy.orm import validates
from sqlalchemy import ForeignKey, func
from models import project_user
from validators import *
from config import db

class Project(db.Model):
  __tablename__ = 'tb_projects'
  id_project = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(50), nullable=False)
  slug = db.Column(db.String(50), nullable=False)
  description = db.Column(db.String(255), nullable=True)
  image = db.Column(db.String(255), nullable=True)
  status = db.Column(db.Enum('1', '2'), nullable=True)
  created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
  id_user = db.Column(db.String(100), ForeignKey('tb_users.id_user'))

  users = db.relationship('User', secondary=project_user, back_populates='projects')

  def __init__(self, title, slug, description, image, status, id_user):
    self.title = title
    self.slug = slug
    self.description = description
    self.image = image
    self.status = status
    self.id_user = id_user

  @validates('name')
  def validate_name(self, key, name):
    return validate_name(name)