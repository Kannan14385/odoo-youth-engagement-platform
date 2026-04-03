from odoo import http
from odoo.http import request

class SocialWebsiteController(http.Controller):

    @http.route('/social-home', type='http', auth='public', website=True)
    def social_landing_page(self, **kwargs):
        return request.render('admin_system.social_landing_page_template', {})