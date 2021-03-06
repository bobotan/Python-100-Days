class MusicPlayer(object):
    instance = None
    def __init__(self):
        print('初始化__init__')

    def __new__(cls, *args, **kwargs):
        # 1.创建对象时，__new__方法会被自动调用
        print('创建对象，初始化化空间')

        if cls.instance is None:
            # 2.为对象分配空间
            cls.instance = super().__new__(cls)
        # 3.返回对象的引用
        return cls.instance


cls = MusicPlayer()
print(cls)
cls2=MusicPlayer()
print(cls2)

