"""create posts table

Revision ID: 26daafd9b22d
Revises: 
Create Date: 2024-12-25 12:50:18.918806

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision: str = '26daafd9b22d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    'posts',
    sa.Column('id', sa.Integer(), primary_key=True, nullable=False, autoincrement=True),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('published', sa.Boolean(), server_default='TRUE', nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')),
)
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
