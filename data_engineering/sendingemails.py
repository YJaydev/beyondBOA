import os
import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import data_engineering.appconstants as appconstants


class emailnotification:

    def sendingEmail(filename):
        emailbody = MIMEMultipart()
        emailbody.attach(MIMEText("Hi"+"\n\n"+"Please have a look for missing requirements."+"\n\n"+"Thanks"))
        emailbody['From'] = appconstants.from_email
        emailbody['To'] = appconstants.to_email
        #emailbody["Cc"] =appconstants.cc_emails
        emailbody['Subject'] = appconstants.email_subject
        attachment = MIMEBase('application', 'octet-stream')
        if os.path.isfile(filename):
            attachment.set_payload(open(filename, 'rb').read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(filename))
            emailbody.attach(attachment)
        mailserver = smtplib.SMTP('smtp.gmail.com', 587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login(appconstants.from_email, appconstants.pwd)
        mailserver.sendmail(appconstants.from_email, appconstants.to_email, emailbody.as_string())
        mailserver.quit()
        print('sent email')

# file = 'datasource/missingData.txt'
# emailnotification.sendingEmail(file)
