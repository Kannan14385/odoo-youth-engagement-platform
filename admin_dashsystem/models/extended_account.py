from odoo import models, fields

class AccountMove(models.Model):
    # Inherit 'account.move' AND 'social.audit.mixin'
    _inherit = ['account.move']

    project_reference_id = fields.Many2one('project.project', string='Related Social Project')
    donation_type = fields.Selection([
        ('grant', 'Grant'),
        ('donation', 'Donation'),
        ('sponsorship', 'Sponsorship')
    ], string='Funding Type')