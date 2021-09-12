import csv
import json
import pandas as pd
import os
csv_file = 'data.csv'
json_file = 'data.json'


csv_file = pd.DataFrame(pd.read_csv(csv_file, sep = ",", header = 0, index_col = False))
csv_file.to_json(json_file, orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)

os.system('git add .')
os.system('git commit -m "add"')
os.system('git push')