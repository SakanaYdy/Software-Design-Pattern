"""
单例模式样例
实现一个代码生成类 全局保持唯一变量
"""
import threading
# 懒汉模式
class CodeFactoryLazy:
    _instance = None
    @staticmethod
    def getCodeFactory():
        if CodeFactoryLazy._instance is None:
            CodeFactoryLazy._instance = CodeFactoryLazy()
        return CodeFactoryLazy._instance
    def printCodeFactory(self):
        print("懒汉模式")

class CodeFactoryNew:
    _instance = None
    _lock = threading.Lock()
    # 线程安全版本实现
    # 双重检查锁 DCL 工程常用版本
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with CodeFactoryNew._lock:
                if CodeFactoryNew._instance is None:
                    CodeFactoryNew._instance = super().__new__(cls)
        return CodeFactoryNew._instance
    def printCodeFactory(self):
            print("__new__ 实现懒汉模式")

# 饿汉模式
class CodeFactoryEager:
    _instance = None
    @staticmethod
    def getCodeFactory():
        if CodeFactoryEager._instance is None:
            CodeFactoryEager._instance = CodeFactoryEager()
        return CodeFactoryEager._instance

    def printCodeFactory(self):
        print("饿汉模式")

