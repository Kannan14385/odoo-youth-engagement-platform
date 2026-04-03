from odoo import http
from odoo.http import request
import base64

class TestimonialController(http.Controller):

    # Route 1: Displays the Form to the User
    @http.route('/testimonial/submit', type='http', auth="public", website=True)
    def render_testimonial_form(self, **kwargs):
        return request.render('admin_dashsystem.testimonial_form_template')

    # Route 2: Captures the Data and Saves it to the Database
    @http.route('/testimonial/save', type='http', auth="public", methods=['POST'], website=True, csrf=True)
    def save_testimonial(self, **post):
        vals = {
            'contact_person': post.get('contact_person'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'category': post.get('category'),
            'date': post.get('date'),
            'description': post.get('description'),
        }

        # Safely handle the File Upload
        uploaded_file = request.httprequest.files.get('media_file')
        if uploaded_file and uploaded_file.filename:
            file_data = uploaded_file.read()
            vals['media_file'] = base64.b64encode(file_data)
            vals['media_filename'] = uploaded_file.filename

        # Create the record in the backend
        request.env['youth.testimonial'].sudo().create(vals)

        # Re-use the nice success page we created earlier!
        return request.render('display_dashboard.submission_success_template')