""""2.4 partner to organization"

Revision ID: 2b975c5dc25b
Revises: 732c0919c1bd
Create Date: 2020-09-07 10:47:39.293730

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '2b975c5dc25b'
down_revision = '732c0919c1bd'
branch_labels = None
depends_on = None

old_name = "partner"
new_name = "organization"


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('budget_organization_fk', 'budget', type_='foreignkey')
    op.drop_constraint('cloudcredentials_ibfk_1', 'cloudcredentials', type_='foreignkey')
    op.drop_constraint('employee_ibfk_partner', 'employee', type_='foreignkey')
    op.drop_constraint('project_ibfk_2', 'project', type_='foreignkey')
    op.drop_constraint('rule_ibfk_2', 'rule', type_='foreignkey')
    op.drop_constraint('partner_partner_fk', 'partner', type_='foreignkey')
    op.drop_constraint('partner_budget_fk', 'partner', type_='foreignkey')
    op.rename_table(old_name, new_name)
    op.alter_column('organization', 'budget_id', existing_type=sa.String(36),
                    nullable=True)
    op.create_foreign_key('budget_organization_fk', 'budget', 'organization', ['organization_id'], ['id'])
    op.create_foreign_key('cc_organization_fk', 'cloudcredentials', 'organization', ['business_unit_id'], ['id'])
    op.create_foreign_key('employee_organization_fk', 'employee', 'organization', ['business_unit_id'], ['id'])
    op.create_foreign_key('project_organization_fk', 'project', 'organization', ['business_unit_id'], ['id'])
    op.create_foreign_key('rule_organization_fk', 'rule', 'organization', ['business_unit_id'], ['id'])
    op.create_foreign_key('organization_organization_fk',
                          'organization', 'organization', ['parent_id'], ['id'])
    op.create_foreign_key('organization_budget_fk',
                          'organization', 'budget', ['budget_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('rule_organization_fk', 'rule', type_='foreignkey')
    op.drop_constraint('project_organization_fk', 'project', type_='foreignkey')
    op.drop_constraint('employee_organization_fk', 'employee', type_='foreignkey')
    op.drop_constraint('cc_organization_fk', 'cloudcredentials', type_='foreignkey')
    op.drop_constraint('budget_organization_fk', 'budget', type_='foreignkey')
    op.drop_constraint('organization_organization_fk', 'organization', type_='foreignkey')
    op.drop_constraint('organization_budget_fk', 'organization', type_='foreignkey')
    op.alter_column('organization', 'budget_id', existing_type=sa.String(36),
                    nullable=False)
    op.rename_table(new_name, old_name)
    op.create_foreign_key('rule_ibfk_2', 'rule', 'partner', ['business_unit_id'], ['id'])
    op.create_foreign_key('project_ibfk_2', 'project', 'partner', ['business_unit_id'], ['id'])
    op.create_foreign_key('employee_ibfk_partner', 'employee', 'partner', ['business_unit_id'], ['id'])
    op.create_foreign_key('cloudcredentials_ibfk_1', 'cloudcredentials', 'partner', ['business_unit_id'], ['id'])
    op.create_foreign_key('budget_organization_fk', 'budget', 'partner', ['organization_id'], ['id'])
    op.create_foreign_key('partner_partner_fk',
                          'partner', 'partner', ['parent_id'], ['id'])
    op.create_foreign_key('partner_budget_fk',
                          'partner', 'budget', ['budget_id'], ['id'])
    # ### end Alembic commands ###
