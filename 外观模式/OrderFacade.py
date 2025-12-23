"""
外观模式-订单外观类
在下单时候需要处理很多逻辑 包括库存 物流 支付 等

外观类能够聚合处理相关的接口内容 保证客户端调用的时候只需要调用下单流程即可实现后续一些隐藏逻辑
"""

class InventoryService:
    def check_stock(self, product_id, count):
        print("库存校验通过")


class PaymentService:
    def pay(self, user_id, amount):
        print("支付成功")


class OrderService:
    def create_order(self, user_id, product_id, count):
        print("订单创建完成")


class NotificationService:
    def notify(self, user_id):
        print("通知用户下单成功")


class OrderFacade:
    def __init__(self):
        self.inventory_service = InventoryService()
        self.payment_service = PaymentService()
        self.order_service = OrderService()
        self.notification_service = NotificationService()

    def place_order(self, user_id, product_id, count, amount):
        self.inventory.check_stock(product_id, count)
        self.payment.pay(user_id, amount)
        self.order.create_order(user_id, product_id, count)
        self.notify.notify(user_id)

 
if __name__ == "__main__":
    order_facade = OrderFacade()
    order_facade.place_order("user123", "product456", 2, 100)
