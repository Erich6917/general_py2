# -*- coding: utf-8 -*-
# @Time    : 2018/1/31 
# @Author  : LIYUAN134
# @File    : my_email.py
# @Commment: 
#
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

from account_util import *


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_msg(msg):
    from_addr = SECRET_EMAIL_ACCOUNT_187
    from_password = SECRET_EMAIL_PASSWORD_187

    to_addr = SECRET_EMAIL_ACCOUNT_NEWBEE
    smtp_server = 'smtp.163.com'
    message = u'一个亿小目标发送邮件功能测试 \n' + str(msg)
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = _format_addr(u'一号爬虫<%s>' % from_addr)
    msg['To'] = _format_addr(u'管理员<%s>' % to_addr)
    msg['Subject'] = Header(u'一号爬虫状态')

    server = smtplib.SMTP(smtp_server, 25)
    server.login(from_addr, from_password)
    server.sendmail(from_addr, [to_addr], msg.as_string())

    server.quit()

# send_msg("HELLO")
