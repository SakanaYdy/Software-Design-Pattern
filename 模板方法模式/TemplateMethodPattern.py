"""
模板方法模式
定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。

role:
    1. 抽象类（Abstract Class）：定义了一个模板方法，该模板方法包含了算法的骨架，同时也定义了一些抽象方法，这些抽象方法在子类中被实现。
    2. 具体类（Concrete Class）：实现了抽象类中定义的抽象方法，完成了算法的具体步骤。
"""
# 订单管理
class OrderProcess:
    def process_order(self):
        self.check_stock() # 检查库存
        self.pay_order() # 付款
        self.deliver_order()    # 发货
        self.notify_customer() # 通知客户
    def check_stock(self):
        print("检查库存")
    def pay_order(self):
        pass
    def deliver_order(self):
        pass
    def notify_customer(self):
        print("客户已通知")


class PhysicalOrderProcess(OrderProcess):
    def pay_order(self):
        print("实体商品付款")
    def deliver_order(self):
        print("实体商品发货")

class VirtualOrderProcess(OrderProcess):
    def pay_order(self):
        print("虚拟商品付款")
    def deliver_order(self):
        print("虚拟商品发货")

if __name__ == "__main__":
    physical_order_process = PhysicalOrderProcess()
    physical_order_process.process_order()
    virtual_order_process = VirtualOrderProcess()
    virtual_order_process.process_order()

    
