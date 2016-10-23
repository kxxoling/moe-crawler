# coding: utf-8
from moe_crawler.crawlers import PixivCrawler


def test_extract_album():
    crawler = PixivCrawler()
    imgs = crawler.extract_album(59563057)
    assert len(imgs) == 1


def test_download_album():
    crawler = PixivCrawler()
    crawler.download_album(59563057)


def test_build_img_src():
    crawler = PixivCrawler()
    assert crawler.build_img_src(59563057, ('i2.pixiv.net', 'img/2016/10/21/01/24/20', 'p0', 'jpg')) == \
        'https://i2.pixiv.net/img-original/img/2016/10/21/01/24/20/59563057_p0.jpg'
