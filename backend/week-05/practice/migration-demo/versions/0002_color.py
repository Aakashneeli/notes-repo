"""Completed teaching revision: backfill using a database default."""
from alembic import op
import sqlalchemy as sa
revision = "demo2"
down_revision = "demo1"
branch_labels = depends_on = None

def upgrade():
    op.add_column("labels", sa.Column("color", sa.String(20),
                  nullable=False, server_default="gray"))

def downgrade():
    op.drop_column("labels", "color")
