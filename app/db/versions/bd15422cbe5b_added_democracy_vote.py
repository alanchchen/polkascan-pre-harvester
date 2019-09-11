"""Added Democracy Vote

Revision ID: bd15422cbe5b
Revises: eab2bca0e472
Create Date: 2019-09-05 17:48:49.782425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd15422cbe5b'
down_revision = 'eab2bca0e472'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_democracy_vote',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('democracy_referendum_id', sa.Integer(), nullable=True),
    sa.Column('vote_account_id', sa.String(length=64), nullable=True),
    sa.Column('stash_account_id', sa.String(length=64), nullable=True),
    sa.Column('vote_raw', sa.Integer(), nullable=True),
    sa.Column('vote_yes', sa.Boolean(), nullable=True),
    sa.Column('vote_no', sa.Boolean(), nullable=True),
    sa.Column('stash', sa.Numeric(precision=65, scale=0), nullable=True),
    sa.Column('conviction', sa.Integer(), nullable=True),
    sa.Column('vote_yes_weighted', sa.Numeric(precision=65, scale=0), nullable=True),
    sa.Column('vote_no_weighted', sa.Numeric(precision=65, scale=0), nullable=True),
    sa.Column('created_at_block', sa.Integer(), nullable=False),
    sa.Column('updated_at_block', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_data_democracy_vote_democracy_referendum_id'), 'data_democracy_vote', ['democracy_referendum_id'], unique=False)
    op.create_index(op.f('ix_data_democracy_vote_stash_account_id'), 'data_democracy_vote', ['stash_account_id'], unique=False)
    op.create_index(op.f('ix_data_democracy_vote_vote_account_id'), 'data_democracy_vote', ['vote_account_id'], unique=False)
    op.create_table('data_democracy_vote_audit',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('democracy_referendum_id', sa.Integer(), nullable=False),
    sa.Column('block_id', sa.Integer(), nullable=False),
    sa.Column('extrinsic_idx', sa.Integer(), nullable=True),
    sa.Column('event_idx', sa.Integer(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('data', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_data_democracy_vote_audit_block_id'), 'data_democracy_vote_audit', ['block_id'], unique=False)
    op.create_index(op.f('ix_data_democracy_vote_audit_democracy_referendum_id'), 'data_democracy_vote_audit', ['democracy_referendum_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_data_democracy_vote_audit_democracy_referendum_id'), table_name='data_democracy_vote_audit')
    op.drop_index(op.f('ix_data_democracy_vote_audit_block_id'), table_name='data_democracy_vote_audit')
    op.drop_table('data_democracy_vote_audit')
    op.drop_index(op.f('ix_data_democracy_vote_vote_account_id'), table_name='data_democracy_vote')
    op.drop_index(op.f('ix_data_democracy_vote_stash_account_id'), table_name='data_democracy_vote')
    op.drop_index(op.f('ix_data_democracy_vote_democracy_referendum_id'), table_name='data_democracy_vote')
    op.drop_table('data_democracy_vote')
    # ### end Alembic commands ###