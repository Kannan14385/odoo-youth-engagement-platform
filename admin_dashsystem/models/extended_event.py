from odoo import models, fields, api

class SocialEvent(models.Model):
    _inherit = 'event.event'

    # 1. Contact Person Number (Responsible Name is renamed in XML)
    contact_person_number = fields.Char(string="Contact Number")

    # 2. Thematic Areas (Linking to your SDG/Tags model)
    thematic_area_ids = fields.Many2many('social.sdg', string="Thematic Areas")

    # 3. Price Field
    event_price = fields.Monetary(string="Registration Price", currency_field='currency_id', default=0.0)
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)

    # 4. Description
    # We use the standard 'description' field but will clean up the view to show it simply.