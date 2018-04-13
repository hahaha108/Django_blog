# 单例模式类

class Singleton:
    _instance = None

    # 创建实例时调用
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            '''
            这里改变的是全局类的_instance的值，直接把此次创建的实例赋值给_instance，
            下次创建实例时值已经改变，if判断为False，直接把第一次创建的实例返回，
            因此之后每次调用此类都会返回第一次创建的实例。
            '''
            cls._instance =super(Singleton, cls).__new__(cls,*args,**kwargs)
        return cls._instance

    # 初始化实例时调用，因为此时实例已经创建了，这里只是初始化，所以在这里操作是没用的
    def __init__(self):
        self.name = 'aaa'

class A(Singleton):
    pass

if __name__ == '__main__':
    a = A()
    b = A()
    print(a == b)
    print(a.name, b.name)
    a.name = 'bbb'
    b.name = 'ccc'
    # 一个实例改变，所有实例都改变，因为其实都是第一次调用时创建的那一个实例
    print(a == b)
    print(a.name,b.name)
    c = A()
    # c初始化时又给name赋值了
    print(a == b)
    print(a.name,b.name)

    '''
    运行结果：
    True
    aaa aaa
    True
    ccc ccc
    True
    aaa aaa
    '''