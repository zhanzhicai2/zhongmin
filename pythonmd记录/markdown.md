###1.模块
    1.一个好的习惯是将所有的import的放在文件的前面
    2.from fibo import * 这种导入可以将所有的函数导入除以'_'为开头的
    但是这种方式并不鼓励去做。
    3.如果在代码后面添加
        if __name__ == "__main__":
        import sys
        fib(int(sys.argv[1]))
     我们可以在dos中执行 python fibo.py 50
###2.模块的搜索路径
    1.在导入模块的时，解释器会先在当前的目录中搜索是否存在，若存在就会导入，不存在才会去导入
    sys.path变量中给出的目录列表查询
    2.所以在今后的给文件命名的时候不允许取跟模块重名。
###3.dir()函数
内置函数dir()是用于按照模块进行搜索的函数它返回一个字符串类型的存储列表
###6.4包
为了让 Python 将目录当做内容包，目录中必须包含 __init__.py 文件。 这是为了避免一个含有烂俗名字的目录无意中隐藏了稍后在模块搜索路径中出现的有效模块，比如 string 。 最简单的情况下，只需要一个空的 __init__.py 文件即可。
 当然它也可以执行包的初始化代码，或者定义稍后介绍的 __all__ 变量
