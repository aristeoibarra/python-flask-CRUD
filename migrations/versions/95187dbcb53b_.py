"""empty message

Revision ID: 95187dbcb53b
Revises: 3101493d2583
Create Date: 2023-10-20 18:04:38.193282

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '95187dbcb53b'
down_revision = '3101493d2583'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventory',
    sa.Column('inventory_id', sa.Integer(), nullable=False),
    sa.Column('inventory_name', sa.String(length=64), nullable=True),
    sa.Column('inventory_description', sa.String(length=64), nullable=True),
    sa.Column('inventory_stock', sa.Integer(), nullable=True),
    sa.Column('inventory_price', sa.Float(), nullable=True),
    sa.Column('inventory_image', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('inventory_id')
    )
    op.drop_column('users', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_table('inventory')
    # ### end Alembic commands ###
