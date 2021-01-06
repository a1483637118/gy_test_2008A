# -*- coding:utf-8 -*-

from time import sleep


def test_baidu(driver):
    driver.get('http://www.baidu.com')
    driver.send_keys("//*[@id='kw']",'手机')
    sleep(2)




