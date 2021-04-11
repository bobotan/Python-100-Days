class MusicPlayer(object):

    instance=None
    #重写__new__单例模式
    def __new__(cls, *args, **kwargs):
        try:
            if cls.instance is None:
                cls.instance=super().__new__(cls)
            return cls.instance
        except Exception as result:
            print('发生异常%s'%result)


    def __init__(self):

        print('初始化播放器')

player1=MusicPlayer()
print(player1)
player2=MusicPlayer()
print(player2)