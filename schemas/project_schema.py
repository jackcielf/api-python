from config import ma

class ProjectSchema(ma.Schema):
  class Meta:
    fields = ('id_project', 'title', 'slug', 'description', 'image', 'status', 'created_at', 'id_user')

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)