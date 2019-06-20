# coding=utf-8
import ssl
import requests
import urllib3
import re

# 因为报错 error:CERTIFICATE_VERIFY_FAILED 所以需要关闭证书验证（MacOs会有这种情况）
ssl._create_default_https_context = ssl._create_unverified_context


class Find_app:
    def get_urls(self):
        links = []
        print('pleass input urls and end of input ok~ ')  # ok~ 后回车
        while True:
            links.append(str(input()))
            if 'ok~' in links:
                break
        return links

    def request_urls(self, links):
        print('=' * 15, 'begin', '=' * 15)
        for link in links[:-1]:
            try:
                session = requests.session()
                session.keep_alive = False  # 关闭多余链接
                requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
                urllib3.disable_warnings()
                content = session.get(url='http://' + link, verify=False, allow_redirects=False).content.decode('UTF-8','ignore').lower()
                if ('移动客户端' in content) or ('ios' in content) or ('android' in content) or ('客户端' in content) or \
                        ('APP下载' in content) or ('安卓' in content) or ('苹果' in content) or ('手机APP' in content):
                    print(link)
            except Exception as error:
                print('*' * 10 + ' error_link:', link + '   ' + 'exception:', error, '*' * 10)
        print('finished~')

    def get_title(self):  # 获取url的title，拖延症～
        pass


f = Find_app()
links = f.get_urls()
f.request_urls(links)
