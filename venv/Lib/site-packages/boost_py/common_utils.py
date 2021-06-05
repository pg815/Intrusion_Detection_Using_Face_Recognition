#!/usr/local/bin python3
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: guu
@contact: yeexiao@yeah.net
@time: 7/8/17 9:24 PM
"""

import time
import random


class CommonUtils(object):
    """

    """

    @classmethod
    def get_random_string(cls, length: int = 7):
        """ 生成随机的字符串

        :param length:
        :return:
        """
        return "".join(random.sample("0123456789abcdefghijklmnopqrstevwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length))

    @classmethod
    def get_uuid(cls):
        """ 生成uuid
        :return:
        """
        return str(round(time.time())) + "_" + "".join(random.sample("0123456789abcdefghijklmnopqrstevwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 7))

if __name__ == "__main__":
    print(CommonUtils.get_random_string())
    print(CommonUtils.get_uuid())