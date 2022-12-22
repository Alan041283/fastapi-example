"""add_last_few_columns_to_posts_table

Revision ID: 08d5606c69c7
Revises: 75c8b0381cbf
Create Date: 2022-12-20 12:13:53.224304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08d5606c69c7'
down_revision = '75c8b0381cbf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
