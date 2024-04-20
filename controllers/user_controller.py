from flask import Blueprint, request, jsonify
from schemas import user_schema, users_schema
from sqlalchemy.exc import IntegrityError
from models import User
from config import db

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/user', methods=['POST'])
def add_user():
    try:
        for item in request.json:
            nome = item['nome']
            email = item['email']
            senha = item['senha']
            telefone = item['telefone']
            genero = item['genero']
            data_nas = item['data_nas']
        new_user = User(nome=nome, email=email, senha=senha, telefone=telefone, genero=genero, data_nas=data_nas)
        db.session.add(new_user)
        try: # Verifica email já existente
            db.session.commit()
            return user_schema.jsonify(new_user), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({ "message": "Email já cadastrado." }), 400
    except Exception as e:
        return jsonify({ "error": str(e) }), 500

@user_blueprint.route('/user', methods=['GET'])
def get_users():
    try:
        all_users = User.query.order_by(User.id_usuario.asc()).all()
        result = users_schema.dump(all_users)
        return jsonify(result)
    except Exception as e:
        return jsonify({ "error": str(e) }), 500

@user_blueprint.route('/user/<id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.get(id)
        if user is None:
            return jsonify({ "message": "Usuário não encontrado." }), 404
        return user_schema.jsonify(user)
    except Exception as e:
        return jsonify({ "error": str(e) }), 500

@user_blueprint.route('/user/<id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.get(id)
        if user is None:
            return jsonify({ "message": "Usuário não encontrado." }), 404
        for item in request.json:
            nome = item['nome']
            email = item['email']
            senha = item['senha']
            telefone = item['telefone']
            genero = item['genero']
            data_nas = item['data_nas']
        user.nome = nome
        user.email = email
        user.senha = senha
        user.telefone = telefone
        user.genero = genero
        user.data_nas = data_nas
        db.session.commit()
        return user_schema.jsonify({ "message": "Dados atualizados com sucesso." })
    except Exception as e:
        return jsonify({ "error": str(e) }), 500

@user_blueprint.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.get(id)
        if user is None:
            return jsonify({ "message": "Usuário não encontrado." }), 404
        db.session.delete(user)
        db.session.commit()
        return jsonify({ "message": "Usuário deletado com sucesso." })
    except Exception as e:
        return jsonify({ "error": str(e) }), 500
