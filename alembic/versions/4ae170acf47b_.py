"""empty message

Revision ID: 4ae170acf47b
Revises: eeb740cec8d5, f54c8fb97076
Create Date: 2023-10-28 16:42:52.545877

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ae170acf47b'
down_revision: Union[str, None] = ('eeb740cec8d5', 'f54c8fb97076')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
