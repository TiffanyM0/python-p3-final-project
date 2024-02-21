"""update

Revision ID: 456326224eec
Revises: fab7324f17e5
Create Date: 2024-02-21 19:43:19.181681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '456326224eec'
down_revision = 'fab7324f17e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('unique_email', 'users', ['user_email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('unique_email', 'users', type_='unique')
    # ### end Alembic commands ###
