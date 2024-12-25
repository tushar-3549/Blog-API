"""add users table

Revision ID: 17df40736fda
Revises: 26daafd9b22d
Create Date: 2024-12-25 19:49:22.135637

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision: str = '17df40736fda'
down_revision: Union[str, None] = '26daafd9b22d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    'users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False, unique=True),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
)
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
