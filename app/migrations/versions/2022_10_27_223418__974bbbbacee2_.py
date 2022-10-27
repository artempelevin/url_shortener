"""empty message

Revision ID: 974bbbbacee2
Revises: c9e55baeb86a
Create Date: 2022-10-27 22:34:18.185810

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '974bbbbacee2'
down_revision = 'c9e55baeb86a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('visits', sa.Column('country', sa.Text(), nullable=True))


def downgrade() -> None:
    op.drop_column('visits', 'country')
