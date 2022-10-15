"""init

Revision ID: c9e55baeb86a
Revises: 
Create Date: 2022-10-15 19:25:39.535740

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'c9e55baeb86a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('urls',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('target_url', sa.Text(), nullable=False),
                    sa.Column('key', sa.String(length=10), nullable=False),
                    sa.Column('secret_key', sa.String(length=15), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('key'),
                    sa.UniqueConstraint('secret_key')
                    )
    op.create_table('visits',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('url_id', sa.Integer(), nullable=True),
                    sa.Column('ip', sa.String(length=15), nullable=False),
                    sa.Column('user_agent', sa.Text(), nullable=True),
                    sa.Column('visit_time', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(['url_id'], ['urls.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('visits')
    op.drop_table('urls')
