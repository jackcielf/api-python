from config import ma

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id_usuario', 'nome', 'email', 'senha', 'telefone', 'genero', 'data_nas', 'created_at')

user_schema = UserSchema()
users_schema = UserSchema(many=True)