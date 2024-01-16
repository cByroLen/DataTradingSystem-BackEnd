"""empty message

Revision ID: 5b7d846f45ab
Revises: c18c79444f9c
Create Date: 2023-04-30 15:22:41.397604

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5b7d846f45ab'
down_revision = 'c18c79444f9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('qc', schema=None) as batch_op:
        batch_op.alter_column('l_area',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=200),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('qc', schema=None) as batch_op:
        batch_op.alter_column('l_area',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=200),
               nullable=False)

    # ### end Alembic commands ###