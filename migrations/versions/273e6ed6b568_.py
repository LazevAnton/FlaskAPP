"""empty message

Revision ID: 273e6ed6b568
Revises: d12eb53db66d
Create Date: 2023-04-13 23:20:26.570192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '273e6ed6b568'
down_revision = 'd12eb53db66d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('facebook_url', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('linkedin_url', sa.String(), nullable=True))
        batch_op.drop_column('facebook')
        batch_op.drop_column('linkedin')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('linkedin', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('facebook', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_column('linkedin_url')
        batch_op.drop_column('facebook_url')

    # ### end Alembic commands ###