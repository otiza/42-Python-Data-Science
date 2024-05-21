import time
from datetime import datetime


current_time = time.time()

print(f"Seconds since January 1, 1970: {current_time} or {current_time:.2e} in scientific notation")

current_date = datetime.now()

print(current_date.strftime('%b %d %Y'))