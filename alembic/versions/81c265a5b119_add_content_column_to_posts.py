"""add_content_column_to posts

Revision ID: 81c265a5b119
Revises: 85c7355184cf
Create Date: 2022-12-20 11:59:53.678139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81c265a5b119'
down_revision = '85c7355184cf'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
