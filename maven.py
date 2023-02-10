import json
import string
import sys
import urllib.request as req
import urllib.error as err

from common.abcs import Base


class Maven(Base):
    def resolve(self):
        url = 'https://search.maven.org/solrsearch/select?q=' + self.safeQuery
        items = []
        try:
            res = req.urlopen(url)
            data = json.loads(res.read())
            idx = 1.1
            response = data.get('response', {})
            arr = response.get('docs', [])
            for item in arr:
                idx += 0.1
                subtitle = 'GroupId: ' + item['g']
                title = item['a'] + ': ' + item['latestVersion']
                arg = string.Template("""$g/$a/$v""") \
                    .substitute({'g': item['g'], 'a': item['a'], 'v': item['latestVersion']})
                items.append(
                    {'uid': idx, 'arg': arg, 'title': title, 'subtitle': subtitle,
                     'icon': '7415E7C4-4E68-4319-B4EB-452A96D1136D.png'})
        except err.HTTPError as e:
            items.append(
                {'uid': 0, 'arg': '//', 'title': self.query, 'subtitle': '获取搜索建议异常，请检查网络...',
                 'icon': '7415E7C4-4E68-4319-B4EB-452A96D1136D.png'})
            print(e)
        return items


if __name__ == '__main__':
    sys.stdout.write(Maven(sys.argv).get_result())
