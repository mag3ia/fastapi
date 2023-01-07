"""create posts table

Revision ID: 739311eeb328
Revises: 
Create Date: 2023-01-07 12:15:01.253215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '739311eeb328'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable = False, primary_key = True),
                    sa.Column('title', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
