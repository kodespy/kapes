"""empty message

Revision ID: 5ac30a972585
Revises: 26d45d154cc7
Create Date: 2017-08-18 11:08:44.712748

"""

# revision identifiers, used by Alembic.
revision = '5ac30a972585'
down_revision = '26d45d154cc7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aportes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idsocio', sa.Integer(), nullable=True),
    sa.Column('monto', sa.Integer(), nullable=True),
    sa.Column('mes', sa.String(), nullable=True),
    sa.Column('fecha', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['idsocio'], ['socios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('aportes')
    # ### end Alembic commands ###
