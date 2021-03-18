from random import randint
from threading import Thread
from time import time, sleep


class DownLoadTask(Thread):
    def __init__(self, filename):
        super(DownLoadTask, self).__init__()
        self.__filename = filename

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, filename):
        self.__filename = filename

    def run(self):
        """
        重写run
        :return:
        """
        print('开始下载%s...' % self.__filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self.__filename, time_to_download))


if __name__ == "__main__":
    start = time()
    t1 = DownLoadTask('fuckyou.pdf')
    t1.filename = 'sss.pdf'
    t1.start()
    t2 = DownLoadTask('Tokey hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))
