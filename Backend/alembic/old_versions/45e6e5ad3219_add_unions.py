"""add unions

Revision ID: 45e6e5ad3219
Revises: 
Create Date: 2026-08-14 21:14:19.487212

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45e6e5ad3219'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("union_id", sa.Integer(), nullable=True)
    )

    op.add_column(
        "teams",
        sa.Column("union_id", sa.Integer(), nullable=True)
    )

    op.add_column(
        "raid",
        sa.Column("union_id", sa.Integer(), nullable=True)
    )

    op.create_foreign_key(
        "fk_users_union_id",
        "users",
        "unions",
        ["union_id"],
        ["id"],
    )

    op.create_foreign_key(
        "fk_teams_union_id",
        "teams",
        "unions",
        ["union_id"],
        ["id"],
    )

    op.create_foreign_key(
        "fk_raid_union_id",
        "raid",
        "unions",
        ["union_id"],
        ["id"],
    )
def downgrade() -> None:
    """Downgrade schema."""

    op.drop_constraint(
        "fk_users_union_id",
        "users",
        type_="foreignkey",
    )

    op.drop_constraint(
        "fk_teams_union_id",
        "teams",
        type_="foreignkey",
    )

    op.drop_constraint(
        "fk_raid_union_id",
        "raid",
        type_="foreignkey",
    )

    op.drop_column("users", "union_id")
    op.drop_column("teams", "union_id")
    op.drop_column("raid", "union_id")

    op.drop_table("unions")
