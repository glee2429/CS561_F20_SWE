"""Add datetime to stocks table

Revision ID: f3a0699f3167
Revises: 1c496262422a
Create Date: 2020-11-04 11:15:33.724544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3a0699f3167'
down_revision = '1c496262422a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stocks', sa.Column('purchase_date', sa.DateTime(), nullable=True))
    op.create_foreign_key(None, 'stocks', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'stocks', type_='foreignkey')
    op.drop_column('stocks', 'purchase_date')
    # ### end Alembic commands ###
