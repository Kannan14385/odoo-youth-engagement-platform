from odoo import models, fields, api

class BlogPost(models.Model):
    _inherit = 'blog.post'

    # Thematic Areas
    thematic_area_ids = fields.Many2many('social.sdg', string="Thematic Areas")

    # Date Field
    custom_publish_date = fields.Date(string="Article Date", default=fields.Date.today)

    # Target Audience
    target_audience = fields.Selection([
        ('all', 'General Public'),
        ('youth', 'Youth & Students'),
        ('ngo', 'NGOs & Partners'),
        ('donor', 'Donors & CSR')
    ], string="Target Audience", default='all')

    # Reading Time
    reading_time = fields.Float(string="Reading Time (min)", compute="_compute_reading_time", store=True)

    @api.depends('content')
    def _compute_reading_time(self):
        for rec in self:
            # Simple calculation: 200 words per minute
            words = len(rec.content.split()) if rec.content else 0
            rec.reading_time = round(words / 200, 1)