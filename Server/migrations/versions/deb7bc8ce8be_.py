"""empty message

Revision ID: deb7bc8ce8be
Revises: 
Create Date: 2021-07-14 19:43:57.732540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'deb7bc8ce8be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tGeo',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Latitude', sa.Float(), nullable=True),
    sa.Column('Longitude', sa.Float(), nullable=True),
    sa.Column('TypeId', sa.Integer(), nullable=True),
    sa.Column('Distance', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tGeo')
    # ### end Alembic commands ###
