import json
import sys
import urllib.error as err
import urllib.request as req

from common.abcs import Base


class Zhihu(Base):
    def resolve(self):
        url = 'https://www.zhihu.com/api/v4/search/suggest?q=' + self.safeQuery
        search = 'https://www.zhihu.com/search?type=content&q='
        items = [
            {'uid': 1.13, 'arg': search + self.safeQuery, 'title': self.query, 'subtitle': '搜索：' + self.query,
             'icon': 'A6D26AB9-4E58-4129-B615-3ED71D0E2DF0.png'}]
        try:
            res = req.urlopen(url)
            data = json.loads(res.read())
            idx = 1.15
            arr = data.get('suggest', [])
            for item in arr:
                idx += 2.3
                subtitle = '搜索建议：' + item['query']
                items.append(
                    {'uid': idx, 'arg': search + item['query'], 'title': item['query'], 'subtitle': subtitle,
                     'icon': 'A6D26AB9-4E58-4129-B615-3ED71D0E2DF0.png'})
        except err.URLError as e:
            items[0]['subtitle'] = '获取搜索建议异常，请检查网络...'
            print(e)
        return items


if __name__ == '__main__':
    sys.stdout.write(Zhihu(sys.argv).get_result())
