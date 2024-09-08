from .functions import *

name = input(str('Please enter your name here : '))
domain = input(str('Please enter your domain here : '))

email_list = email_generator(name,domain)

for email in email_list:
    if verify_email(email) == True:
        verified_email = email
        break 

if verified_email:
    print(verified_email)

else:
    print('Cant churn the email you looking for')