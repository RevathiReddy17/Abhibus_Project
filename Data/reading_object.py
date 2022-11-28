import xlrd
from Library.config import Config
# path = r'C:\Users\Revathi Reddy\PycharmProjects\Abhibus\abhibus_data.xlsx'

# class ReadExcel:
#
#     def read_data(self,sheetname):
#         wb = xlrd.open_workbook(Config.Data_Path)
#         ws = wb.sheet_by_name(sheetname)
#         columns=ws.ncols
#         rows = ws.get_rows()  #generator onject
#         header = next(rows)
#         data = []
#         for row in rows:
#             values=()
#             for j in range(columns):
#                 values +=(row[j].value,)
#             data.append(values)
#         return data
#     def read_locators(self,sheetname):
#         wb = xlrd.open_workbook(Config.Data_Path)
#         ws = wb.sheet_by_name(sheetname)
#         rows = ws.get_rows()
#         print(rows)
#         header = next(rows)
#         d = {}
#         for row in rows:
#             d[row[0].value] = (row[1].value,row[2].value)
#         return d
#
#     print(read_data())
#     print(read_locators())
    ##############################################
import xlrd
from Library.config import Config


class ReadExcel:

    def read_test_data(self,sheetname):
        wb = xlrd.open_workbook(Config.Data_Path)
        ws = wb.sheet_by_name(sheetname)
        columns = ws.ncols
        rows = ws.get_rows()
        header=next(rows)
        data = []
        for row in rows:
            values = ()
            for j in range(columns):
                values += (row[j].value,)
            data.append(values)
        return data

    def read_locators(self,sheetname):
        wb = xlrd.open_workbook(Config.Data_Path)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)
        d = {}
        for row in rows:
            d[row[0].value] = (row[1].value, row[2].value)
        return d





