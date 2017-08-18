"""empty message

Revision ID: a0ef55bfc5a9
Revises: None
Create Date: 2017-08-18 08:12:53.661047

"""

# revision identifiers, used by Alembic.
revision = 'a0ef55bfc5a9'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('socios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('documento', sa.Integer(), nullable=True),
    sa.Column('nombres', sa.String(), nullable=True),
    sa.Column('celular', sa.String(), nullable=True),
    sa.Column('club', sa.String(), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.Column('fecha', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('documento')
    )
    op.create_table('aportes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idsocio', sa.Integer(), nullable=True),
    sa.Column('monto', sa.Integer(), nullable=True),
    sa.Column('mes', sa.Integer(), nullable=True),
    sa.Column('fecha', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['idsocio'], ['socios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('aportes')
    op.drop_table('socios')
    # ### end Alembic commands ###
