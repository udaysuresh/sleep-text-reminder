# writing a SMTP based text reminder to automate sleep alarms
# using gmail
# using schedule package to automate the timings
# using tmobile protocol:
# '10digit'@tmomail.net

#user details
user = 'username@gmail.com'
passwd = 'password'
frm = 'from'
to = '(((10 digit phone number)))@tmomail.net'

import smtplib 
import time 
import schedule
from time import strftime

body = "the time is now " + str(time.strftime("%-I:%M on %A, %B %-d")) + ", please consider going to sleep."

#message formatting
#allows for cleaner subject formatting
message = 'Subject: %s\n\n%s' % ('SLEEP REMINDER', body)

#push send
pushto = smtplib.SMTP('smtp.gmail.com:587')
def send():	
	pushto.starttls()
	pushto.login(user,passwd)
	pushto.sendmail(frm, to, message)
	pushto.quit() 

#for a reminder every day at a certain time 
schedule.every().day.at("insert-time").do(send)

#for a reminder every 2 minutes
#schedule.every(2).minutes.do(send)

#allowing scheduling functionality, run with ampersand
while 1:
	schedule.run_pending()
	time.sleep(1)
