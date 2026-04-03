from odoo import models, fields, api

class SocialGrant(models.Model):
    _name = 'social.grant'
    _description = 'Grants & Funding'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Grant Title", required=True, tracking=True)
    applicant_id = fields.Many2one('res.partner', string="Applicant")
    donor_name = fields.Char(string="Funding Organization / Donor", required=True)
    donor_type = fields.Selection([
        ('un', 'UN Agency'),
        ('csr', 'CSR / Corporate'),
        ('foundation', 'Foundation / Trust'),
        ('govt', 'Government'),
        ('other', 'Other')
    ], string="Donor Type", tracking=True)

    source_link = fields.Char(string="Official Source Link", widget="url")
    ref_id = fields.Char(string="Grant Reference ID")

    state = fields.Selection([
        ('upcoming', 'Upcoming'),
        ('open', 'Open'),
        ('closed', 'Closed')
    ], string="Status", default='open', tracking=True)

    # Details
    grant_size = fields.Char(string="Grant Size", help="e.g. $10,000 - $50,000")
    deadline = fields.Date(string="Application Deadline", tracking=True)
    location = fields.Char(string="Location / Region")

    # Criteria
    applicant_eligibility = fields.Char(string="Who Can Apply", help="e.g. Registered NGOs, Section 8 Companies")
    compliance_req = fields.Char(string="Regulatory Compliance", help="e.g. FCRA, 12A, 80G")
    thematic_area_ids = fields.Many2many('social.sdg', string="Thematic Focus")

    # Descriptions
    problem_statement = fields.Html(string="Problem Statement")
    eligibility_criteria = fields.Html(string="Detailed Eligibility")
    documents_required = fields.Html(string="Documents Required")