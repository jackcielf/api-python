from flask import Flask
from config import db, ma
from flask_migrate import Migrate
from controllers import user_blueprint, project_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:jakki@localhost/db_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'

db.init_app(app)
ma.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(user_blueprint)
app.register_blueprint(project_blueprint)

if __name__ == '__main__':
  app.run(port=5000, host='localhost', debug=True)