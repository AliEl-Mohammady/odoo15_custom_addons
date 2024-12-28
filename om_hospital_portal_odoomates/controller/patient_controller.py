from odoo import http
from odoo.http import request
import json


class PatientController(http.Controller):
    # type=['http' : for get data from this method,'json' :return this data from function to other]
    # auth=['public','users','none']
    @http.route('/om_hospital/my_patients',type='http', auth='public', website=True)
    def get_patient_method(self):
        # Your controller logic goes here
        # You can fetch data from models, process it, and return results
        # For example, let's fetch some data from a model
        my_patient_records = request.env['hospital.patient'].sudo().search([])
        # patients_data = [{'id': record.id, 'name': record.name, 'age': record.age} for record in my_patient_records]

        # Render a view template and pass data to it
        # return json.dumps({'myPatients': patients_data}) for json
        return request.render('om_hospital.get_patient_controller', {'myPatients': my_patient_records,})



    @http.route('/om_hospital/create_patients',type='http', auth='public', website=True, methods=['POST'],csrf=True)
    def process_form(self, **post):
        # Access the form data submitted by the user
        name = post.get('name')
        phone = post.get('phone')
        reference = post.get('reference')
        age = post.get('age')
        # Process the form data as required

        # For example, create a record in a model
        request.env['hospital.patient'].create({'name': name, 'phone': phone, 'reference': reference, 'age': age})

        # Redirect to a thank you page or any other page
        # return
        return request.redirect('/om_hospital/my_patients')