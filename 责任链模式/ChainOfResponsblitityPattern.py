"""
责任链模式
    使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。将这个对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止。

role
    1. 处理者（Handler）
        定义一个处理请求的接口，包含一个方法来处理请求和一个方法来设置下一个处理者。
    2. 具体处理者（Concrete Handler）
        实现处理者接口，处理它负责的请求，或者将请求传递给下一个处理者。
"""

# 以流程审核为例
class Handler:
    def set_next_handler(self,next_handler):
        pass
    def handle(self,request):
        pass


class FirstHandler(Handler):
    def __init__(self) -> None:
        self.next_handler = None
    def set_next_handler(self,next_handler):
        self.next_handler = next_handler
    def handle(self):
        print('第一个处理者处理请求')
        if self.next_handler:
            self.next_handler.handle()
    
class SecondHandler(Handler):
    def __init__(self) -> None:
        self.next_handler = None
    def set_next_handler(self,next_handler):
        self.next_handler = next_handler
    def handle(self):
        print('第二个处理者处理请求')
        if self.next_handler:
            self.next_handler.handle()


if __name__ == '__main__':
    first_handler = FirstHandler()
    second_handler = SecondHandler()
    first_handler.set_next_handler(second_handler)
    first_handler.handle()