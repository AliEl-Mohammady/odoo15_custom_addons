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
        sheet.set_column('D:D', 50)
        sheet.set_column('F:F', 25)
        # worksheet.col(9).width = 300 * 50
        format2 = workbook.add_format({'font_size': 14, 'align': 'vcenter', })
        format4 = workbook.add_format({'font_size': 13, 'align': 'center','bold':True })
        format6 = workbook.add_format({'font_size': 13, 'align': 'vcenter','bold':True })
        format5 = workbook.add_format({'font_size': 14, 'align': 'center',})
        format3 = workbook.add_format(
            {'font_size': 20, 'align': 'center', 'bold': True, 'bg_color': '#f2eee4', 'border': True})
        format7 = workbook.add_format(
            {'font_size': 17, 'align': 'center', 'bg_color': '#f2eee4', 'border': True})
        for obj in lines:
            row = 15
            sheet.merge_range('C1:G1', 'Products Report', format3)
            sheet.merge_range('D14:F14', 'Products Sold During This Time Period', format7)
            sheet.merge_range('D8:F8', 'Best seller Products', format7)
            sheet.write(row, 3, 'Products', format4)
            sheet.write(2, 3, 'User Name : ' + data['user'], format6)
            sheet.write(4, 3, 'Print Date : '+data['form']['create_date'], format6)
            sheet.write(3, 3, 'Company Name : '+data['company'], format6)
            sheet.write(row, 4, 'Quantity', format4)
            sheet.write(row, 5, 'Creation Date', format4)


            for prod in data['products_list']:
                row += 1
                sheet.write(row, 3, prod['name'], format2)
                sheet.write(row, 4, prod['quantity'], format5)
                sheet.write(row, 5, prod['create_date'], format5)
            row = 8
            sheet.write(row, 3, 'Product', format4)
            sheet.write(row, 4, 'Number of Orders', format4)
            sheet.write(row, 5, 'Sale Date', format4)
            for best in data['the_first_product']:
                row += 1
                sheet.write(row, 3, best['name'], format2)
                sheet.write(row, 4, best['quantity'], format5)
                sheet.write(row, 5, best['create_date'], format5)

            for best in data['the_second_product']:
                row += 1
                sheet.write(row, 3, best['name'], format2)
                sheet.write(row, 4, best['quantity'], format5)
                sheet.write(row, 5, best['create_date'], format5)

            for best in data['the_third_product']:
                row += 1
                sheet.write(row, 3, best['name'], format2)
                sheet.write(row, 4, best['quantity'], format5)
                sheet.write(row, 5, best['create_date'], format5)
