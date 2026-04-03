from odoo import models, fields, api

class SocialSkillTraining(models.Model):
    _name = 'social.skill.training'
    _description = 'Skill Development & Training'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name of Training", required=True, tracking=True)
    organizer = fields.Char(string="By Organization", required=True)

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    subject_area = fields.Char(string="Subject Area", help="e.g. Digital Marketing, Carpentry")
    duration = fields.Char(string="Duration", help="e.g. 3 Days, 6 Weeks")
    description = fields.Html(string="Training Details")

    # Link to User Model (Frontend Record)
    user_skill_id = fields.Many2one('youth.skill.dev', string="Linked User Skill", readonly=True)

    # ADMIN -> USER SYNC
    @api.model_create_multi
    def create(self, vals_list):
        skills = super().create(vals_list)
        for skill in skills:
            # அட்மின் தரப்பில் புதிதாக உருவாக்கினால், அது Frontend-லும் தெரிய Sync செய்கிறோம்
            if not skill.user_skill_id:
                new_user_skill = self.env['youth.skill.dev'].sudo().create({
                    'name': skill.name,
                    'organizer': skill.organizer or 'Admin',
                    'start_date': skill.start_date,
                    'end_date': skill.end_date,
                    'subject_area': skill.subject_area,
                    'duration': skill.duration,
                    'description': skill.description,
                    'state': 'approved',
                    'admin_skill_id': skill.id
                })
                skill.user_skill_id = new_user_skill.id
        return skills

    def unlink(self):
        for rec in self:
            if rec.user_skill_id:
                rec.user_skill_id.unlink()
        return super().unlink()