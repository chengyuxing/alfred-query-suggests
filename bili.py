import json
import sys
import urllib.error as err
import urllib.request as req

from common.abcs import Base


class Bili(Base):
    def resolve(self):
        url = 'https://s.search.bilibili.com/main/suggest?main_ver=v1&term=' + self.safeQuery
        search = 'https://search.bilibili.com/all?keyword='
        items = [
            {'uid': 1.13, 'arg': search + self.safeQuery, 'title': self.query, 'subtitle': '搜索：' + self.query,
             'icon': '0AA53A40-3B3E-4FC4-9414-31C0B8AE2994.png'}]
        try:
            res = req.urlopen(url)
            data = json.loads(res.read())

            idx = 1.15
            result = data['result']
            arr = []
            if result is not None and len(result) > 0:
                arr = result.get('tag', [])
            for item in arr:
                idx += 2.3
                subtitle = '搜索建议：' + item['value']
                items.append(
                    {'uid': idx, 'arg': search + item['value'], 'title': item['value'], 'subtitle': subtitle,
                     'icon': '0AA53A40-3B3E-4FC4-9414-31C0B8AE2994.png'})
        except err.URLError as e:
            items[0]['subtitle'] = '获取搜索建议异常，请检查网络...'
            print(e)
        return items


if __name__ == '__main__':
    sys.stdout.write(Bili(sys.argv).get_result())
