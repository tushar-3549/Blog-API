"""add foreign key to posts table

Revision ID: 568428ac4c2c
Revises: 17df40736fda
Create Date: 2024-12-25 20:40:56.054721

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '568428ac4c2c'
down_revision: Union[str, None] = '17df40736fda'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('author_id', sa.Integer(), nullable=False)),
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=['author_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'author_id')
    pass
