import json
import sys
import urllib.error as err
import urllib.request as req

from common.abcs import Base


class YouKu(Base):
    def resolve(self):
        url = 'https://tip.soku.com/search_tip_1?query=' + self.safeQuery + '&site=2&h=10'
        search = 'https://so.youku.com/search_video/q_'
        items = [
            {'uid': 1.13, 'arg': search + self.safeQuery, 'title': self.query, 'subtitle': '搜索：' + self.query,
             'icon': 'B83BBBD6-5F9F-4434-B6BB-24ACF95F176D.png'}]
        try:
            res = req.urlopen(url)
            data = json.loads(res.read())
            idx = 1.15
            arr = data.get('r', [])
            for item in arr:
                idx += 2.3
                subtitle = '搜索建议：' + item['w']
                items.append(
                    {'uid': idx, 'arg': search + item['w'], 'title': item['w'], 'subtitle': subtitle,
                     'icon': 'B83BBBD6-5F9F-4434-B6BB-24ACF95F176D.png'})
        except err.URLError as e:
            items[0]['subtitle'] = '获取搜索建议异常，请检查网络...'
            print(e)
        return items


if __name__ == '__main__':
    sys.stdout.write(YouKu(sys.argv).get_result())
