from datetime import date
from datetime import datetime

today = date.today()

print("Today's date is : {}".format(today))
print("Date : " , today.day , today. month , today.year)
print("Today's weekday : " , today.weekday())

# monday => 0
# Tuesday => 1
# Wendnesday =>2
# Thursday => 3
# Friday => 4
# Staurday => 5
# Sunday=> 6

now = datetime.now()

print("The current date and time is : " , now)
print(now.strftime("%A,%d %b,%Y - %I:%M:%S %p"))
