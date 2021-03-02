import smtplib
from email.mime.text import MIMEText
from apscheduler.schedulers.background import BackgroundScheduler

# 定时任务
scheduler = BlockingScheduler()
# 每天9：30给女朋友发送每日一句
# scheduler.add_job(start_today_info, 'cron', hour=9, minute=30)
scheduler.start()


# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://blog.pangao.vip">PanGao’s blog</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')
#
#
# # 输入Email地址和口令:
# from_addr = '283731869@qq.com'
# password = 'pmvaazermnqhbiae'
# # 输入收件人地址:
# to_addr = 'ming.xie@naoxuejia.com'
# # 输入SMTP服务器地址:
# smtp_server = 'smtp.qq.com'
#
# server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
# # server.starttls() # 如果是SSL，则用 587 端口，再加上这句代码就行了
# server.set_debuglevel(1)  # 打印出和SMTP服务器交互的所有信息
# server.login(from_addr, password)  # 登录SMTP服务器
# server.sendmail(from_addr, [to_addr], msg.as_string())  # 发邮件
# server.quit()
