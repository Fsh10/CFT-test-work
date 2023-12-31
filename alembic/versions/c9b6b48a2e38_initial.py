"""Initial

Revision ID: c9b6b48a2e38
Revises: 
Create Date: 2023-06-29 15:23:25.459392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9b6b48a2e38'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'salary',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('user', 'promotion_date',
               existing_type=sa.DATE(),
               nullable=False)
    op.drop_index('ix_user_id', table_name='user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_user_id', 'user', ['id'], unique=False)
    op.alter_column('user', 'promotion_date',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('user', 'salary',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
