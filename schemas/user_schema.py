from config import ma

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id_usuario', 'name', 'email', 'password', 'fone', 'gender', 'date_birth', 'created_at')

user_schema = UserSchema() # Usado para retorna um único dado do db
users_schema = UserSchema(many=True) # Usado para retorna todos os dados do db