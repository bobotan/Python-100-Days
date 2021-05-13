class Tool(object):

    count=0
    @classmethod
    def add_count(cls):
        print('输出count:%d'%cls.count)
    def use_tool(self):
        self.count+=1

t1=Tool()
t2=Tool()
t1.use_tool()

t1.add_count()
