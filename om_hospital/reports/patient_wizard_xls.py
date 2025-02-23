from odoo import models


class pientCardXlsx(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_wizard_xls'
    # _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, lines):
        for obj in lines:
            sheet = workbook.add_worksheet('patient Card')
            sheet.set_column('D:D', 20)  #Increase width of column
            sheet.set_column('C:C', 16)
            sheet.right_to_left()
            format1 = workbook.add_format({'font_size': 16, 'align': 'center', 'bold': True,})
            format2 = workbook.add_format({'font_size': 16, 'align': 'vcenter', })
            # sheet.write(row, col, text or object, style)
            sheet.write(2, 2, 'Name', format1)
            sheet.write(2, 3, 'Reference', format1)
            row = 2
            for app in data['appointments']:
                row +=1
                sheet.write(row, 2, app['ref'], format2)
                sheet.write(row, 3, app['patient_id'][1], format2)

#     def action_print_excel(self):
#             lines = []
#             self.ensure_one()
#
#             workbook = xlwt.Workbook()
#             TABLE_HEADER = xlwt.easyxf(
#                 'font: bold 1, name Tahoma, color-index black,height 300;'
#                 'align: vertical center, horizontal center, wrap off;'
#                 'borders: left thin, right thin, top thin, bottom thin;'
#                 # 'pattern: pattern solid, pattern_fore_colour gray25, pattern_back_colour gray25'
#             )
#
#             TABLE_HEADER_batch = xlwt.easyxf(
#                 'font: bold 1, name Tahoma, color-index black,height 200;'
#                 'align: horiz right, horizontal center, wrap off;'
#                 'borders: left thin, right thin, top thin, bottom thin;'
#                 'pattern: pattern solid, pattern_fore_colour light_green, pattern_back_colour light_green'
#             )
#             header_format = xlwt.easyxf(
#                 'font: bold 1, name Aharoni , color-index black,height 200;'
#                 'align: vertical center, horizontal center, wrap off;'
#                 'alignment: wrap 1;'
#                 'borders: left thin, right thin, top thin, bottom thin;'
#                 # 'pattern: pattern solid, pattern_fore_colour gray25, pattern_back_colour gray25'
#             )
#             header_format0 = xlwt.easyxf(
#                 'font: bold 1, name Aharoni , color-index black,height 200;'
#                 'align: vertical center, horizontal center, wrap off;'
#                 'alignment: wrap 1;'
#                 'borders: left thin, right thin, top thin, bottom thin;'
#                 'pattern: pattern solid, pattern_fore_colour gray25, pattern_back_colour gray25'
#             )
#
#             header_format1 = xlwt.easyxf(
#                 'font: bold 1, name Aharoni , color-index black,height 200;'
#                 'align: vertical center, horizontal right, wrap off;'
#                 'alignment: wrap 1;'
#                 'borders: left thin, right thin, top thin, bottom thin;'
#                 # 'pattern: pattern solid, pattern_fore_colour gray25, pattern_back_colour gray25'
#
#             )
#             header_format2 = xlwt.easyxf(
#                 'font: bold 1, name Aharoni , color-index black,height 200;'
#                 'align: vertical center, horizontal left, wrap off;'
#                 'alignment: wrap 1;'
#                 'borders: left thin, right thin, top thin, bottom thin;'
#                 # 'pattern: pattern solid, pattern_fore_colour gray25, pattern_back_colour gray25'
#
#             )
#
#             TABLE_HEADER_Data = TABLE_HEADER
#             TABLE_HEADER_Data.num_format_str = '#,##0.00_);(#,##0.00)'
#             STYLE_LINE = xlwt.easyxf(
#                 'align: vertical center, horizontal center, wrap off;',
#                 # 'borders: left thin, right thin, top thin, bottom thin; '
#                 # 'num_format_str: General'
#             )
#
#             TABLE_data = xlwt.easyxf(
#                 'font: bold 1, name Aharoni, color-index black,height 200;'
#                 'align: vertical center, horizontal center, wrap off;'
#                 # 'borders: left thin, right thin, top thin, bottom thin;'
#                 # 'pattern: pattern solid, pattern_fore_colour white, pattern_back_colour white'
#             )
#             TABLE_data.num_format_str = '#,##0.00'
#             xlwt.add_palette_colour("gray11", 0x11)
#             workbook.set_colour_RGB(0x11, 222, 222, 222)
#             TABLE_data_tolal_line = xlwt.easyxf(
#                 'font: bold 1, name Aharoni, color-index black,height 200;'
#                 'align: vertical center, horizontal center, wrap off;'
#                 # 'borders: left thin, right thin, top thin, bottom thin;'
#                 # 'pattern: pattern solid, pattern_fore_colour white, pattern_back_colour white'
#             )
#
#             TABLE_data_tolal_line.num_format_str = '#,##0.00'
#             TABLE_data_o = xlwt.easyxf(
#                 'font: bold 1, name Aharoni, color-index black,height 150;'
#                 'align: vertical center, horizontal center, wrap off;'
#                 # 'borders: left thin, right thin, top thin, bottom thin;'
#                 # 'pattern: pattern solid,'
#             )
#             STYLE_LINE_Data = STYLE_LINE
#             STYLE_LINE_Data.num_format_str = '#,##0.00_);(#,##0.00)'
#
#     worksheet = workbook.add_sheet(_('Purchase Report'))
#     lang = self.env.user.lang
#     worksheet.cols_right_to_left = 1
#
#     worksheet.col(0).width = 256 * 20
#     worksheet.col(1).width = 256 * 40
#     worksheet.col(2).width = 256 * 20
#     worksheet.col(3).width = 256 * 20
#     worksheet.col(4).width = 256 * 20
#     worksheet.col(5).width = 256 * 20
#     worksheet.col(6).width = 256 * 20
#     worksheet.col(7).width = 256 * 20
#     worksheet.col(8).width = 256 * 20
#     worksheet.col(9).width = 256 * 20
#     worksheet.col(10).width = 256 * 20
#     worksheet.col(11).width = 256 * 20
#     worksheet.col(12).width = 256 * 20
#     worksheet.col(13).width = 256 * 20
#     worksheet.col(14).width = 256 * 20
#     worksheet.col(15).width = 256 * 20
#     row = 0
#     col = 0
#
#     data = {
#         'date_from': self.date_from,
#         'date_to': self.date_to,
#         'partner_id': self.partner_id.id,
#         'id_company': self.company_id.id,
#         # 'state': self.state
#     }
#     domain = [('product_id', '!=', False), ('product_id.detailed_type', '=', 'product'), '|',
#               ('move_type', '=', 'in_invoice'), ('move_type', '=', 'in_refund')]
#     if data['date_from']:
#         domain.append(('invoice_date', '>=', data['date_from']))
#     if data['date_to']:
#         domain.append(('invoice_date', '<=', data['date_to']))
#     if data.get('state'):
#         domain.append(('state', '=', data.get('state')))
#     if data['partner_id']:
#         domain.append(('partner_id', '=', data['partner_id']))
#     domain.append(('company_id', '=', data['id_company']))
#     docs = self.env['account.move.line'].search(domain)
#     print('ffffffffffff', data.get('state'))
#
#     location = 'Purchase Report'
#     worksheet.write_merge(row, row + 1, col, col + 13, location, TABLE_HEADER)
#     row += 2
#     worksheet.write_merge(row, row + 1, col, col + 13, self.company_id.name, header_format)
#     row += 2
#     worksheet.write_merge(row, row + 1, 0, 6, self.company_id.phone, header_format2)
#     worksheet.write_merge(row, row + 1, 7, 13, _('Tel:'), header_format1)
#     row += 2
#     worksheet.write_merge(row, row + 1, 7, 13, _('print Date:'), header_format1)
#     worksheet.write_merge(row, row + 1, 0, 6, str(fields.Date.today()), header_format2)
#     row += 2
#     worksheet.write_merge(row, row + 1, col, col + 13, _('Detailed Purchase Report'), TABLE_HEADER)
#     row += 2
#
#     worksheet.write_merge(row, row + 1, 6, 13, _('from Date:'), header_format1)
#     worksheet.write_merge(row, row + 1, 0, 5, str(data['date_from']), header_format2)
#     row += 2
#     worksheet.write_merge(row, row + 1, 6, 13, _('To Date:'), header_format1)
#     worksheet.write_merge(row, row + 1, 4, 5, str(data['date_to']), header_format2)
#     worksheet.write_merge(row, row + 1, 2, 3, _('state:'), header_format1)
#     worksheet.write_merge(row, row + 1, 0, 1, self.state, header_format2)
#     row += 2
#     worksheet.write_merge(row, row + 1, col, col, _('#'), header_format0)
#     col += 1
#     worksheet.write_merge(row, row + 1, col, col, _('Invoice No'), header_format0)
#     col += 1
#     worksheet.write_merge(row, row + 1, col, col, _('Date'), header_format0)
#     col += 1
#     worksheet.write_merge(row, row + 1, col, col, _('Account Name'), header_format0)
#     col += 1
#     worksheet.write_merge(row, row + 1, col, col, _('Product Name'), header_format0)
#     col += 1
#     worksheet.write_merge(row, row + 1, col, col, _('Price/Ton'), header_format0)
#     col += 1
#     worksheet.write_merge(row, row + 1, col, col, _('Shipping Price'), header_format0)
#     col += 1
#
#
# worksheet.write_merge(row, row + 1, col, col, _('Quantity'), header_format0)
# col += 1
# worksheet.write_merge(row, row + 1, col, col, _('Price'), header_format0)
# col += 1
# worksheet.write_merge(row, row + 1, col, col, _('Total'), header_format0)
# col += 1
# worksheet.write_merge(row, row + 1, col, col, _('Additions'), header_format0)
# col += 1
#
# worksheet.write_merge(row, row + 1, col, col, _('Product Total Cost'), header_format0)
# col += 1
# worksheet.write_merge(row, row + 1, col, col, _('Total + Additions'), header_format0)
# col += 1
# worksheet.write_merge(row, row + 1, col, col, _('Product Category'), header_format0)
#
# row += 2
# i = 1
# row = 16
# for line in docs:
#     # ad_cost = 0
#     # lc = line.move_id.landed_costs_ids
#     # lc_line = lc.cost_lines
#     # if line.product_id == lc_line.product_id:
#     #     ad_cost = ad_cost + sum(
#     #         ad_price.additional_landed_cost for ad_price in lc.valuation_adjustment_lines)
#     col = 0
#
#     worksheet.write(row, col, i, TABLE_data)
#     col += 1
#     worksheet.write(row, col, line.move_id.name, TABLE_data)
#     col += 1
#     worksheet.write(row, col, str(line.invoice_date), TABLE_data)
#     col += 1
#     # worksheet.write(row, col, self.partner_id, TABLE_data)
#     # worksheet.write(row, col, line.partner_id, TABLE_data)
#     worksheet.write(row, col, line.move_id.name, TABLE_data)
#     # worksheet.write(row, col, line.move_id.partner_id, TABLE_data)
#     col += 1
#     worksheet.write(row, col, line.product_id.name, TABLE_data)
#     col += 1
#     worksheet.write(row, col, line.price_for_ton, TABLE_data_tolal_line)
#     col += 1
#     worksheet.write(row, col, line.Shipping_price, TABLE_data_tolal_line)
#     col += 1
#     worksheet.write(row, col, line.quantity, TABLE_data_tolal_line)
#     col += 1
#     worksheet.write(row, col, line.price_unit, TABLE_data_tolal_line)
#     col += 1
#     worksheet.write(row, col, line.price_subtotal, TABLE_data_tolal_line)
#     col += 1
#     worksheet.write(row, col, line.additions, TABLE_data_tolal_line)
#     col += 1
#
#     worksheet.write(row, col,
#                     (line.additions / line.quantity) + line.price_unit,
#                     TABLE_data_tolal_line)
#     col += 1
#     worksheet.write(row, col, line.price_subtotal + line.additions, TABLE_data_tolal_line)
#     col += 1
#     worksheet.write(row, col, line.product_id.categ_id.name, TABLE_data_tolal_line)
#     row += 1
#     i += 1
#
#     output = BytesIO()
#     workbook.save(output)
#     self.excel_sheet_name = 'Top products'
#
#     self.excel_sheet = base64.b64encode(output.getvalue())
#     self.excel_sheet_name = str(self.excel_sheet_name) + '.xls'
#     output.close()
#     return {
#         'type': 'ir.actions.act_url',
#         'name': 'Purchase Report wizard',
#         'url': '/web/content/purchase.invoices.wizard/%s/excel_sheet/Purchase Report wizard.xls?download=true' % (
#             self.id),
#         'target': 'self'
#     }
# self.ensure_one()
#             workbook = xlwt.Workbook()
#             worksheet = workbook.add_sheet(_('Purchase Report'))
#             lang = self.env.user.lang
#             worksheet.cols_right_to_left = 1
#             output = BytesIO()
#             workbook.save(output)
#             # self.excel_sheet_name = 'Top products'
#             # self.excel_sheet = base64.b64encode(output.getvalue())
#             # self.excel_sheet_name = str(self.excel_sheet_name) + '.xls'
#             output.close()
#
#
#             TABLE_HEADER = xlwt.easyxf(
#                 'font: bold 1, name Tahoma, color-index black,height 300;'
#                 'align: vertical center, horizontal center, wrap off;'
#                 'borders: left thin, right thin, top thin, bottom thin;')
#             # 'pattern: pattern solid, pattern_fore_colour gray25, pattern_back_colour gray25'
#
#             TABLE_data = xlwt.easyxf(
#                 'font: bold 1, name Aharoni, color-index black,height 200;'
#                 'align: vertical center, horizontal center, wrap off;'
#             )
#
#             worksheet.col().width = 256 * 20
#             worksheet.col(1).width = 256 * 40
            # worksheet.col(2).width = 256 * 20
            # worksheet.col(3).width = 256 * 20

            # worksheet.write_merge(row, row + 1, col, col, _('Total + Additions'), header_format0)
            # col += 1
            # worksheet.write_merge(row, row + 1, col, col, _('Product Category'), header_format0)
            #
            # worksheet.write(row, col, i, TABLE_data)
            # col += 1
            # worksheet.write(row, col, line.move_id.name, TABLE_data)
            # col += 1