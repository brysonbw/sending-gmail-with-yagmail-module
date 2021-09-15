#First  have to install module > pip or pip3 install yagmail in terminal
#Importing the yagmail module
import yagmail

#Initialize variabiles to your email address
senderEmail = 'your_gmail_user_name_@gmail.com'
receiverEmail = senderEmail
subject = 'Enter Subject'

yag = yagmail.SMTP(f'{senderEmail}')

'''
***After registering a keyring entry for yagmail,
you can instantiate the client by simply passing your username, 
e.g. yagmail.SMTP('your_gmail_user_name_@gmail.com').***
'''

contents = ['Enter your message here']

yag.send(receiverEmail, subject, contents)