"""empty message

Revision ID: 4947469110ca
Revises: 273e6ed6b568
Create Date: 2023-04-13 23:20:54.831667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4947469110ca'
down_revision = '273e6ed6b568'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('linkedIn_url', sa.String(), nullable=True))
        batch_op.drop_column('linkedin_url')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('linkedin_url', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_column('linkedIn_url')

    # ### end Alembic commands ###
