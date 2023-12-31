"""crear habitos y tags

Revision ID: f54c8fb97076
Revises: 15dc10e1c935
Create Date: 2023-09-16 12:12:29.085768

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f54c8fb97076'
down_revision: Union[str, None] = '15dc10e1c935'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('habitos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('descripcion', sa.String(), nullable=True),
    sa.Column('aprendizaje', sa.String(), nullable=True),
    sa.Column('dificultad', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_habitos_id'), 'habitos', ['id'], unique=False)
    op.create_index(op.f('ix_habitos_name'), 'habitos', ['name'], unique=True)
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tags_id'), 'tags', ['id'], unique=False)
    op.create_table('habitos_tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('habitos_id', sa.Integer(), nullable=True),
    sa.Column('tags_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['habitos_id'], ['habitos.id'], ),
    sa.ForeignKeyConstraint(['tags_id'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_habitos_tags_id'), 'habitos_tags', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_habitos_tags_id'), table_name='habitos_tags')
    op.drop_table('habitos_tags')
    op.drop_index(op.f('ix_tags_id'), table_name='tags')
    op.drop_table('tags')
    op.drop_index(op.f('ix_habitos_name'), table_name='habitos')
    op.drop_index(op.f('ix_habitos_id'), table_name='habitos')
    op.drop_table('habitos')
    # ### end Alembic commands ###
