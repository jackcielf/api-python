from config import db

project_user = db.Table('project_user',
  db.Column('id_user', db.String(100), db.ForeignKey('tb_users.id_user')),
  db.Column('id_project', db.Integer, db.ForeignKey('tb_projects.id_project'))
)