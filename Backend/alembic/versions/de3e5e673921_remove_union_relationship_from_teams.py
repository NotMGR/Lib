"""remove union relationship from teams

Revision ID: de3e5e673921
Revises: 8ce8698cdb90
Create Date: 2026-08-17 15:59:59.357321

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de3e5e673921'
down_revision: Union[str, Sequence[str], None] = '8ce8698cdb90'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint(
        "teams_union_id_fkey",
        "teams",
        type_="foreignkey",
    )
    op.drop_column("teams", "union_id")

def downgrade() -> None:
    op.add_column(
        "teams",
        sa.Column("union_id", sa.Integer(), nullable=True),
    )
    op.create_foreign_key(
        "THE_ACTUAL_CONSTRAINT_NAME",
        "teams",
        "unions",
        ["union_id"],
        ["id"],
    )