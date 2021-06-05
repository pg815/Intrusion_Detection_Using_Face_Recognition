#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: guu
@contact: yeexiao@yeah.net
@time: 7/8/17 9:24 PM
"""

import time
from datetime import datetime
import sys

from pytz import timezone

timezone = timezone("Asia/Shanghai")


class DateTimeUtils(object):
    """ Datetime utils

    """

    @classmethod
    def get_current_timestamp(cls):
        """ 获得当前时间戳
        :return:
        """
        return int(time.time())

    @classmethod
    def get_current_datestamp(cls):
        """ 获得当前日期时间戳
        :return:
        """
        date_string = cls.get_formatted_datetime_string(cls.get_current_timestamp(), fmt="%Y-%m-%d")
        return cls.get_timestamp(date_string, fmt="%Y-%m-%d")

    @classmethod
    def get_timestamp(cls, time_string: str, fmt: str):
        """ 获得给定的时间字符串，获得相应的时间戳
        :param time_string: 时间字符串
        :param fmt:
        :return:
        """
        return int(time.mktime(time.strptime(time_string, fmt)))

    @classmethod
    def get_current_formatted_datetime_string(cls, fmt="%Y-%m-%d %H:%M:%S"):
        """ 获得当前日期时间的格式化的字符串
        :param fmt:
        :return:
        """
        return datetime.now(timezone).strftime(fmt)

    @classmethod
    def get_formatted_datetime_string(cls, timestamp: int, fmt="%Y-%m-%d %H:%M:%S"):
        """ 解析给定的时间戳，获得相应的时间字符串
        :param timestamp:
        :param fmt:
        :return:
        """
        return time.strftime(fmt, time.localtime(timestamp))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit("参数有误")

    function = sys.argv[1]
    if function == "-h":
        print("datetime utils\n"
              "1. 获取当前时间戳：python3 datetime_utils.py current_ts \n"
              "2. 获取当前日期的时间戳：python3 datetime_utils.py current_ds \n"
              "3. 获取指定日期的时间戳：python3 datetime_utils.py ts '2017-10-08 12:10:23' '%Y-%m-%d %H:%M:%S' \n"
              "4. 格式化当前时间：python3 datetime_utils.py format_current_datetime ['%Y-%m-%d'] \n"
              "5. 格式化指定时间：python3 datetime_utils.py format_given_datetime 1507435823 ['%Y-%m-%d']")
    if function == "current_ts":
        # 当前时间戳 python3 datetime_utils.py current_ts
        print("当前时间戳：%d" % DateTimeUtils.get_current_timestamp())
    elif function == "current_ds":
        # 当前日期时间戳 python3 datetime_utils.py current_ds
        print("当前日期的时间戳：%d" % DateTimeUtils.get_current_datestamp())
    elif function == "ts":
        # 时间戳 python3 datetime_utils.py ts "2017-10-08 12:10:23" "%Y-%m-%d %H:%M:%S"
        if len(sys.argv) < 4:
            exit("参数有误")
        time_string = sys.argv[2]
        fmt = sys.argv[3]
        print("%s的时间戳：%d" % (time_string, DateTimeUtils.get_timestamp(time_string=time_string, fmt=fmt)))
    elif function == "format_current_datetime":
        # 格式化当前时间戳
        if len(sys.argv) == 3:
            fmt = sys.argv[2]
            print("当前时间为：%s" % DateTimeUtils.get_current_formatted_datetime_string(fmt=fmt))
        else:
            print("当前时间为：%s" % DateTimeUtils.get_current_formatted_datetime_string())
    elif function == "format_given_datetime":
        if len(sys.argv) < 3:
            exit("参数有误")
        timestamp = int(sys.argv[2])
        if len(sys.argv) == 4:
            fmt = sys.argv[3]
            print("%d的格式化时间为：%s" % (timestamp, DateTimeUtils.get_formatted_datetime_string(timestamp=timestamp, fmt=fmt)))
        else:
            print("%d的格式化时间为：%s" % (timestamp, DateTimeUtils.get_formatted_datetime_string(timestamp=timestamp)))
