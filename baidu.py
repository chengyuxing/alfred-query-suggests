#!/usr/bin/python3
# coding=utf-8
import json
import sys
import urllib.error as err
import urllib.request as req

from common.abcs import Base


class BaiDu(Base):
    def resolve(self):
        url = 'https://www.baidu.com/sugrec?ie=utf-8&json=1&prod=pc&wd=' + self.safeQuery
        search = 'https://www.baidu.com/s?wd='
        items = [
            {'uid': 1.13, 'arg': search + self.safeQuery, 'title': self.query, 'subtitle': '搜索：' + self.query,
             'icon': 'D5FE57DE-9CCF-4E53-BA13-80FD301DE2FA.png'}]
        try:
            res = req.urlopen(url)
            data = json.loads(res.read())

            idx = 1.15
            arr = data.get('g', [])
            for item in arr:
                idx += 2.3
                subtitle = '搜索建议：' + item['q']
                items.append(
                    {'uid': idx, 'arg': search + item['q'], 'title': item['q'], 'subtitle': subtitle,
                     'icon': 'D5FE57DE-9CCF-4E53-BA13-80FD301DE2FA.png'})
        except err.URLError as e:
            items[0]['subtitle'] = '获取搜索建议异常，请检查网络...'
            print(e)
        return items


if __name__ == '__main__':
    sys.stdout.write(BaiDu(sys.argv).get_result())
