import json
from urllib import parse
from abc import ABCMeta
from abc import abstractmethod


# 搜索建议抽象类
class Base(metaclass=ABCMeta):
    def __init__(self, argv):
        self.query = ' '.join(argv[1:])
        self.safeQuery = parse.quote(self.query)

    @abstractmethod
    def resolve(self):
        pass

    def get_result(self):
        items = self.resolve()
        suggests = {'items': items}
        json_result = json.dumps(suggests, ensure_ascii=False)
        return json_result
