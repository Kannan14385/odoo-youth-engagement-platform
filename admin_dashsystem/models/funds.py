from odoo import models, fields, api

class SocialFund(models.Model):
    _inherit = 'account.move'  # <--- Inherit Standard Invoicing

    # Link the Invoice/Fund to a Social Project
    fund_project_id = fields.Many2one(
        'project.project',
        string="Linked Social Project",
        help="Select the project this fund is allocated to."
    )

    # Custom Compliance Field for SRS
    audit_status = fields.Selection([
        ('pending', 'Audit Pending'),
        ('cleared', 'Audit Cleared'),
        ('flagged', 'Flagged')
    ], string="Audit Status", default='pending')