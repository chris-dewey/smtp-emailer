# smtp-emailer
Send emails with python

This is not designed as a standalone application, but it can be used as one.

Currently, two functions are available:

  1)  Send a happy birthday email:
    Searches birthdays.csv for today's birthdays, randomly selects a happy birthday letter template, fills
    the name field automatically, and sends it to the birthday boy/s and/or birthday girl/s.
    
  2)  Send a quote of the day email:
    Randomly selects a quote from quotes.txt, modifies the subject line to include the current day of the week,
    and sends it to the email address of your choosing.
    
Before using the happy birthday function, be sure to configure the birthdays.csv file and the letter templates
to your liking.
    
