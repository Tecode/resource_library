# -*- coding: utf-8 -*-

import smtplib
import importlib
import lunar_calendar
import random
import datetime
import json
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr

# 定时任务
from apscheduler.schedulers.blocking import BlockingScheduler

# 图片地址
url_array = [
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g6/M00/0A/01/ChMkKV_2dFKIKXcjACboAfcCgo8AAH6vQLeN68AJugZ696.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g5/M00/0F/09/ChMkJlfJQaGIJqqnAAG5FlZTIGIAAU7gANRdSQAAbku420.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x960c5/g5/M00/0F/0C/ChMkJlfJRSOIBtVVAAMtm191MjgAAU8QwGufk4AAy2z233.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x960c5/g5/M00/0F/0C/ChMkJ1fJRSOIBhiRAAHt6kmiUCsAAU8QwHxWTEAAe4C785.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g6/M00/04/09/ChMkKWAHmTuIPphEACJiVRQWu64AAIkpQPHRMAAImJt633.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g6/M00/04/09/ChMkKmAHmTyIKNPaAAb6xVPKiOcAAIkpgAtuAIABvrd985.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g6/M00/04/09/ChMkKWAHmTuIWDx2AAQTlZ-c_zYAAIkpQP4GO0ABBOt181.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g6/M00/04/09/ChMkKmAHmTuIOd99AAErcSKxkwYAAIkpQPx0FMAASuJ627.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g2/M00/05/04/ChMlWV1ADfuIJ0U6AAP4_1uh-AEAAMOaAEMW1MAA_kX725.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s800x1280c5/g5/M00/00/02/ChMkJ1fJVGmIJEUGABjBgwQ_SUoAAU9xAEdeZEAGMGb931.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s800x1280c5/g5/M00/00/02/ChMkJlfJVGiIFVv1AARwxElTOF8AAU9xAEPxnAABHDc214.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g5/M00/00/02/ChMkJlfJVDeIdq1CAAfrWAv6PdMAAU9vwBRGYgAB-tw527.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x960c5/g5/M00/0F/0C/ChMkJlfJRNiIKxUQAA-GBsWV5RwAAU8NgOPbXIAD4Ye121.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x960c5/g5/M00/0F/0C/ChMkJ1fJRNiIF_XyAAd8EHi5AawAAU8NwBV3bwAB3wo278.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g5/M00/0F/0B/ChMkJ1fJRACId6WBAAs-p-sDHSEAAU8DwBwgHQACz6_559.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g5/M00/0F/0B/ChMkJ1fJQ_-IW2WCABhQTtDgoz0AAU8DgOzFDsAGFBm451.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g5/M00/0F/0B/ChMkJlfJQ_6IUT0NABRMHaoSlUsAAU8DgGnte8AFEw1384.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g5/M00/0F/0B/ChMkJlfJQ_-IGHr4AAtcpbj-3IoAAU8DgLL3EgAC1y9819.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x960c5/g5/M00/0F/0A/ChMkJlfJQmqIdw7VABLbeJXqkeQAAU7pwCTL14AEtuQ356.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x960c5/g5/M00/0F/0A/ChMkJ1fJQr6ICpN3ABMz5b-wtT4AAU7vwMCWQcAEzP9874.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x960c5/g5/M00/0F/0A/ChMkJ1fJQr2IcwXZABU2EtHNtAMAAU7vwIjUj4AFTYq418.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g5/M00/0F/0B/ChMkJ1fJQ-CICFp_AAo4dPDsu6MAAU8CAFfifUACjiM787.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s480x854c5/g5/M00/0F/09/ChMkJlfJQaaIe15jAAlaBuQ5m7UAAU7gQLaScEACVoe314.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s480x854c5/g5/M00/0F/09/ChMkJ1fJQaWIcluuAAzEGVPK5q0AAU7gQLjo98ADMQx344.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s480x854c5/g5/M00/0F/09/ChMkJ1fJQaWIbW8eAAhWNY7wU-IAAU7gQL2_ncACFZN380.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g5/M00/0F/0A/ChMkJlfJQp6ITQvtAA04W9NzhOQAAU7tgMVDV8ADThz511.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x960c5/g5/M00/0F/0A/ChMkJlfJQp6IeX8RAAtZYG7iAfkAAU7tgO5qVYAC1l4091.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g4/M0B/08/09/ChMlzF2IQSiIQrmhAAZTUZdKyg4AAXwnAP4ZOMABlNp565.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g4/M01/08/09/ChMlzF2IQSiIEjtGABiz_oYfFwIAAXwngAtCl8AGLQW688.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s800x1280c5/g1/M03/02/0B/ChMljV2IQSqITqE-AATRNBW1i_EAAP4-wFT-WUABNFM032.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s480x854c5/g5/M00/00/02/ChMkJ1fJVUSIFVuIAAK2_o2mCUgAAU92wCzOLoAArcW832.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s480x854c5/g5/M00/00/02/ChMkJ1fJVUSINOXfAAItY0SHkzcAAU92wCfIV8AAi17499.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s480x854c5/g5/M00/00/02/ChMkJlfJVUOIcyvFAAVIKGonI_UAAU92wCMcNoABUhA974.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g2/M00/0F/0E/ChMlWV55dkKIdh5tAAQc1eJPV-sAAN05QJXJiUABBzt748.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g2/M00/0F/0E/ChMlWl55dkOIYRSMABC42GJ70M8AAN05QJsWHAAELjw129.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g6/M00/03/08/ChMkKV-ap6yIKAqjACBOrXKDPcYAAEgnwGT2F4AIE7F716.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g6/M00/03/08/ChMkKV-ap6WIccmHADYOUGKhn94AAEgngMSwd4ANg5o025.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g6/M00/03/08/ChMkKl-ap6OINmwIAC07vPmnm1sAAEgngINyicALTvU404.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g6/M00/04/09/ChMkKmAHmTyIKNPaAAb6xVPKiOcAAIkpgAtuAIABvrd985.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g6/M00/04/09/ChMkKWAHmTuIWDx2AAQTlZ-c_zYAAIkpQP4GO0ABBOt181.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g6/M00/04/09/ChMkKmAHmTuIOd99AAErcSKxkwYAAIkpQPx0FMAASuJ627.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g6/M00/07/01/ChMkKl-g-haIdcCJABmjn2xNP24AAEupgPbmAsAGaO3706.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g6/M00/07/01/ChMkKV-g-hiIFV9sABr1YT-MTPUAAEupwLwiMIAGvV5254.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g5/M00/00/08/ChMkJ18VA1mIcVmOACYgXy4ceDcAAw8mgJRre8AJiB3903.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g5/M00/00/08/ChMkJl8VA1yIa7gFABZIEEV9OUYAAw8mgL-gCgAFkgo683.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g2/M00/0E/01/ChMlWl7XCqSINXSNABIfkiMFBlwAAPtWwPmKJQAEh-q512.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g2/M00/0E/01/ChMlWV7XCqOIREJxABEeBJaWLcgAAPtWwNIrx0AER4c687.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x960c5/g5/M00/0F/0E/ChMkJlfJR8uIRcPAAAZKG-Ys0I8AAU8rwGJNbYABkoz360.png",
    "https://sjbz-fd.zol-img.com.cn/t_s640x960c5/g5/M00/0F/0E/ChMkJ1fJR8qIZxlhAAYCGa_SMuYAAU8rwGR98oABgIx140.png",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g3/M07/0C/05/ChMlV17i4_CIMgreAAl4ZH8XNFAAAUqugBaY0YACXh8294.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g6/M00/08/00/ChMkKWA-79OIIVBxAACbXUoSWKAAAKyQwEsvmMAAJt1275.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g6/M00/08/00/ChMkKmA-79SIMZNNAAC2q2OK47wAAKyQwEo5EQAALbD935.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g6/M00/08/00/ChMkKWA-79OIEjauAACGaIiDgbwAAKyQwEngXkAAIaA007.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g6/M00/08/00/ChMkKWA-79KILNrNAACPkdJhxZAAAKyQwEmTIMAAI-p216.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s1080x1920c5/g6/M00/08/00/ChMkKWA-79SIJOxXAACDkfkK5zEAAKyQwEvAfcAAIOp109.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s800x1280c5/g5/M00/07/04/ChMkJ1jlsOKIUYUYAAQhvA87IyIAAbZHwKhfVgABCHU427.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s800x1280c5/g5/M00/07/04/ChMkJljlsOKIeduCAALpzJmXYBkAAbZHwLR2ugAAunk48.jpeg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g5/M00/07/04/ChMkJljlsOOIE7IZAACvznpiFzAAAbZHwLqxP4AAK_m558.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g5/M00/07/04/ChMkJ1jlsOGIckltAAD6LHNz0YIAAbZHwKdkk0AAPpE697.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g5/M00/07/04/ChMkJljlsOGIQ5h0AADEkjWGSeIAAbZHwKY3NIAAMSq08.jpeg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g5/M00/07/04/ChMkJljlsOKIPErpAACKNSGZMTcAAbZHwK9pzkAAIpN19.jpeg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g5/M00/07/04/ChMkJljlsOKIT8LEAABRht9mBLUAAbZHwKtPPkAAFGe781.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g6/M00/07/02/ChMkKmA9o5OIBkhyAAYPnFcg6PAAAKu1QF-QwwABg-0799.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g6/M00/07/02/ChMkKmA9o5KIK234AAQZnrAlteIAAKu1QCPlecABBm2677.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s640x1136c5/g5/M00/00/03/ChMkJlfJVZSIdRFfAAPuBXrxmkAAAU94gNlCOQAA-4d828.jpg",
    "https://sjbz-fd.zol-img.com.cn/t_s800x1280c5/g5/M00/00/02/ChMkJlfJVGiIEmAKAAXvL2BzqwIAAU9xAEJ1ykABe9H108.jpg"
]


def get_week_day(date):
    week_day_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期日',
    }
    day = date.weekday()
    return week_day_dict[day]


def main(email):
    # 图片地址
    url = url_array[random.randint(0, 65)]
    print(url)
    # 农历日期
    d_date = datetime.datetime.now().date()
    l_date = lunar_calendar.lunarDate(d_date)[8:]
    print(l_date)
    # 星期几
    week = get_week_day(datetime.datetime.now())
    print(week)
    # 日期 03/04
    today_date = datetime.datetime.now().strftime('%m/%d')
    print(today_date)
    # 短语
    file = open('./content.json')
    list_data = json.load(file)['data']
    random_data = list_data[random.randint(0, len(list_data) - 1)]
    print(random_data['content'])
    msg = MIMEText('''
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Dear,洁洁 元气满满的一天开始啦，要开心噢（づ￣ 3￣)づ'</title>
        </head>
        <body>
        <div style="width: 375px; height: 667px; margin: 0 auto; background-repeat: no-repeat; background-size: cover; background-image: url('{url}');">
            <div style="padding: 10% 10% 0 10%; ">
                <div style="color: white; border:8px white solid;background-repeat: no-repeat; background-size: cover; height: 100%; background-image: url('{url}'); ">
                    <div style="min-height: 240px">
                        <p style="margin: 0;padding: 10px;font-size: 20px;font-weight: 500;">Dear 洁洁</p>
                        <p style="margin: 0;padding:  0 10px; font-size: 14px;">新的一天开始啦，要开心噢（づ￣ 3￣)づ</p>
                    </div>
                    <div style="font-size: 36px; padding-left: 10px; font-weight: bold;">{today_date}</div>
                    <p style="padding: 2px 0 2px 10px;margin: 0;">{week}</p>
                    <p style="padding: 0 0 20px 10px;margin: 0;">农历{l_date}</p>
                </div>
            </div>
            <div style="font-size: 14px; margin: 0 10%;padding: 20px 8px 0 8px; line-height: 20px; background-color: white; color: #16181A;">
                <p style="margin: 0; font-size: 40px; line-height: 4px;">“</p>
                <p style="padding: 0 6px 0 10px; margin: 0">{content}</p>
                <p style="margin: 0; font-size: 40px; text-align: right;line-height: 40px;">”</p>
            </div>
        </div>
        </body>
        </html>
    '''.format(l_date=l_date, week=week, content=random_data['content'], url=url, today_date=today_date), 'html',
                   'utf-8')
    msg['From'] = Header('小明', 'utf-8')
    msg['To'] = Header('Dear,洁洁', 'utf-8')
    msg['Subject'] = Header('元气满满的一天开始啦，要开心噢（づ￣ 3￣)づ', 'utf-8').encode()
    # 输入Email地址和口令:
    from_addr = '283731869@qq.com'
    password = 'pmvaazermnqhbiae'
    # 输入收件人地址:
    to_addr = email
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.qq.com'

    server = smtplib.SMTP_SSL(smtp_server)
    server.ehlo(smtp_server)
    # server.starttls() # 如果是SSL，则用 587 端口，再加上这句代码就行了
    server.login(from_addr, password)  # 登录SMTP服务器
    server.sendmail(from_addr, to_addr, msg.as_string())  # 发邮件
    server.quit()


if __name__ == '__main__':
    # main('283731869@qq.com')
    # 定时任务
    print('开始运行脚本')
    scheduler = BlockingScheduler()
    # 在 6：30 运行一次
    scheduler.add_job(main, 'cron', hour='19', minute='32', args=['283731869@qq.com'])
    scheduler.add_job(main, 'cron', hour='7', minute='30', args=['964856415@qq.com'])

    scheduler.start()
