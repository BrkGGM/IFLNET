"""update

Revision ID: 28f5f63d72b5
Revises: 0397be6a31b8
Create Date: 2024-03-05 23:25:47.909639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28f5f63d72b5'
down_revision = '0397be6a31b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('yazilar', schema=None) as batch_op:
        batch_op.add_column(sa.Column('kategori', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('yazilar', schema=None) as batch_op:
        batch_op.drop_column('kategori')

    # ### end Alembic commands ###
