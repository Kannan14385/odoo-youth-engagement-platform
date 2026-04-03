from odoo import models, fields, api


# 1. Define the Tag Model
class SocialSDG(models.Model):
    _name = 'social.sdg'
    _description = 'Sustainable Development Goals'

    name = fields.Char(string="SDG Goal", required=True)
    color = fields.Integer(string="Color Index")


# 2. Inherit the Standard Project Model
class SocialProject(models.Model):
    _inherit = 'project.project'

    # Organization / NGO linking
    organization_id = fields.Many2one(
        'res.users',
        string="NGO/Organization",
        domain="[('user_role', '=', 'ngo')]"
    )

    # Project Details
    location = fields.Char(string="Location (City/State)")

    # SDG Mapping
    sdg_tag_ids = fields.Many2many(
        'social.sdg',
        string="SDG Goals"
    )

    # Volunteer Requirements
    volunteer_required = fields.Boolean(string="Volunteers Required?")
    volunteer_count_needed = fields.Integer(string="No. of Volunteers")

    # Funding Requirements
    fund_required = fields.Boolean(string="Funds Required?")
    fund_amount_needed = fields.Monetary(
        string="Fund Amount Required",
        currency_field='currency_id'
    )

    # Note: 'approval_status' is handled in your approval_extension.py
    # We do NOT add user_project_id here. It is added in user_dashboard/models/sub.py