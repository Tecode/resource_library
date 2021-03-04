#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# Author   : mayi
# Blog     : http://www.cnblogs.com/mayi0312/
# Date     : 2019/1/14
# Name     : test01
# Software : PyCharm
# Note     : 用于实现根据公历计算农历的功能
# 导入模块
import datetime

# 数组g_lunar_month_day存入阴历1901年到2050年每年中的月天数信息，
# 阴历每月只能是29或30天，一年用12（或13）个二进制位表示，对应位为1表30天，否则为29天
g_lunar_month_day = [
    0x4ae0, 0xa570, 0x5268, 0xd260, 0xd950, 0x6aa8, 0x56a0, 0x9ad0, 0x4ae8, 0x4ae0,  # 1910
    0xa4d8, 0xa4d0, 0xd250, 0xd548, 0xb550, 0x56a0, 0x96d0, 0x95b0, 0x49b8, 0x49b0,  # 1920
    0xa4b0, 0xb258, 0x6a50, 0x6d40, 0xada8, 0x2b60, 0x9570, 0x4978, 0x4970, 0x64b0,  # 1930
    0xd4a0, 0xea50, 0x6d48, 0x5ad0, 0x2b60, 0x9370, 0x92e0, 0xc968, 0xc950, 0xd4a0,  # 1940
    0xda50, 0xb550, 0x56a0, 0xaad8, 0x25d0, 0x92d0, 0xc958, 0xa950, 0xb4a8, 0x6ca0,  # 1950
    0xb550, 0x55a8, 0x4da0, 0xa5b0, 0x52b8, 0x52b0, 0xa950, 0xe950, 0x6aa0, 0xad50,  # 1960
    0xab50, 0x4b60, 0xa570, 0xa570, 0x5260, 0xe930, 0xd950, 0x5aa8, 0x56a0, 0x96d0,  # 1970
    0x4ae8, 0x4ad0, 0xa4d0, 0xd268, 0xd250, 0xd528, 0xb540, 0xb6a0, 0x96d0, 0x95b0,  # 1980
    0x49b0, 0xa4b8, 0xa4b0, 0xb258, 0x6a50, 0x6d40, 0xada0, 0xab60, 0x9370, 0x4978,  # 1990
    0x4970, 0x64b0, 0x6a50, 0xea50, 0x6b28, 0x5ac0, 0xab60, 0x9368, 0x92e0, 0xc960,  # 2000
    0xd4a8, 0xd4a0, 0xda50, 0x5aa8, 0x56a0, 0xaad8, 0x25d0, 0x92d0, 0xc958, 0xa950,  # 2010
    0xb4a0, 0xb550, 0xb550, 0x55a8, 0x4ba0, 0xa5b0, 0x52b8, 0x52b0, 0xa930, 0x74a8,  # 2020
    0x6aa0, 0xad50, 0x4da8, 0x4b60, 0x9570, 0xa4e0, 0xd260, 0xe930, 0xd530, 0x5aa0,  # 2030
    0x6b50, 0x96d0, 0x4ae8, 0x4ad0, 0xa4d0, 0xd258, 0xd250, 0xd520, 0xdaa0, 0xb5a0,  # 2040
    0x56d0, 0x4ad8, 0x49b0, 0xa4b8, 0xa4b0, 0xaa50, 0xb528, 0x6d20, 0xada0, 0x55b0,  # 2050
]

# 数组gLanarMonth存放阴历1901年到2050年闰月的月份，如没有则为0，每字节存两年
g_lunar_month = [
    0x00, 0x50, 0x04, 0x00, 0x20,  # 1910
    0x60, 0x05, 0x00, 0x20, 0x70,  # 1920
    0x05, 0x00, 0x40, 0x02, 0x06,  # 1930
    0x00, 0x50, 0x03, 0x07, 0x00,  # 1940
    0x60, 0x04, 0x00, 0x20, 0x70,  # 1950
    0x05, 0x00, 0x30, 0x80, 0x06,  # 1960
    0x00, 0x40, 0x03, 0x07, 0x00,  # 1970
    0x50, 0x04, 0x08, 0x00, 0x60,  # 1980
    0x04, 0x0a, 0x00, 0x60, 0x05,  # 1990
    0x00, 0x30, 0x80, 0x05, 0x00,  # 2000
    0x40, 0x02, 0x07, 0x00, 0x50,  # 2010
    0x04, 0x09, 0x00, 0x60, 0x04,  # 2020
    0x00, 0x20, 0x60, 0x05, 0x00,  # 2030
    0x30, 0xb0, 0x06, 0x00, 0x50,  # 2040
    0x02, 0x07, 0x00, 0x50, 0x03  # 2050
]

# 年份
ly = '零一二三四五六七八九'
# 月份
lm = '正二三四五六七八九十冬腊'
# 日份
ld = '初一初二初三初四初五初六初七初八初九初十十一十二十三十四十五十六十七十八十九二十廿一廿二廿三廿四廿五廿六廿七廿八廿九三十'


def strToDate(c_date):
    """
    将8位日期字符串转换成日期格式
    :param c_date: 8位日期字符串
    :return: 对应的日期格式：若返回-1代表字符串长度不对，若返回-2代表转换失败，字符串格式非法
    """
    if len(c_date) != 8:
        # 字符串长度不正确
        return -1
    # 年
    year = int(c_date[:4])
    # 月
    month = int(c_date[4:6])
    # 日
    day = int(c_date[6:])
    try:
        d_date = datetime.date(int(year), int(month), int(day))
        return d_date
    except:
        # 转换失败，格式非法
        return -2


def lunarYearDays(year):
    """
    计算某农历年有多少天
    :param year: 年份（农历）
    :return: 农历天数
    """
    days = 0
    for i in range(1, 13):
        (high, low) = lunarMonthDays(year, i)
        days += high
        days += low

    return days


def lunarMonthDays(year, month):
    """
    计算某年某月农历有多少天
    :param year: 年份（农历）
    :param month: 月份（农历）
    :return: 天数
    """
    if (year < 1901):
        return 30

    high, low = 0, 29
    iBit = 16 - month
    if (month > getLeapMonth(year)) and getLeapMonth(year):
        iBit -= 1
    if (g_lunar_month_day[year - 1901] & (1 << iBit)):
        low += 1
    if (month == getLeapMonth(year)):
        if (g_lunar_month_day[year - 1901] & (1 << (iBit - 1))):
            high = 30
        else:
            high = 29

    return (high, low)


def getLeapMonth(year):
    """
    返回该年的闰月，若返回0，代表该年没有闰月
    :param year: 年份（农历）
    :return: 闰月的月份，若该年没有闰月，则返回0
    """
    flag = g_lunar_month[(year - 1901) // 2]
    if (year - 1901) % 2:
        return flag & 0x0f
    else:
        return flag >> 4


def lunarDate(d_date):
    """
    将公历日期转换成农历日期（查表法）
    :param d_date: 公历日期
    :return: 农历日期
    """
    # 从1901.1.1计算，至今过了多少天
    delta_days = (d_date - datetime.date(1901, 1, 1)).days
    # 阳历1901年02月19日为阴历1901年正月初一
    # 阳历1901年01月01日到1901年02月19日共有49天
    if delta_days < 49:
        year = 1901 - 1
        if delta_days < 19:
            month = 11
            day = delta_days + 11
        else:
            month = 12
            day = delta_days - 18
    else:
        # 下面从阴历1901年正月初一算起
        delta_days -= 49
        year, month, day = 1901, 1, 1
        # 计算年
        temp = lunarYearDays(year)
        while delta_days >= temp:
            delta_days -= temp
            year += 1
            temp = lunarYearDays(year)
        # 计算月
        (foo, temp) = lunarMonthDays(year, month)
        while delta_days >= temp:
            delta_days -= temp
            if (month == getLeapMonth(year)):
                (temp, foo) = lunarMonthDays(year, month)
                if (delta_days < temp):
                    year, month, day = 0, 0, 0
                delta_days -= temp
            month += 1
            (foo, temp) = lunarMonthDays(year, month)
        # 计算日
        day += delta_days
    # 将数字年份信息转成中文年份信息
    temp_year = str(year)
    year = ""
    for i in temp_year:
        year += ly[int(i)]

    return "农历：%s年%s月%s" % (year, lm[month - 1], ld[(day - 1) * 2:day * 2])


def test():
    print(121)

# 主函数
def main():
    # 输入8位公历日期（字符串）
    c_date = input("请输入8位的公历日期（如：20180101）：")
    # 将8位字符串转成日期格式
    d_date = strToDate(c_date)
    if d_date == -1:
        print("您输入的公历日期长度错误！")
        return -1
    elif d_date == -2:
        print("您输入的公历日期格式错误！")
        return -1
    # 将公历日期转换成农历日期
    l_date = lunarDate(d_date)
    # 分别打印公历、农历
    print("公历：%s" % (d_date))
    print(l_date)


# 入口函数
if __name__ == '__main__':
    main()
