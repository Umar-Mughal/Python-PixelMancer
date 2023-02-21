import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('002_send_email_with_html/index.html').read_text())

email = EmailMessage()
email['from'] = 'Umar Farooq'
email['to'] = 'umarmughal1194@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # ping
    smtp.starttls()
    smtp.ehlo()  # ping again
    smtp.login('umar.async@gmail.com', 'ojvxpegcggtgcgnd')
    smtp.send_message(email)
    print('all good boss!')

