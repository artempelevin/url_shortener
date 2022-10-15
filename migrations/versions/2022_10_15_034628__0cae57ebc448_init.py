"""init

Revision ID: 0cae57ebc448
Revises: 
Create Date: 2022-10-15 03:46:28.826286

"""
from alembic import op
import sqlalchemy as sa

revision = '0cae57ebc448'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('urls',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('target_url', sa.Text(), nullable=True),
                    sa.Column('key', sa.String(length=10), nullable=True),
                    sa.Column('secret_key', sa.String(length=15), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('urls')
