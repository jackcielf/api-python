from flask import Blueprint, request, jsonify
from models import User
from schemas import user_schema, users_schema
from config import db

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/user', methods=['POST'])
def add_user():
    for item in request.json:
        nome = item['nome']
        email = item['email']
        telefone = item['telefone']
        genero = item['genero']
    new_user = User(nome=nome, email=email, telefone=telefone, genero=genero)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

@user_blueprint.route('/user', methods=['GET'])
def get_users():
    all_users = User.query.order_by(User.id_usuario.asc()).all()
    result = users_schema.dump(all_users)
    return jsonify(result)

@user_blueprint.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

@user_blueprint.route('/user/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)

    for item in request.json:
        nome = item['nome']
        email = item['email']
        telefone = item['telefone']
        genero = item['genero']
    user.nome = nome
    user.email = email
    user.telefone = telefone
    user.genero = genero
    db.session.commit()
    return user_schema.jsonify(user)

@user_blueprint.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)
