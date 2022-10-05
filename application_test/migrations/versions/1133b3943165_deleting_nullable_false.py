"""deleting nullable false

Revision ID: 1133b3943165
Revises: 826c202e810a
Create Date: 2022-10-04 18:43:19.522769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1133b3943165'
down_revision = '826c202e810a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('modules', sa.Column('name_1', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('modules', 'name_1')
    # ### end Alembic commands ###
