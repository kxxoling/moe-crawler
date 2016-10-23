# coding: utf-8

import re
import os

import requests

from utils import download, pixiv_re, mobile_ua


class BaseCrawler(object):
    def __init__(self):
        self.session = requests.Session()


class PixivCrawler(BaseCrawler):
    @staticmethod
    def gen_album_url(album_id):
        return 'http://touch.pixiv.net/member_illust.php?mode=big&illust_id=%d' % album_id

    def extract_user_images(self, user_id):
        pass

    def extract_album(self, album_id):
        album_url = self.gen_album_url(album_id)
        headers = {
            'Referer': album_url,
            'User-Agent': mobile_ua,
            'Host': 'touch.pixiv.net',
            'Accept-Language': 'zh-CN,zh;q=0.8',
        }
        album_rsp = self.session.get(album_url, headers=headers)
        assert album_rsp.status_code == 200
        album_page = album_rsp.text
        pattern = re.compile(pixiv_re % album_id, re.VERBOSE)
        imgs = pattern.findall(album_page)
        return set(imgs)

    @staticmethod
    def build_img_src(album_id, args):
        return 'https://{0}/img-original/{1}/{album_id}_{2}.{3}'.format(*args, album_id=album_id)

    def download_album(self, album_id):
        dir_path = os.path.join(os.getcwd(), str(album_id))
        imgs = self.extract_album(album_id)
        for img in imgs:
            img_src = self.build_img_src(album_id, img)
            download(img_src, path=dir_path)
