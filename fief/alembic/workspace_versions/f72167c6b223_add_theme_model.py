"""Add Theme model

Revision ID: f72167c6b223
Revises: ab9cf21c76dd
Create Date: 2023-01-04 10:42:08.479094

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.orm import Session

import fief
from fief.models import Theme

# revision identifiers, used by Alembic.
revision = "f72167c6b223"
down_revision = "ab9cf21c76dd"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "fief_themes",
        sa.Column("id", fief.models.generics.GUID(), nullable=False),
        sa.Column(
            "created_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("default", sa.Boolean(), nullable=False),
        sa.Column("primary_color", sa.String(length=255), nullable=False),
        sa.Column("primary_color_hover", sa.String(length=255), nullable=False),
        sa.Column("primary_color_light", sa.String(length=255), nullable=False),
        sa.Column("input_color", sa.String(length=255), nullable=False),
        sa.Column("input_color_background", sa.String(length=255), nullable=False),
        sa.Column("light_color", sa.String(length=255), nullable=False),
        sa.Column("light_color_hover", sa.String(length=255), nullable=False),
        sa.Column("text_color", sa.String(length=255), nullable=False),
        sa.Column("accent_color", sa.String(length=255), nullable=False),
        sa.Column("background_color", sa.String(length=255), nullable=False),
        sa.Column("font_size", sa.Integer(), nullable=False),
        sa.Column("font_family", sa.String(length=255), nullable=False),
        sa.Column("font_css_url", sa.String(length=512), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_fief_themes_created_at"), "fief_themes", ["created_at"], unique=False
    )
    op.create_index(
        op.f("ix_fief_themes_updated_at"), "fief_themes", ["updated_at"], unique=False
    )
    op.add_column(
        "fief_tenants",
        sa.Column("theme_id", fief.models.generics.GUID(), nullable=True),
    )
    op.create_foreign_key(
        None, "fief_tenants", "fief_themes", ["theme_id"], ["id"], ondelete="SET NULL"
    )

    # Insert default theme
    session = Session(bind=op.get_bind())
    default_theme = Theme.build_default()
    session.add(default_theme)
    session.commit()

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "fief_tenants", type_="foreignkey")
    op.drop_column("fief_tenants", "theme_id")
    op.drop_index(op.f("ix_fief_themes_updated_at"), table_name="fief_themes")
    op.drop_index(op.f("ix_fief_themes_created_at"), table_name="fief_themes")
    op.drop_table("fief_themes")
    # ### end Alembic commands ###
