"""empty message

Revision ID: 2cd8dfd5ba20
Revises: a5f7287907db
Create Date: 2024-01-29 16:10:39.453761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cd8dfd5ba20'
down_revision = 'a5f7287907db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('group_trening', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('update_at', sa.DateTime(), nullable=True, server_onuodate=sa.text('CURRENT_TIMESTAMP')))

    with op.batch_alter_table('personal_trening', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('update_at', sa.DateTime(), nullable=True, server_onuodate=sa.text('CURRENT_TIMESTAMP')))

    with op.batch_alter_table('trener', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('update_at', sa.DateTime(), nullable=True, server_onuodate=sa.text('CURRENT_TIMESTAMP')))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trener', schema=None) as batch_op:
        batch_op.drop_column('update_at')
        batch_op.drop_column('created_at')

    with op.batch_alter_table('personal_trening', schema=None) as batch_op:
        batch_op.drop_column('update_at')
        batch_op.drop_column('created_at')

    with op.batch_alter_table('group_trening', schema=None) as batch_op:
        batch_op.drop_column('update_at')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###