from odoo import models
from openpyxl import Workbook
import xlwt


class pientCardXlsx(models.AbstractModel):
    _name = 'report.first_project.report_patient_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):

        # workbook = xlwt.Workbook()
        sheet = workbook.add_worksheet('Sale Order Card')
        sheet.set_column('E:E', 20)
        sheet.set_column('D:D', 30)
        # worksheet.col(9).width = 300 * 50
        format2 = workbook.add_format({'font_size': 14, 'align': 'vcenter', })
        format4 = workbook.add_format({'font_size': 13, 'align': 'center', 'bold': True})
        format6 = workbook.add_format({'font_size': 13, 'align': 'vcenter', 'bold': True})
        format5 = workbook.add_format({'font_size': 14, 'align': 'center', })
        format3 = workbook.add_format(
            {'font_size': 20, 'align': 'center', 'bold': True, 'bg_color': '#f2eee4', 'border': True})
        format7 = workbook.add_format(
            {'font_size': 17, 'align': 'center', 'bg_color': '#f2eee4', 'border': True})
        for obj in lines:
            row = 15
            sheet.merge_range('C1:F1', 'Products Report', format3)
            sheet.merge_range('D14:E14', 'Products Sold During This Time Period', format7)
            sheet.merge_range('D8:E8', 'Best seller Products', format7)
            sheet.write(row-1, 3, 'Products', format4)
            sheet.write(2, 3, 'User Name : ' + data['user'], format6)
            sheet.write(4, 3, 'Print Date : ' + data['form']['create_date'], format6)
            sheet.write(3, 3, 'Company Name : ' + data['company'], format6)
            sheet.write(row-1, 4, 'Quantity', format4)
            row=14
            for prod in data['product_list2']:
                row += 1
                sheet.write(row, 3, prod['name'], format2)
                sheet.write(row, 4, prod['quantity'], format5)
            row = 8
            sheet.write(row, 3, 'Product', format4)
            sheet.write(row, 4, 'Number of Orders', format4)
            row += 1
            sheet.write(row, 3, data['product_list2'][0]['name'], format2)
            sheet.write(row, 4, data['product_list2'][0]['quantity'], format5)
            row += 1
            sheet.write(row, 3, data['product_list2'][1]['name'], format2)
            sheet.write(row, 4, data['product_list2'][1]['quantity'], format5)
            row += 1
            sheet.write(row, 3, data['product_list2'][2]['name'], format2)
            sheet.write(row, 4, data['product_list2'][2]['quantity'], format5)

