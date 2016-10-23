# coding: utf-8

import re, os
import shutil
import requests


USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) '\
             'AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'

mobile_ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) '\
            'AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'


def download(src, filename=None, path=None):
    filename = filename or src.split('/')[-1]
    if not filename.lower().endswith(('.jpg', '.png', 'jpeg')):
        filename = '{}.jpg'.format(filename)

    headers = {
        'Referer': src,
        'User-Agent': USER_AGENT
    }
    rsp = requests.get(src, headers=headers, stream=True)
    assert rsp.status_code == 200
    
    path = path or os.getcwd()

    if not os.path.exists(path):
        os.makedirs(path)
    file_path = os.path.join(path, filename)
    with open(file_path, 'wb') as f:
        shutil.copyfileobj(rsp.raw, f)


pixiv_re = b'''
    src="
    http\:\/\/
    (?P<domain>
    i[1-9]
    \.pixiv\.net
    )
    \/c
    \/\d{1,4}x\d{1,4}
    \/img-master\/
    (?P<time_tag>
    img
    \/\d{4}
    \/\d{2}
    \/\d{2}
    \/\d{2}
    \/\d{2}
    \/\d{2}
    )
    \/
    %d
    _
    (?P<illust_seq>
    p
    \d{1,2}
    )*
    .{2,20}
    \.
    (?P<format>
    jpg|png|jpeg
    )
    "
    '''
