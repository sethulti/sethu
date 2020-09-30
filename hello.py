import time
import sys
import calendar

calendar = calendar.month(2020,10)
print (calendar)
localtime = time.localtime(time.time())
print ("Local current time:", localtime)

msg = "Hello World. Welcome to Python" 
msg1 = "Python is a language that is mainly used by web development"
print(msg)
print(msg1) 

name = "Sethu"

print (name) 

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)

