import xlrd


def read_excel():
	workbook = xlrd.open_workbook(r"C:\Users\shaik\PycharmProjects\Project_VIA\Excell_files\data1.xlsx")
	worksheet = workbook.sheet_by_name("positive")
	rows = worksheet.get_rows()           
	header = next(rows)

	data = []
	for row in rows:
		# print(type(row[0]))
		temp = (row[0].value, row[1].value, row[2].value, row[3].value, row[4].value)
		data.append(temp)
	return data
