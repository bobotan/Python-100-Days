import json


class model(object):
    def __init__(self, dictmodel):
        self.modelTypeId = dictmodel.modelTypeId
        self.modelName = dictmodel.modelName


class ParamModel(object):
    def __init__(self, **kw):
        self.paramModel = []
        # print(type(paramModel))
        self._paramModel = [model for x in paramModel]
        print(len(self._paramModel))
        # print(self._paramModel[0])


# Day01-15\Day11\
with open(r'E37971408.json', mode='r', encoding='utf-8') as f:
    text = f.read(
    )  # .decode(encoding='gbk',errors='ingore').encode(encoding='utf-8')

kjlList = json.loads(text)
list_key = []
print(type(kjlList))
# kujia = ParamModel(**kjlList)
j = 0
for key in kjlList.keys():
    print(key)
    list_key.append(key)
a = list_key[0]

print(kjlList[a])
print(type(kjlList[a]))
for i in list_key:
    for dic in kjlList[list_key[j]]:
        print(dic)
    j += 1
