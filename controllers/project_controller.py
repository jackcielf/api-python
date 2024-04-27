from flask import Blueprint, request

project_blueprint = Blueprint('project', __name__)

@project_blueprint.route('/project', methods=['POST'])
def add():
  try: 
    for item in request.json:
      title = item['title']
      description = item['description']
      image = item.get('image', None)

  except Exception as e:
    return e