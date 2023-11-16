from datetime import *

from main.constant.QueueManagementConstant import date_pattern_format

transaction_id_prefix = "T"

# Get today's date
str_date = str(date.today().strftime(date_pattern_format))

print(transaction_id_prefix + str_date)

