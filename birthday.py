"""
birthday.py
Author: Matthew Fenner
Credit: Robbie
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""


from datetime import datetime
from calendar import month_name

todaymonth = datetime.today().month
todaydate = datetime.today().day

print(todaymonth,"/",todaydate,"/ 2016")

Name = input("What is your name?")
Birthmonth = float(input("What month were you born in?"))
if Birthmonth in [month_name[9], month_name[10], month_name[11]]:
    print("Fall")
elif Birthmonth in [month_name[12], month_name[1], month_name[2], month_name[3]]:
    print("Winter")
elif Birthmonth in [month_name[4], month_name[5]]:
    print("Spring")
else: 
    print("Summer")
Birthyear = float(input("What year were you born in?"))
Birthday = float(input("What day were you born on?"))

print(todaymonth,"/",todaydate,"/ 2016")