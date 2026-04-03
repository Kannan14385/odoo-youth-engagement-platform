from odoo import models, fields, api
from datetime import timedelta


class SocialOpportunity(models.Model):
    _name = 'social.opportunity'
    _description = 'Jobs, Internships & Volunteering'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # 1. Title & Organization
    name = fields.Char(string="Opportunity Title", required=True, tracking=True)
    org_id = fields.Many2one('res.users', string="Organization",
                             domain="[('user_role', 'in', ['ngo', 'csr', 'institution', 'admin'])]",
                             default=lambda self: self.env.user)

    # 2. Type (Radio Buttons)
    type = fields.Selection([
        ('volunteer', 'Volunteering Event'),
        ('job', 'Job / Employment'),
        ('internship', 'Internship')
    ], string="Opportunity Type", required=True, default='internship', tracking=True)

    # 3. Dates
    date_posted = fields.Date(string="Date Posted", default=fields.Date.today, tracking=True)
    date_deadline = fields.Date(string="Valid Until", help="Date when this opportunity expires.")

    # 4. Description (HTML for rich text)
    description = fields.Html(string="Full Description", help="Detailed job/role description.")

    # 5. Requirements & Academics
    skill_ids = fields.Many2many('social.skill', string="Skills Required")
    subject_ids = fields.Char(string="Subjects / Streams", help="e.g. Computer Science, Social Work")
    qualification = fields.Char(string="Qualification Required", help="e.g. Bachelor's Degree, MCA")

    # 6. Impact (Thematic & SDGs)
    thematic_area_ids = fields.Many2many('social.sdg', string="Thematic Areas / SDGs")

    # 7. Contact Info (For both Org & Individual)
    contact_name = fields.Char(string="Contact Person")
    contact_email = fields.Char(string="Contact Email")
    contact_phone = fields.Char(string="Contact Phone")

    # 8. Extra Fields (Logistics)
    mode = fields.Selection([
        ('onsite', 'On-Site'),
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid')
    ], string="Work Mode", default='onsite')

    location = fields.Char(string="Location (City/State)")
    max_students = fields.Integer(string="No. of Openings", default=1)
    duration = fields.Char(string="Duration", help="e.g. 3 Months, Permanent")
    salary_stipend = fields.Char(string="Salary / Stipend", help="e.g. $500/month or 'Unpaid'")

    # Status Bar Logic (Renamed 'status' to 'state' for standard Odoo conventions)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('closed', 'Closed')
    ], string="Status", default='draft', tracking=True)

    def action_publish(self):
        self.state = 'published'

    def action_close(self):
        self.state = 'closed'