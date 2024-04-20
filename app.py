from flask import Flask
from config import db, ma
from controllers import user_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:jakki@localhost/db_test'
db.init_app(app)
ma.init_app(app)

app.register_blueprint(user_blueprint)

if __name__ == '__main__':
  app.run(port=5000, host='localhost', debug=True)