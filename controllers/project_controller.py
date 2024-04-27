from flask import Blueprint, jsonify, request
from schemas import project_schema
from models import Project
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
    result = project_schema.dump(all_projects)
    return jsonify(result), 201
  except Exception as error:
    return jsonify({
      "message": "Erro ao listar projetos",
      "error": str(error)
    }), 500
  
@project_blueprint.route('/project/<id>', methods=['GET'])
def get_one(id):
  try:
    project = Project.query.get(id)
    if not project:
      return jsonify({ "error": "Projeto não encontrado" }), 404
    return project_schema.jsonify(project), 201
  except Exception as error:
    return jsonify({
      "message": "Erro ao lista projeto",
      "error": str(error)
    }), 500
  
@project_blueprint.route('/project/<id>', methods=['PUT'])
def update(id):
  try:
    project = Project.query.get(id)
    if not project:
      return jsonify({ "error": "Projeto não encontrado" }), 404
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
    }), 201
  except Exception as error:
    return jsonify({
      "message": "Erro ao atualizar dados do projeto",
      "error": str(error)
    }), 500
  
@project_blueprint.route('/project/<id>', methods=['DELETE'])
def delete(id):
  try:
    project = Project.query.get(id)
    if not project:
      return jsonify({ "error": "Projeto não encontrado" }), 404
    db.session.delete(project)
    db.session.commit()
    return jsonify({ "message": "Projeto deletado com sucesso" }), 201
  except Exception as error:
    return jsonify({
      "message": "Erro ao deletar dados do projeto",
      "error": str(error)
    }), 500