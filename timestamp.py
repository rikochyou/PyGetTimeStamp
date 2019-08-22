import time
import datetime


def getAnyTimeStamp(time_num):
    """
    :param time_num:  字符串 格式为：2017-04-03 00:00:00
    :return: 任意时间点的时间戳
    """

    # print(time.mktime(time.strptime(time_str, '%Y-%m-%d %X')))
    return time.mktime(time.strptime(time_str, '%Y-%m-%d %X'))


def getMonthStartTimeStamp():
    """
    :return: 本月开始的时间戳
    """
    # dt1 = time.mktime(datetime.date(datetime.date.today().year, datetime.date.today().month, 1).timetuple())
    # dt3 = datetime.datetime.fromtimestamp(dt1)
    # print(dt3)
    return time.mktime(datetime.date(datetime.date.today().year, datetime.date.today().month, 1).timetuple())


def getWeekStartTimeStamp():
    """
    :return:  本周开始的时间戳
    """
    dt_today = datetime.datetime.today()
    dt_weekday = dt_today.weekday()
    dt_week_start = (dt_today - datetime.timedelta(days = (dt_weekday))).strftime('%Y-%m-%d 00:00')
    dt1 = time.strptime(dt_week_start, '%Y-%m-%d 00:00')

    week_start_time_stamp = time.mktime(dt1)

    dt3 = datetime.datetime.fromtimestamp(week_start_time_stamp)
    # print(dt3)
    return week_start_time_stamp


def getTodayStartTimeStamp():
    """
    :return: 今天开始的时间戳
    """
    dt_today = datetime.datetime.today().strftime('%Y-%m-%d 00:00')
    dt1 = time.strptime(dt_today, '%Y-%m-%d 00:00')
    today_start_time_stamp = time.mktime(dt1)
    # print(today_start_time_stamp)
    # dt3 = datetime.datetime.fromtimestamp(today_start_time_stamp)
    # print(dt3)
    return today_start_time_stamp


def getNDayAgo():
    """

    :return: N天前的时间戳
    """
    # print(datetime.datetime.now() - datetime.timedelta(days=100))
    return datetime.datetime.now() - datetime.timedelta(days=100)

def getNMOnthAgo(_month):
    """

    :param _month:  数字类型
    :return: N个月前该月开始的时间戳
    """
    dt_month = datetime.datetime.today().month
    mmonth = _month % 12
    dt_year = datetime.date.today().year
    cor_month = dt_month - mmonth
    if(dt_month - _month > 0):
        _year = dt_year
    elif _month//12 == 0:
        _year = dt_year - 1
        cor_month = 12 - mmonth
    else:
        _year = dt_year - _month//12

    # dt1
    # print(dt1)
    # print(time.mktime(datetime.date(_year, cor_month, 1).timetuple()))
    return time.mktime(datetime.date(_year, cor_month, 1).timetuple())


def getNMonthAgoEach(num):
    """

    :param num:  数值类型
    :return:  N个月前每个月开始的时间戳
    """
    res = []
    for i in range(num):
        res.append(getNMOnthAgo(i))
    # print(res)
    return res

