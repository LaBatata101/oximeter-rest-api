"""init db

Revision ID: f47bfc2ff0b7
Revises: 
Create Date: 2022-07-03 17:16:55.282886

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "f47bfc2ff0b7"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "sensor_data",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("user_id", sa.Integer, nullable=False, index=True),
        sa.Column("bpm", sa.Integer, nullable=False),
        sa.Column("spo2", sa.Integer, nullable=False),
        sa.Column("date", sa.DateTime, nullable=False, index=True),
    )


def downgrade() -> None:
    op.drop_table("sensor_data")
