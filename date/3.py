import datetime

current_time = datetime.datetime.now()
without_micro = current_time.replace(microsecond = 0)
print(without_micro)