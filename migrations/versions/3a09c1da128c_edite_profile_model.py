"""Edite profile model

Revision ID: 3a09c1da128c
Revises: 9340a1a912e6
Create Date: 2023-04-04 15:05:30.617157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a09c1da128c'
down_revision = '9340a1a912e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('linkedIn_url', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('facebook_url', sa.String(), nullable=True))
        batch_op.drop_column('bio')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bio', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_column('facebook_url')
        batch_op.drop_column('linkedIn_url')

    # ### end Alembic commands ###
