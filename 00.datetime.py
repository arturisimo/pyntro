from datetime import datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day
current_hr = now.hour
current_min = now.minute
current_sec = now.second

print ('%02d-%02d-%04d' % (now.month, now.day, now.year))
print ('%02d:%02d:%02d' % (now.hour, now.minute, now.second))