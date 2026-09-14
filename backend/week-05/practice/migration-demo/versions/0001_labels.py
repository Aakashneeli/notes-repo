"""Completed teaching revision: a tiny label table."""
from alembic import op
import sqlalchemy as sa
revision = "demo1"
down_revision = None
branch_labels = depends_on = None

def upgrade():
    op.create_table("labels",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(40), nullable=False))

def downgrade():
    op.drop_table("labels")
