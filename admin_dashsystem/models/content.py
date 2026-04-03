from odoo import models, fields, api

class SocialContent(models.Model):
    _name = 'social.content'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Website Content Management'
    _rec_name = 'title'

    author_id = fields.Many2one('res.users', string='Author', default=lambda self: self.env.user, readonly=True)
    type = fields.Selection([
        ('blog', 'Blog'),
        ('news', 'News'),
        ('report', 'Report')
    ], string='Content Type', required=True, default='blog')

    title = fields.Char(string='Title', required=True)
    content = fields.Html(string="Content Body", required=True)
    sdg_tags = fields.Char(string='SDG Tags')
    publish_date = fields.Date(string='Publish Date', default=fields.Date.today)

    status = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending Approval'),
        ('published', 'Published'),
        ('rejected', 'Rejected')
    ], string='Status', default='draft', tracking=True)

    rejection_reason = fields.Text(string="Reason for Rejection", tracking=True)

    # --- WORKFLOW ACTIONS ---
    def action_submit(self):
        self.status = 'pending'

    def action_approve(self):
        self.status = 'published'
        # Sync logic is now handled in the user_dashboard module via override

    def action_reject(self):
        self.status = 'rejected'

    def action_reset_draft(self):
        self.status = 'draft'