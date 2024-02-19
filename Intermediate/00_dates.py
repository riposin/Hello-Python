### Dates ###

from datetime import datetime, date, time

now = datetime.now()
datea = date(2024, 1, 1)
timea = time(12, 0, 0)

print(now.year)
print(now.month)

timestamp = now.timestamp()

print(timestamp)

year_2025 = datetime(2025, 1, 1)

