from odoo import models

#
# class pientCardXlsx(models.AbstractModel):
#     _name = 'report.om_hospital.report_patient_xls'
#     _inherit = 'report.report_xlsx.abstract'
#
#
#     def generate_xlsx_report(self, workbook, data, lines):
#         for obj in lines:
#             sheet = workbook.add_worksheet('patient Card')
#             sheet.set_column(10, 3, 20)
#             # sheet.right_to_left()
#             format1 = workbook.add_format({'font_size': 10, 'align': 'vcenter', 'bold': True})
#             format2 = workbook.add_format({'font_size': 7, 'align': 'vcenter', })
#             sheet.write(2, 2, 'Name', format1)
