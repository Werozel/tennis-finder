"""empty message

Revision ID: 700540bee8bd
Revises: 
Create Date: 2022-05-20 22:32:02.977202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '700540bee8bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('full_name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('login', sa.VARCHAR(length=50), nullable=False),
    sa.Column('password', sa.VARCHAR(length=512), nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), nullable=True),
    sa.Column('phone', sa.VARCHAR(length=12), nullable=True),
    sa.Column('skill', sa.FLOAT(), nullable=False),
    sa.Column('wins', sa.INTEGER(), nullable=True),
    sa.Column('losses', sa.INTEGER(), nullable=True),
    sa.Column('cancels', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    op.create_table('games',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=512), nullable=False),
    sa.Column('winner_id', sa.INTEGER(), nullable=True),
    sa.Column('game_date', sa.TIMESTAMP(), nullable=True),
    sa.Column('status', sa.Enum('PENDING', 'IN_PROGRESS', 'COMPLETED', 'CANCELED', name='gamestatus'), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['winner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game_participants',
    sa.Column('game_id', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game_participants')
    op.drop_table('games')
    op.drop_table('users')
    # ### end Alembic commands ###
