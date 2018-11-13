
###### REMOVE HASH FOR COMMANDLINE INPUTS. OTHERWISE, CALL IN OTHER SCRIPTS

# name = input("? Sender Name:")
# recipients = input("? Email Recipients(,):")
# subject = input("? Email Subject:")
# body = input("? Email body text:")
# gmail_user = input("? Gmail:")
# gmail_pwd = input("? Gmail password:")
# file_list = input("? File(s)(,):")

##### START FUNCTION #####
##### NOTE: SET file_list to '' if no file to attach

__author__ = "Trevor Gurgick"
__copyright__ = "Copyright (c) 2018, Trevor Gurgick"

__license__ = "GPL"
__version__ = "1.1"
__status__ = "active"

def send(name,recipients,subject,body,gmail_user,gmail_pwd,file_list):
	
	import requests,datetime,sys,json,base64,csv,smtplib,os
	from email.mime.multipart import MIMEMultipart #for email
	from email.mime.text import MIMEText #for email
	from email.mime.image import MIMEImage #for email
	from email.mime.base import MIMEBase #for email
	from email import encoders
	from dateutil import parser

	recipients = recipients.split(",")
	cwd = os.getcwd()
	filenames = []
	if file_list != '':
		file_list = file_list.split(",")
		for item in file_list:
			item = '%s/%s.csv' %(cwd,item)
			filenames.append(item)
	else:
		pass

	msg = MIMEMultipart()
	msg['From'] = name
	msg['To'] = ", ".join(recipients)
	msg['Subject'] = subject

	msg.attach(MIMEText(body))
	#msg.attach(MIMEText(body,'html')) ### FOR HTML FORMATED TEXT FILE

	if filenames is not None: 
		try: 
			for file in filenames:
				part = MIMEBase('application', 'octet-stream')
				part.set_payload(open(file, 'rb').read())
				encoders.encode_base64(part)
				part.add_header('Content-Disposition', 
					'attachment; filename="%s"' % file)
				msg.attach(part)
		except:
			pass
	else:
		pass

	mailServer = smtplib.SMTP("smtp.gmail.com", 587)
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.ehlo()
	mailServer.login(gmail_user, gmail_pwd)
	mailServer.sendmail(gmail_user, recipients, msg.as_string())
	mailServer.close()


if __name__ == '__main__':
	send(name,recipients,subject,body,gmail_user,gmail_pwd,file_list)
