from odoo import models, fields


class YouthTestimonial(models.Model):
    _name = 'youth.testimonial'
    _description = 'User Testimonials'
    _rec_name = 'contact_person'
    _order = 'date desc'

    contact_person = fields.Char(string="Contact Person", required=True)
    email = fields.Char(string="Email Address", required=True)
    phone = fields.Char(string="Phone Number", required=True)

    category = fields.Selection([
        ('student', 'Student'),
        ('professional', 'Professional'),
        ('ngo', 'NGO / Organization'),
        ('donor', 'Donor'),
        ('volunteer', 'Volunteer')
    ], string="Category", required=True)

    date = fields.Date(string="Date", default=fields.Date.context_today, required=True)
    description = fields.Text(string="Testimony / Description", required=True)

    # Binary field to handle both Image and Video uploads
    media_file = fields.Binary(string="Picture / Video", required=True, attachment=True)
    media_filename = fields.Char(string="Filename")

    state = fields.Selection([
        ('draft', 'Pending Review'),
        ('published', 'Published')
    ], string="Status", default='draft')

    def action_publish(self):
        for rec in self:
            rec.state = 'published'