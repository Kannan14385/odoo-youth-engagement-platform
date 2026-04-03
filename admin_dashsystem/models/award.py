from odoo import models, fields

class SocialAward(models.Model):
    _name = 'social.award'
    _description = 'Awards and Recognition'

    type = fields.Char(string='Award Type')
    description = fields.Text(string='Description')
    eligibility = fields.Text(string='Eligibility Criteria')
    won_by = fields.Char(string='Won By (Name)')
    year_date = fields.Date(string='Date Awarded')