"""empty message

Revision ID: 150566d7f57d
Revises: 43ca8f0e4e15
Create Date: 2019-04-08 15:54:38.693455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '150566d7f57d'
down_revision = '43ca8f0e4e15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('eth_contact',
    sa.Column('address', sa.String(length=42), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('eth_balance', sa.Float(), nullable=True),
    sa.Column('ogn_balance', sa.Float(), nullable=True),
    sa.Column('dai_balance', sa.Float(), nullable=True),
    sa.Column('investor', sa.Boolean(), nullable=True),
    sa.Column('presale_interest', sa.Boolean(), nullable=True),
    sa.Column('dapp_user', sa.Boolean(), nullable=True),
    sa.Column('employee', sa.Boolean(), nullable=True),
    sa.Column('exchange', sa.Boolean(), nullable=True),
    sa.Column('company_wallet', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text(u'now()'), nullable=True),
    sa.PrimaryKeyConstraint('address')
    )
    op.create_index(op.f('ix_eth_contact_email'), 'eth_contact', ['email'], unique=False)
    op.create_index(op.f('ix_eth_contact_name'), 'eth_contact', ['name'], unique=False)
    op.create_table('token_transaction',
    sa.Column('tx_hash', sa.String(length=66), nullable=False),
    sa.Column('from_address', sa.String(length=42), nullable=True),
    sa.Column('to_address', sa.String(length=42), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('block_number', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text(u'now()'), nullable=True),
    sa.PrimaryKeyConstraint('tx_hash')
    )
    op.create_index(op.f('ix_token_transaction_from_address'), 'token_transaction', ['from_address'], unique=False)
    op.create_index(op.f('ix_token_transaction_to_address'), 'token_transaction', ['to_address'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_token_transaction_to_address'), table_name='token_transaction')
    op.drop_index(op.f('ix_token_transaction_from_address'), table_name='token_transaction')
    op.drop_table('token_transaction')
    op.drop_index(op.f('ix_eth_contact_name'), table_name='eth_contact')
    op.drop_index(op.f('ix_eth_contact_email'), table_name='eth_contact')
    op.drop_table('eth_contact')
    # ### end Alembic commands ###