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
      name = item['name']
      email = item['email']
      password = item['password']
      fone = item.get('fone', None)
      gender = item.get('gender', None)
      date_birth = item.get('date_birth', None)
    new_user = User(name, email, password, fone, gender, date_birth)
    db.session.add(new_user)
    try:
      db.session.commit()
      return user_schema.jsonify(new_user), 201
    except IntegrityError:
      db.session.rollback()
      return jsonify({ "error": "Email já cadastrado" }), 400
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
      return jsonify({ "error": "Usuário não encontrado" }), 404
    return user_schema.jsonify(user)
  except Exception as e:
    return jsonify({ "error": str(e) }), 500

@user_blueprint.route('/user/<id>', methods=['PUT'])
def update(id):
  try:
    user = User.query.get(id)
    if not user:
      return jsonify({ "error": "Usuário não encontrado" }), 404
    for item in request.json:
      name = item['name']
      fone = item['fone']
      gender = item['gender']
      date_birth = item['date_birth']
    user.name = name
    user.fone = fone
    user.gender = gender
    user.date_birth = date_birth
    db.session.commit()
    return jsonify({ "message": "Dados de usuário atualizados com sucesso" })
  except Exception as e:
    return jsonify({
        "message": "Não foi possível atualizar dados de usuário",
        "error": str(e)
    }), 500

@user_blueprint.route('/user/<id>', methods=['DELETE'])
@jwt_required
def delete(id, current_user):
  try:
    user = User.query.get(id)
    if not user:
      return jsonify({ "error": "Usuário não encontrado" }), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({ "message": "Usuário deletado com sucesso" })
  except Exception as e:
    return jsonify({ "error": str(e) }), 500

@user_blueprint.route('/user/login', methods=['POST'])
def login():
  for item in request.json:
    email = item['email']
    password = item['password']

  if not email or not password:
    return jsonify({ "error": "E-mail e senha são obrigatórios" }), 400
    
  user = User.query.filter_by(email=email).first()

  if not user or not user.verify_password(password):
    return jsonify({ "error": "E-mail e/ou senha incorretos" }), 403 # 403 representa falha de autenticação
    
  expiration_token_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=10)
  payload = {
    "id": user.id_user,
    "exp": expiration_token_time
  }

  token = jwt.encode(payload, current_app.config['SECRET_KEY'])

  return jsonify({ "token": token })