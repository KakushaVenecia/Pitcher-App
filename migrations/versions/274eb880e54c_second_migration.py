"""Second Migration

Revision ID: 274eb880e54c
Revises: 8a63ee488903
Create Date: 2022-05-10 22:27:33.240031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '274eb880e54c'
down_revision = '8a63ee488903'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles')
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.drop_constraint('users_role_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_role_id_fkey', 'users', 'roles', ['role_id'], ['id'])
    op.drop_column('users', 'pass_secure')
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('emailaddress', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('password_input', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='roles_pkey')
    )
    # ### end Alembic commands ###
