"""add foreign key to posts table

Revision ID: 320672591ddc
Revises: a33a58d784c5
Create Date: 2023-01-07 13:02:39.425293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '320672591ddc'
down_revision = 'a33a58d784c5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
