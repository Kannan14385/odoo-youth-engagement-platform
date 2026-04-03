from odoo import models, fields, api

class ProjectApproval(models.Model):
    _inherit = 'project.project'

    # Approval Status Field
    approval_status = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Approval Status', default='draft', tracking=True)

    # --- ACTIONS ---
    def action_submit_project(self):
        self.approval_status = 'pending'

    def action_approve_project(self):
        self.approval_status = 'approved'
        # Optional: Automatically set visibility to Public/Portal on approval
        self.privacy_visibility = 'portal'

    def action_reject_project(self):
        self.approval_status = 'rejected'

    def action_reset_project(self):
        self.approval_status = 'draft'


class BlogApproval(models.Model):
    _inherit = 'blog.post'

    # Approval Status for Standard Blogs
    approval_status = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Approval Status', default='draft', tracking=True)

    def action_submit_blog(self):
        self.approval_status = 'pending'

    def action_approve_blog(self):
        self.approval_status = 'approved'
        self.is_published = True  # Auto-publish on approval

    def action_reject_blog(self):
        self.approval_status = 'rejected'
        self.is_published = False

    def action_reset_blog(self):
        self.approval_status = 'draft'
        self.is_published = False

class UserApproval(models.Model):
    _inherit = 'res.users'

    approval_status = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Approval Status', default='draft', tracking=True)

    def action_submit_user(self):
        self.approval_status = 'pending'

    def action_approve_user(self):
        self.approval_status = 'approved'
        self.active = True  # Enable login

    def action_reject_user(self):
        self.approval_status = 'rejected'
        self.active = False # Prevent login

    def action_reset_user(self):
        self.approval_status = 'draft'