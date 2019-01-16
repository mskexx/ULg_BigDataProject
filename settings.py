import os
#PRE-PROCESS DIRECTORIES
root_path = "C:\\Users\Kexx\Documents\\Universidad\Master-Primero\BigData"
#From xls to csv
xls_path = os.path.join(root_path, "DATA")
csv_path = os.path.join(root_path, "DATA_CSV")

#From monthly csv to total year csv
month_path = csv_path
year_path = os.path.join(root_path, "DATA_CSV_TOTAL")
