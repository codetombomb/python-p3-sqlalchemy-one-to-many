"""Add Review Model

Revision ID: 5d682c6699e4
Revises: 846c33486c16
Create Date: 2022-12-29 23:08:11.259891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d682c6699e4'
down_revision = '846c33486c16'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('platform', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('games')
    # ### end Alembic commands ###
