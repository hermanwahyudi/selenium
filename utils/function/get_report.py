import xlsxwriter


report_dir = xlsxwriter.Workbook("report_dir.xlsx")
report_dir_sheet = report_dir.add_worksheet()
report_dir_row = 0
report_dir_col = 0

report_index_product = xlsxwriter.Workbook("report_index_product.xlsx")
report_index_product_sheet = report_index_product.add_worksheet()
bold = report_index_product.add_format({'bold': True})
report_index_product_row = 1
report_index_product_col = 0
