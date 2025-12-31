"""
策略模式：定义了算法族，分别封装起来，让它们之间可以互相替换，此模式让算法的变化独立于使用算法的客户。

role:
    1. 策略接口
    2. 具体策略类
    3. 上下文类

示例:电商支付方式,优惠策略
"""
class DiscountStrategy:
    def calculate(self, price):
        pass


class FullDiscountStrategy(DiscountStrategy):
    def calculate(self, price):
        # 满减策略
        if price >= 100:
            return price - 20
        else:
            return price

class PercentageDiscountStrategy(DiscountStrategy):
    def calculate(self, price):
        # 折扣策略
        return price * 0.8

# 上下文类
class PriceCalculator:
    def __init__(self, discount_strategy):
        self.discount_strategy = discount_strategy

    def calculate_price(self, price):
        return self.discount_strategy.calculate(price)


if __name__ == "__main__":
    # 满减策略
    full_discount_strategy = FullDiscountStrategy()
    price_calculator = PriceCalculator(full_discount_strategy)
    print(price_calculator.calculate_price(150))  # 输出: 130

    # 折扣策略
    percentage_discount_strategy = PercentageDiscountStrategy()
    price_calculator = PriceCalculator(percentage_discount_strategy)
    print(price_calculator.calculate_price(150))  # 输出: 120.0