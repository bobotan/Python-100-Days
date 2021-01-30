import os
import time


class Clock(object):
    '''
    初始化 init
    '''
    def __init__(self,**kws):
        if 'hour' in kws and 'minute' in kws and 'second' in kws:
            self._hour=kws['hour']
            self._minute=kws['minute']
            self._second=kws['second']
        else:
           print(f'{time.time()} 时间')
           tm=time.localtime(time.time())
           self._hour=tm.tm_hour
           self._minute=tm.tm_min
           self._second=tm.tm_sec

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)
if __name__ == '__main__':
	# clock = Clock(hour=10, minute=5, second=58)
	clock = Clock()
	while True:
		os.system('clear')
		print(clock.show())
		time.sleep(1)
		clock.run()
