# coding:utf-8

import smtplib
from email.mime.text import MIMEText
#
# send email via using smtplib 
#
class MailUtil(object):
	def __init__(self, to, sub, content):
		self.mail_host = 'email server addr, eg: smtp.163.com'
		self.mail_user = 'email address of sender'
		self.mail_pass = 'your email password'
		self.to = to
		self.sub = sub
		self.content = content

	def sendMail(self):
		msg = MIMEText(self.content, _subtype = 'plain', _charset = 'utf-8')
		msg['Subject'] = self.sub
		msg['From'] = self.mail_user
		msg['To'] = ";".join(self.to)
		try:
			server = smtplib.SMTP()
			server.connect(self.mail_host)
			server.login(self.mail_user, self.mail_pass)
			server.sendmail(self.mail_user, self.to, msg.as_string())
			server.close()
			return True
		except Exception, e:
			print str(e)
			return False

