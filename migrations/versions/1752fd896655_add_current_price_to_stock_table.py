"""Add current price to stock table

Revision ID: 1752fd896655
Revises: f3a0699f3167
Create Date: 2020-11-06 09:36:05.546319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1752fd896655'
down_revision = 'f3a0699f3167'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stocks', sa.Column('current_price', sa.Integer(), nullable=True))
    op.add_column('stocks', sa.Column('current_price_date', sa.DateTime(), nullable=True))
    op.add_column('stocks', sa.Column('position_value', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'stocks', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'stocks', type_='foreignkey')
    op.drop_column('stocks', 'position_value')
    op.drop_column('stocks', 'current_price_date')
    op.drop_column('stocks', 'current_price')
    # ### end Alembic commands ###