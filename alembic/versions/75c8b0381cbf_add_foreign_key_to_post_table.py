"""add_foreign_key_to_post_table

Revision ID: 75c8b0381cbf
Revises: 3e53844ad947
Create Date: 2022-12-20 12:06:28.117677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75c8b0381cbf'
down_revision = '3e53844ad947'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk',source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
