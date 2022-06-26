"""

**** SMTP Email Sender ****

Send a motivational quote of the day:
    1. Configure USERNAME, PASSWORD, and SMTP_SERVER with your information.
    2. Be sure to provide the recipient's email in the send_quote call.

Send a happy birthday email.
    1. Configure USERNAME, PASSWORD, and SMTP_SERVER with your information.
    2. Customize letters in letter templates with your personal messages. Leave the [NAME] placeholder.
    3. Add the people you want to send birthday emails following the format specified in birthdays.csv.

"""
import smtplib
from datetime import datetime as dt
import random
import pandas
import re


USERNAME = "email@email.com"
PASSWORD = "password"
SMTP_SERVER = "smtp.gmail.com"


# ----------------------------- Send Quote of the Day ----------------------------- #
def send_quote(send_to_address):
    """
    Send a quote of the day!
    :param send_to_address: Recipient Email
    :return: bool - success (True) or failure (False)
    """
    day = dt.now().weekday()
    try:
        with open("quotes.txt", "r") as qs:
            quote = random.choice(qs.readlines())

        with smtplib.SMTP(SMTP_SERVER) as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=PASSWORD)
            connection.sendmail(
                from_addr=USERNAME,
                to_addrs=send_to_address,
                msg=f"Subject: {day}'s Quote\n\n{quote}")
            connection.close()
    except smtplib.SMTPException:
        return False
    else:
        return True


# ----------------------------- Send Happy Birthday Emails ----------------------------- #
def happy_birthday():
    """
    Check birthdays.csv for today's birthdays. Send email to each birthday boy or girl.
    :return: bool - success (True) or failure (False)
    """
    today = (dt.now().day, dt.now().month)
    birthdays_today = []

    try:
        birthdays = pandas.read_csv("birthdays.csv").to_dict(orient="records")
        birthdays_today = [birthday for birthday in birthdays if (birthday.get("day"), birthday.get("month")) == today]
    except FileNotFoundError:
        print("No birthday list found.")


    for birthday in birthdays_today:
        try:
            with open(f"./letter_templates/letter_{random.randint(1,3)}.txt", encoding="utf-8") as letter:
                letter = letter.read()
                birthday_letter = re.sub(r"\[NAME]", birthday.get("name"), letter)
                with smtplib.SMTP(SMTP_SERVER) as connection:
                    connection.starttls()
                    connection.login(user=USERNAME, password=PASSWORD)
                    connection.sendmail(
                        from_addr=USERNAME,
                        to_addrs=birthday.get("email"),
                        msg=f"Subject: Happy Birthday!\n\n{birthday_letter}"
                    )
        except FileNotFoundError:
            print("No letter match")
            return False
        except smtplib.SMTPException or smtplib.SMTPAuthenticationError:
            print("SMTP Error. Check authentication and try again.")
            return False
        else:
            return True
