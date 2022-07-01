"""Initial migration

Revision ID: 3fde428e09a2
Revises: 
Create Date: 2022-06-30 18:08:23.033300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fde428e09a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hotels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('continent_name', sa.String(length=100), nullable=True),
    sa.Column('city_name', sa.String(length=100), nullable=True),
    sa.Column('country_name', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('reviews_count', sa.Integer(), nullable=True),
    sa.Column('info_1', sa.String(length=100), nullable=True),
    sa.Column('info_2', sa.String(length=100), nullable=True),
    sa.Column('info_3', sa.String(length=100), nullable=True),
    sa.Column('info_4', sa.String(length=100), nullable=True),
    sa.Column('info_5', sa.String(length=100), nullable=True),
    sa.Column('info_6', sa.String(length=100), nullable=True),
    sa.Column('info_7', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hotels')
    # ### end Alembic commands ###
