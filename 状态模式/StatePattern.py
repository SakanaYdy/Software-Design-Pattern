"""
状态模式
    允许对象在内部状态改变时改变它的行为，对象看起来好像修改了它的类。

role
    状态模式包含以下角色：
        环境类（Context）：也称为上下文类，它定义了客户程序需要的接口，维护一个当前状态，并将与状态相关的操作委托给当前状态对象来处理。
        抽象状态类（State）：定义一个接口，用以封装环境对象中的特定状态所对应的行为。
        具体状态类（Concrete State）：实现抽象状态类接口，定义该状态下的行为。

"""

# 以订单状态场景为例
class OrderState:
    def handle(self):
        pass

class PendingState(OrderState):
    def handle(self,order):
        print('待付款状态')
        order.state = PaidState()

class PaidState(OrderState):
    def handle(self,order):
        print('订单已支付，等待发货')
        order.state = ShippedState()

class ShippedState(OrderState):
    def handle(self,order):
        print('订单已发货，等待用户确认')
        order.state = CompletedState()

class CompletedState(OrderState):
    def handle(self,order):
        print('订单已完成')


class Order:
    def __init__(self):
        self.state = PendingState()
    def handle(self):
        self.state.handle(self)


if __name__ == '__main__':
    order = Order()
    order.handle()
    order.handle()
    order.handle()
    order.handle()




