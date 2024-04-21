from flask import Blueprint, current_app, request, jsonify
from schemas import user_schema, users_schema
from sqlalchemy.exc import IntegrityError
from authenticate import jwt_required
from models import User
from config import db
import datetime
import jwt

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/user', methods=['POST'])
def add():
    try:
        for item in request.json:
            nome = item['nome']
            email = item['email']
            senha = item['senha']
            telefone = item['telefone']
            genero = item['genero']
            data_nas = item['data_nas']
        new_user = User(nome, email, senha, telefone, genero, data_nas)
        db.session.add(new_user)
        try: # Verifica email já existente
            db.session.commit()
            return user_schema.jsonify(new_user), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({ "error": "Email já cadastrado." }), 400
    except Exception as e:
        return jsonify({ "error": str(e) }), 500

@user_blueprint.route('/user', methods=['GET'])
@jwt_required
def get_all(current_user):
    try:
        all_users = User.query.all()
        result = users_schema.dump(all_users)
        return jsonify(result)
    except Exception as e:
        return jsonify({ "error": str(e) }), 500

@user_blueprint.route('/user/<id>', methods=['GET'])
def get_one(id):
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({ "error": "Usuário não encontrado." }), 404
        return user_schema.jsonify(user)
    except Exception as e:
        return jsonify({ "error": str(e) }), 500

@user_blueprint.route('/user/<id>', methods=['PUT'])
def update(id):
    try:
        user = User.query.get(id)
        if user is None:
            return jsonify({ "error": "Usuário não encontrado." }), 404
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
def delete(id):
    try:
        user = User.query.get(id)
        if user is None:
            return jsonify({ "error": "Usuário não encontrado." }), 404
        db.session.delete(user)
        db.session.commit()
        return jsonify({ "message": "Usuário deletado com sucesso." })
    except Exception as e:
        return jsonify({ "error": str(e) }), 500

@user_blueprint.route('/user/login', methods=['POST'])
def login():
    for item in request.json:
        email = item['email']
        senha = item['senha']

    if not email or not senha:
        return jsonify({ "error": "E-mail e senha são obrigatórios." }), 400
    
    user = User.query.filter_by(email=email).first()

    if not user or not user.verify_password(senha):
        return jsonify({ "error": "E-mail e/ou senha incorretos." }), 403 # 403 representa falha de autenticação
    
    expiration_token_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=10)
    payload = {
        "id": user.id_usuario,
        "exp": expiration_token_time
    }

    token = jwt.encode(payload, current_app.config['SECRET_KEY'])

    return jsonify({ "token": token })