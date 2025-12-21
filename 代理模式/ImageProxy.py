"""
代理模式 主要用于创建一个第三者来管理真实对象的访问
实现什么时候可以访问 什么权限可以访问 如何访问 这些类似的访问控制功能

role:
    1. 代理类 负责管理真实对象的访问
    2. 真实类 被代理的对象
    3. 抽象主体接口 定义了真实类和代理类的公共接口

"""

# 抽象主体接口 
class image:
    def display():
        pass

class RealImage(image):
    def __init__(self, filename):
        self.filename = filename
        print("read from disk")

    def display(self):
        print("display image")

class ProxyImage(image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()


if __name__ == "__main__":
    proxy_image = ProxyImage("test.jpg")
    proxy_image.display()

    # 控制第二次加载的时候不用再从磁盘读入
    # 实现懒加载
    proxy_image.display()
