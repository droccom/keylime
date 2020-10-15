"""allowlist rename

Revision ID: eeb702f77d7d
Revises: 8a44a4364f5a
Create Date: 2020-10-15 13:29:38.853574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eeb702f77d7d'
down_revision = '8a44a4364f5a'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_registrar():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_registrar():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def upgrade_cloud_verifier():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('verifiermain', 'ima_whitelist', new_column_name='allowlist', existing_type=sa.Text(length=429400000), existing_nullable=True)
    # ### end Alembic commands ###


def downgrade_cloud_verifier():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('verifiermain', 'allowlist', new_column_name='ima_whitelist', existing_type=sa.Text(length=429400000), existing_nullable=True)
    # ### end Alembic commands ###

