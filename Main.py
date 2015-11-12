import coinbase
import requests
import json
import email.utils
import smtplib, smtpd
import imaplib
import asyncore
import sys
import getpass
from email.mime.text import MIMEText
import email



#Conversion of 1 bitcoin = MUR
url = "http://blockchain.info/ticker"
response = requests.get(url)
USD = (json.loads(response.text)['USD']['last'])
MUR = round((USD * 31),2) #formula for dollar to MUR
mmsg = ('1 Bitcoin = ' + str(MUR) + ' MUR')
USD = str(USD)
print (mmsg)
#print trnasaction rate.

coinbase = coinbase.Coinbase.with_api_key("dNCXFJk2cQHTBkKl", "HG8PynSQ1cvdJXwYnZUnXayylHAym8nV")



balance = coinbase.get_balance()
bmsg = ('Balance is ' + balance + ' BTC ')
print(bmsg)
# print bitcoin balance.

#total mur
tmur = round((float(balance) * int(MUR)),2)
print ('Balance is ' +str(tmur) )



# Create the message
fromaddr = 'user@gmail.com'
toaddrs  = '#phonenumber@txt.providor.net'
msg1 = (bmsg + '              ' + str(tmur) + ' MUR' + '                                     ' + mmsg)



server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()

username = 'user@gmail.com'
password = 'password'

server.login(username,password)



    
        
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('user@gmail.com', 'password')
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.






result, data = mail.uid('search', None, "ALL") # search and return uids instead
latest_email_uid = data[0].split()[-1]
result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
raw_email = data[0][1]

rv, mailboxes = mail.list()
if rv == 'OK':
    print ("Mailboxes:")
    print (mailboxes)

 
 

def process_mailbox(mail):
    """
    Do something with emails messages in the folder.  
    For the sake of this example, print some headers.
    """
 
    rv, data = mail.search(None, "ALL")
    if rv != 'OK':
        print ("No messages found!")
        return
 
    for num in data[0].split():
        rv, data = mail.fetch(num, '(RFC822)')
        if rv != 'OK':
            print ("ERROR getting message", num)
            return
        
        msg = (data[0][1])
        msg = msg.decode(encoding='UTF-8')
        msg = email.message_from_string(msg)
        decode = email.header.decode_header(msg['From'])[0]
        msg = (decode[0])
        if (msg == 'phonenumber@txt.providor.net'):
            server.sendmail('user@gmail.com', 'phonenumber@txt.providor.net', msg1)
            server.quit()
            

process_mailbox(mail) # ... do something with emails, see below ...
  
mail.close()
mail.logout()

