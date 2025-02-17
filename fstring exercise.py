#to calculate how many days are left until the end of the year
from datetime import datetime
today = datetime.today()
end_of_year = datetime(year=today.year, month=12, day=31)
days_left = end_of_year - today
print(f"Days left until the end of the year: {days_left.days}")




#find my local time
from datetime import datetime
today = datetime.today()
print(f"Today's date: {today:%B %d, %Y}")
print(f"Current time: {today:%I:%M %p}")

#to detect the OS of the user
import os
print(f"Operating System: {os.name}")

#to get the current working directory
import os
print(f"Current working directory: {os.getcwd()}")






#to calculate days, weeks, months and years left to 2090
from datetime import datetime
today = datetime.today()
end_of_year = datetime(year=2090, month=12, day=31)
days_left = end_of_year - today
weeks_left = days_left.days // 7
months_left = days_left.days // 30
years_left = days_left.days // 365
print(f"Days left until the end of the year 2090: {days_left.days}")
print(f"Weeks left until the end of the year 2090: {weeks_left}")
print(f"Months left until the end of the year 2090: {months_left}")
print(f"Years left until the end of the year 2090: {years_left}")
