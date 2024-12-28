from odoo import api, models, _


class PatientCard(models.AbstractModel):
    _name = 'report.om_hospital.report_patient'
    _description = 'Patient Card Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("docids", docids)
        docs = self.env['hospital.patient'].browse(docids[0])
        print("docids", docids[0])
        appointments = self.env['hospital.appointment'].search([('patient_id', '=', docids[0])])
        print("appointments", appointments)
        appointment_list = []
        for app in appointments:
            vals = {
                'name': app.name,
                'booking_date': app.booking_date,
                'state': app.state,
            }
            appointment_list.append(vals)
        print("appointment_list", appointment_list)
        return {
            'doc_model': 'hospital.patient',
            'data': data,
            'docs': docs,
            'appointment_list': appointment_list,
        }
