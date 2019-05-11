"""update protocols table: is_cool col

Revision ID: 1a9952031305
Revises: 8a4192a2406a
Create Date: 2019-05-11 16:51:29.945073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a9952031305'
down_revision = '8a4192a2406a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('protocols', sa.Column('is_cool', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('protocols', 'is_cool')
    # ### end Alembic commands ###
