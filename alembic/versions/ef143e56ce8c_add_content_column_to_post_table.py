"""add content column to post table

Revision ID: ef143e56ce8c
Revises: 739311eeb328
Create Date: 2023-01-07 12:26:22.341580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef143e56ce8c'
down_revision = '739311eeb328'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
                    sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
