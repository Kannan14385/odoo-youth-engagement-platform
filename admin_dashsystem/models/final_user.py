from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


# ==============================================================================
# 1. MASTER DATA (MOVED HERE SO ADMIN CAN SEE IT)
# ==============================================================================
class ThematicArea(models.Model):
    _name = 'thematic.area'
    _description = 'Thematic Areas'
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    color = fields.Integer("Color Index")


class SustainableDevelopmentGoal(models.Model):
    _name = 'sustainable.development.goal'
    _description = 'Sustainable Development Goals'
    _order = 'goal_number'
    name = fields.Char(string="Goal Name", required=True)
    goal_number = fields.Integer(string="Goal Number")
    image = fields.Image("Icon")


# ==============================================================================
# 2. ADMIN USER EXTENSION
# ==============================================================================
class ResUsers(models.Model):
    _inherit = 'res.users'
    _description = 'Social User'

    # --- 1. ROLES & STATUS ---
    user_role = fields.Selection([
        ('student', 'Student'),
        ('professional', 'Professional'),
        ('ngo', 'NGO'),
        ('donor', 'Donor'),
        ('csr', 'CSR Company'),
        ('admin', 'Admin')
    ], string='User Role', default='student', required=True)

    approval_status = fields.Selection([
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Approval Status', default='pending', tracking=True)

    rejection_reason = fields.Text(string="Reason for Rejection")
    show_password = fields.Boolean(string="Show Passwords")

    # --- 2. COMMON PROFILE FIELDS ---
    mobile_contact = fields.Char(string="Mobile Number")
    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute='_compute_age', store=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")
    district = fields.Char(string="District")

    # Standard Fields
    city = fields.Char(related='partner_id.city', readonly=False)
    state_id = fields.Many2one('res.country.state', related='partner_id.state_id', readonly=False)

    # --- 3. ROLE SPECIFIC FIELDS ---

    # Admin
    admin_username = fields.Char(string="Admin Username")
    admin_password = fields.Char(string="Admin Password")
    admin_email = fields.Char(string="Admin Email")  # <--- ADD THIS LINE
    admin_mobile_contact = fields.Char(string="Mobile Number")
    admin_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")

    # Student
    student_username = fields.Char(string="Student Username")
    student_password = fields.Char(string="Student Password")
    college_name = fields.Char(string="College Name")
    course_department = fields.Char(string="College Department")
    student_interests = fields.Char(string="Interests")
    student_description = fields.Text(string="Student Description")
    willing_to_intern = fields.Boolean(string="Willing to join Internship/Project?")

    # Professional
    professional_username = fields.Char(string="Professional Username")
    professional_password = fields.Char(string="Professional Password")
    professional_email = fields.Char(string="Professional Email ID")
    qualification = fields.Char(string="Highest Qualification")
    expertise_area = fields.Char(string="Area of Expertise")
    experience_years = fields.Integer(string="Years of Experience")
    current_organization = fields.Char(string="Organization / Company Name")
    designation = fields.Char(string="Role / Designation")
    mentor_willingness = fields.Boolean(string="Willingness to Mentor / Volunteer")
    professional_profile_description = fields.Text(string="Profile Description")

    # NGO
    ngo_username = fields.Char(string="NGO Username")
    ngo_password = fields.Char(string="NGO Password")
    ngo_contact_person = fields.Char(string="Contact Person Name")
    ngo_contact_email = fields.Char(string="Contact Email")
    ngo_contact_mobile = fields.Char(string="Contact Mobile Number")
    ngo_reg_number = fields.Char(string="Registration Number")
    establishment_year = fields.Integer(string="Year of Establishment")
    ngo_website = fields.Char(string="Website / Social Media Link")
    ngo_address = fields.Text(string="Address")
    ongoing_projects = fields.Text(string="Ongoing Projects Description")
    ngo_focus_area_ids = fields.Many2many(
        comodel_name='thematic.area',
        relation='rel_ngo_focus_admin',
        column1='user_id',
        column2='thematic_area_id',
        string="Focus Areas"
    )

    # Donor
    donor_username = fields.Char(string="Donor Username")
    donor_password = fields.Char(string="Donor Password")
    donor_email = fields.Char(string="Email ID")
    donor_mobile = fields.Char(string="Mobile Number")
    donor_address = fields.Text(string="Address")
    donor_type = fields.Selection([('individual', 'Individual'), ('organization', 'Organization')], string="Donor Type")
    donation_frequency = fields.Selection(
        [('one_time', 'One-Time'), ('monthly', 'Monthly'), ('quarterly', 'Quarterly'), ('yearly', 'Yearly')],
        string="Donation Frequency")
    donor_focus_area_ids = fields.Many2many(
        comodel_name='thematic.area',
        relation='rel_donor_focus_admin',
        column1='user_id',
        column2='thematic_area_id',
        string="Preferred Donation Areas"
    )

    # CSR
    csr_username = fields.Char(string="CSR Username")
    csr_password = fields.Char(string="CSR Password")
    cin_number = fields.Char(string="CIN Number")
    industry_type = fields.Char(string="Industry Type")
    csr_contact_person = fields.Char(string="CSR Contact Person Name")
    csr_contact_email = fields.Char(string="Contact Email")
    csr_contact_mobile = fields.Char(string="Contact Mobile Number")
    csr_budget = fields.Selection([
        ('under_10l', 'Under 10 Lakhs'), ('10l_50l', '10 Lakhs - 50 Lakhs'),
        ('50l_1cr', '50 Lakhs - 1 Crore'), ('above_1cr', 'Above 1 Crore')
    ], string="Annual CSR Budget Range")
    preferred_project_type = fields.Selection(
        [('education', 'Education'), ('health', 'Health'), ('infrastructure', 'Infrastructure'),
         ('environment', 'Environment')], string="Preferred Project Type")
    csr_focus_area_ids = fields.Many2many(
        comodel_name='thematic.area',
        relation='rel_csr_focus_admin',
        column1='user_id',
        column2='thematic_area_id',
        string="CSR Focus Areas"
    )

    thematic_area = fields.Selection([('technology', 'Technology'), ('education', 'Education'), ('health', 'Health'),
                                      ('environment', 'Environment')], string="Thematic Area")
    sdg_alignment = fields.Char(string="SDG Alignment")

    sdg_goals = fields.Many2many(
        comodel_name='sustainable.development.goal',
        relation='rel_users_sdg_admin',
        column1='user_id',
        column2='sdg_id',
        string="SDG Selection"
    )
    confirm_password = fields.Char(string="Confirm Password")
    overall_description = fields.Html(string="Overall Description")

    # --- LOGIC ---
    @api.constrains('student_password', 'professional_password', 'ngo_password', 'donor_password', 'csr_password',
                    'admin_password')
    def _check_password_length(self):
        for record in self:
            pwd = False
            if record.user_role == 'student':
                pwd = record.student_password
            elif record.user_role == 'professional':
                pwd = record.professional_password
            elif record.user_role == 'ngo':
                pwd = record.ngo_password
            elif record.user_role == 'donor':
                pwd = record.donor_password
            elif record.user_role == 'csr':
                pwd = record.csr_password
            elif record.user_role == 'admin':
                pwd = record.admin_password

            if pwd and len(pwd) < 6:
                raise ValidationError(f"Password for {record.user_role.title()} must be at least 6 characters long!")

    @api.constrains('student_password', 'professional_password', 'ngo_password', 'donor_password', 'csr_password',
                    'admin_password', 'confirm_password')
    def _check_password_match(self):
        for record in self:
            pwd = False
            if record.user_role == 'student':
                pwd = record.student_password
            elif record.user_role == 'professional':
                pwd = record.professional_password
            elif record.user_role == 'ngo':
                pwd = record.ngo_password
            elif record.user_role == 'donor':
                pwd = record.donor_password
            elif record.user_role == 'csr':
                pwd = record.csr_password
            elif record.user_role == 'admin':
                pwd = record.admin_password

            if pwd and pwd != record.confirm_password:
                raise ValidationError("Passwords do not match!")

    @api.depends('dob')
    def _compute_age(self):
        today = fields.Date.today()
        for record in self:
            if record.dob:
                record.age = today.year - record.dob.year - (
                        (today.month, today.day) < (record.dob.month, record.dob.day)
                )
            else:
                record.age = 0

    # Sync Helpers
    def action_approve_user(self):
        for user in self:
            user.approval_status = 'approved'
            user.active = True
            if user.partner_id:
                user.partner_id.write({'approval_status': 'approved', 'account_status': 'active'})

    def action_reject_user(self):
        for user in self:
            user.approval_status = 'rejected'
            user.active = False
            if user.partner_id:
                user.partner_id.write({'approval_status': 'rejected', 'account_status': 'inactive'})

    def action_reset_user(self):
        for user in self:
            user.approval_status = 'pending'
            if user.partner_id:
                user.partner_id.write({'approval_status': 'pending'})


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Move these fields here so Admin can see them immediately
    approval_status = fields.Selection([
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Approval Status', default='pending', tracking=True, index=True)

    account_status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended')
    ], default='active', string="Account Status")