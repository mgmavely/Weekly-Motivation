import smtplib
import random
import datetime as dt

# Email information
my_email = ""
password = ""

# Select random quote from quotes.txt
random_line = None
with open("quotes.txt") as file:
    lines = file.readlines()
    random_line = random.choice(lines)


# Check if it is the day to send the weekly email
now = dt.datetime.now()
if now.weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:Weekly Quote\n\n" + random_line)
else:
    print("Not the day.")