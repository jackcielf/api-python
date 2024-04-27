from config import ma

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id_user', 'name', 'email', 'password', 'fone', 'gender', 'date_birth', 'created_at', 'is_admin')

user_schema = UserSchema()
users_schema = UserSchema(many=True)