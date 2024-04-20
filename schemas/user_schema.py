from config import ma

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id_usuario', 'nome', 'email', 'telefone', 'genero')

user_schema = UserSchema()
users_schema = UserSchema(many=True)