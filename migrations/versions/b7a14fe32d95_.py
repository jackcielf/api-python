"""empty message

Revision ID: b7a14fe32d95
Revises: 41d4cf378886
Create Date: 2024-04-27 15:09:17.443645

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b7a14fe32d95'
down_revision = '41d4cf378886'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_users',
    sa.Column('id_user', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('fone', sa.String(length=11), nullable=True),
    sa.Column('gender', sa.Enum('1', '2'), nullable=True),
    sa.Column('date_birth', sa.Date(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id_user'),
    sa.UniqueConstraint('email')
    )
    op.create_table('tb_projects',
    sa.Column('id_project', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('slug', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('status', sa.Enum('1', '2'), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('id_user', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['tb_users.id_user'], ),
    sa.PrimaryKeyConstraint('id_project')
    )
    op.create_table('project_user',
    sa.Column('id_user', sa.String(length=100), nullable=True),
    sa.Column('id_project', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_project'], ['tb_projects.id_project'], ),
    sa.ForeignKeyConstraint(['id_user'], ['tb_users.id_user'], )
    )
    with op.batch_alter_table('tb_user', schema=None) as batch_op:
        batch_op.drop_index('email')

    op.drop_table('tb_user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_user',
    sa.Column('id_user', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('fone', mysql.VARCHAR(length=11), nullable=True),
    sa.Column('gender', mysql.ENUM('1', '2'), nullable=True),
    sa.Column('date_birth', sa.DATE(), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('is_admin', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id_user'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('tb_user', schema=None) as batch_op:
        batch_op.create_index('email', ['email'], unique=True)

    op.drop_table('project_user')
    op.drop_table('tb_projects')
    op.drop_table('tb_users')
    # ### end Alembic commands ###
