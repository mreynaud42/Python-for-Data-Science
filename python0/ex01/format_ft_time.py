from time import time, gmtime
from calendar import month_abbr

epoch = time()
print(f"Seconds since January 1, 1970: {epoch:,.4f} or {epoch:.2e} in scientific notation")
date = gmtime()
print(month_abbr[date.tm_mon], date.tm_mday, date.tm_year)