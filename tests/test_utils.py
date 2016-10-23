# coding: utf-8
import re
from moe_crawler.utils import pixiv_re


def test_download():
    pass


def test_pixiv_pattern():
    s = '''
    <img src="http://i5.pixiv.net/c/128x128/img-master/img/2016/10/22/16/48/30/59584762_p0_square1200.png">
    <img src="http://i3.pixiv.net/c/128x128/img-master/img/2016/10/22/16/48/30/59584762_p1_square1200.jpg">
    <img src="http://i3.pixiv.net/c/480x960/img-master/img/2016/10/22/16/48/30/59584762_p0_master1200.jpg">
    '''
    pattern = re.compile(pixiv_re % 59584762, re.VERBOSE)
    assert pattern.findall(s) == [
        ('i5.pixiv.net', 'img/2016/10/22/16/48/30', 'p0', 'png'),
        ('i3.pixiv.net', 'img/2016/10/22/16/48/30', 'p1', 'jpg'),
        ('i3.pixiv.net', 'img/2016/10/22/16/48/30', 'p0', 'jpg'),
        ]
