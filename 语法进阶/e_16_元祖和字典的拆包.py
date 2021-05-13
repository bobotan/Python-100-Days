def demo(*args,**kwargs):
    print(args)
    print(kwargs)

#元组、字典变量
gl_nums=(1,2,3)
gl_dict={"name":"xiaoming","age":18}

#拆包语法
demo(*gl_dict,**gl_dict)
