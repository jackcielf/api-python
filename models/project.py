from sqlalchemy.orm import validates, relationship
from sqlalchemy import ForeignKey, func
from validators import *
from config import db

class Project(db.Model):
  __tablename__ = 'tb_projects'
  id_project = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(60), nullable=False)
  slug = db.Column(db.String(60), nullable=False)
  description = db.Column(db.String(255))
  image = db.Column(db.String(255), nullable=True)
  status = db.Column(db.Enum('1', '2'), nullable=True)
  created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
  id_user = db.Column(db.String(100), db.ForeignKey('tb_users.id_user'), nullable=True)

  user = relationship("User", back_populates="projects")

  def __init__(self, title, description=None, image=None, id_user=None):
    self.title = title
    self.slug = title
    self.description = description
    self.image = image
    self.id_user = id_user

  @validates('title')
  def validate_title(self, key, title):
    return validate_title(title)
  
  @validates('slug')
  def validate_slug(self, key, slug):
    return validate_slug(slug)
  
  @validates('image')
  def validate_image(self, key, image):
    return validate_image(image)