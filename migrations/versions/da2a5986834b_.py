"""empty message

Revision ID: da2a5986834b
Revises: 
Create Date: 2020-12-10 14:58:06.227798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da2a5986834b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('keyword',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_keyword_name'), 'keyword', ['name'], unique=False)
    op.create_table('produce',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Integer(), nullable=False),
    sa.Column('imageRef', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id', 'name')
    )
    op.create_table('supplier',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('address', sa.String(length=64), nullable=True),
    sa.Column('zipcode', sa.Integer(), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('state', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_supplier_address'), 'supplier', ['address'], unique=False)
    op.create_index(op.f('ix_supplier_city'), 'supplier', ['city'], unique=False)
    op.create_index(op.f('ix_supplier_name'), 'supplier', ['name'], unique=False)
    op.create_index(op.f('ix_supplier_state'), 'supplier', ['state'], unique=False)
    op.create_index(op.f('ix_supplier_zipcode'), 'supplier', ['zipcode'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('listing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('supplier_id', sa.Integer(), nullable=True),
    sa.Column('produce_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['produce_id'], ['produce.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('produce_to_keyword',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('produce_id', sa.Integer(), nullable=True),
    sa.Column('keyword_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['keyword_id'], ['keyword.id'], ),
    sa.ForeignKeyConstraint(['produce_id'], ['produce.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('content',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('listing_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['listing_id'], ['listing.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('content')
    op.drop_table('produce_to_keyword')
    op.drop_table('listing')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_supplier_zipcode'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_state'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_name'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_city'), table_name='supplier')
    op.drop_index(op.f('ix_supplier_address'), table_name='supplier')
    op.drop_table('supplier')
    op.drop_table('produce')
    op.drop_index(op.f('ix_keyword_name'), table_name='keyword')
    op.drop_table('keyword')
    # ### end Alembic commands ###
