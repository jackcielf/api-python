from flask import Blueprint, jsonify, request
from authenticate import jwt_required
from models import Project
from schemas import *
from config import db

project_blueprint = Blueprint('project', __name__)

@project_blueprint.route('/project', methods=['POST'])
def add():
  try: 
    for item in request.json:
      title = item['title']
      description = item.get('description', None)
      image = item.get('image', None)
    new_project = Project(title, description, image)
    db.session.add(new_project)
    db.session.commit()
    return project_schema.jsonify(new_project), 201
  except Exception as error:
    return jsonify({
      "message": "Erro ao criar novo projeto",
      "error": str(error)
    }), 500

@project_blueprint.route('/project', methods=['GET'])
def get_all():
  try:
    all_projects = Project.query.all()
    result = projects_schema.dump(all_projects)
    return jsonify(result), 200
  except Exception as error:
    return jsonify({
      "message": "Erro ao listar projetos",
      "error": str(error)
    }), 500
  
@project_blueprint.route('/project/<id>', methods=['GET'])
def get_one(id):
  project = Project.query.get(id)
  if not project:
    return jsonify({ "error": "Projeto não encontrado" }), 404
  try:
    return project_schema.jsonify(project), 200
  except Exception as error:
    return jsonify({
      "message": "Erro ao lista projeto",
      "error": str(error)
    }), 500
  
@project_blueprint.route('/project/<id>', methods=['PUT'])
def update(id):
  project = Project.query.get(id)
  if not project:
    return jsonify({ "error": "Projeto não encontrado" }), 404
  try:
    for item in request.json:
      title = item['title']
      description = item.get('description', None)
      image = item.get('image', None)
    project.title = title
    project.description = description
    project.image = image
    db.session.commit()
    return jsonify({
      "message": "Dados do projeto atualizados com sucesso"
    }), 200
  except Exception as error:
    return jsonify({
      "message": "Erro ao atualizar dados do projeto",
      "error": str(error)
    }), 500
  
@project_blueprint.route('/project/<id>', methods=['DELETE'])
def delete(id):
  project = Project.query.get(id)
  if not project:
    return jsonify({ "error": "Projeto não encontrado" }), 404
  try:
    db.session.delete(project)
    db.session.commit()
    return jsonify({ "message": "Projeto deletado com sucesso" }), 200
  except Exception as error:
    return jsonify({
      "message": "Erro ao deletar dados do projeto",
      "error": str(error)
    }), 500
  
@project_blueprint.route('/project/<id>', methods=['PATCH'])
@jwt_required
def init_project(id, current_user):
  try:
    project = Project.query.get(id)
    print(project)
    if not current_user and not project:
      return jsonify({ "error": "Usuário ou projeto não encontrado" }), 404
    project.id_user = current_user.id_user
    project.status = "1"
    db.session.commit()
    return jsonify({
      "message": "Novo projeto iniciado"
    }), 200
  except Exception as error:
    return jsonify({
      "message": "Erro ao mudar dados do projeto",
      "error": str(error)
    }), 500