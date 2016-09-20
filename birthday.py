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

if todaymonth== 1:
    S = "January"
elif todaymonth== 2:
    S = "February"
elif todaymonth== 3:
    S = "March"
elif todaymonth== 4:
    S = "April"
elif todaymonth== 5:
    S = "May"
elif todaymonth== 6:
    S = "June"
elif todaymonth== 7:
    S = "July"
elif todaymonth== 8:
    S = "August"
elif todaymonth== 9:
    S = "September"
elif todaymonth== 10:
    S = "October"
elif todaymonth== 11:
    S = "November"
elif todaymonth== 12:
    S = "December"
    
name = input("Hello, what is your name?")
Birthmonth = input(" Hi "+ name + ", what was the name of the month you were born in?")
Birthyear = int(input(" And what year were you born in, "+ name+ "?"))
Birthday = int(input(" And the day?"))
if Birthday== todaydate and Birthmonth== S:
    print(" Happy birthday!")
elif Birthmonth== "October" and Birthday== 31:
    print(" You were born on Halloween!")
elif Birthmonth in ( "September", "October", "November", "september", "october", "november", "9", "10", "11" ):
    if Birthyear < 1980:
        print( name + " , you are a fall baby of the Stone Age.")
    if Birthyear >= 1980 and Birthyear <=1989:
        print( name + " , you are a fall baby of the eighties.")
    if Birthyear >= 1990 and Birthyear <= 1999:
        print( name + " , you are a fall baby of the nineties.")
    if Birthyear >=2000:
        print( name + " , you are a fall baby of the two thousands.")
    
elif Birthmonth in ("December", "January", "February", "March", "december", "january", "february", "march", "12", "1", "2", "3"):
    if Birthyear < 1980:
        print( name + " ,you are a winter baby of the Stone Age.")
    if Birthyear >= 1980 and Birthyear <=1989:
        print( name + " ,you are a winter baby of the eighties.")
    if Birthyear >= 1990 and Birthyear <= 1999:
        print( name + " ,you are a winter baby of the nineties.")
    if Birthyear >=2000:
        print( name + " ,you are a winter baby of the two thousands.")
        
elif Birthmonth in ("April", "May", "april", "may", "4", "5"):
    if Birthyear < 1980:
        print( name + " ,you are a spring baby of the Stone Age.")
    if Birthyear >= 1980 and Birthyear <=1989:
        print( name + " ,you are a spring baby of the eighties.")
    if Birthyear >= 1990 and Birthyear <= 1999:
        print( name + " ,you are a spring baby of the nineties.")
    if Birthyear >=2000:
        print( name + " ,you are a spring baby of the two thousands.")
else : 
    if Birthyear < 1980:
        print( name + " ,you are a summer baby of the Stone Age.")
    if Birthyear >= 1980 and Birthyear <=1989:
        print( name + " ,you are a summer baby of the eighties.")
    if Birthyear >= 1990 and Birthyear <= 1999:
        print( name + " ,you are a summer baby of the nineties.")
    if Birthyear >=2000:
        print( name + " ,you are a summer baby of the two thousands.")