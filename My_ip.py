#script is sending email raspberry's ip on boot.
#Use file /etc/rc.local ,before exit 0; , path example sudo python /home/pi/scriptname.py
#OR crontab @reboot

#!/usr/bin/env python2.7
import smtplib, string, subprocess

# Settings
fromaddr = 'yourgoogleaccount@googlemail.com'	#email from
toaddr = 'youremailaddress@somedomain.com'	#email to

# Googlemail login details
username = 'type your googlemail username here'
password = 'type your googlemail password here'

output_if = subprocess.Popen(['/sbin/ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}''], stdout=subprocess.PIPE).communicate()[0]
output_cpu = open('/proc/cpuinfo', 'r').read()

BODY = string.join((
"From: %s" % fromaddr,
"To: %s" % toaddr,
"Subject: Your RasPi just booted",
"",
output_if,
output_cpu,
), "\r\n")

# send the email
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, BODY)
server.quit()