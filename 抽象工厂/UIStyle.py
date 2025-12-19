"""
抽象工厂模式主要是用来创建相关或依赖对象的家族，而不需要明确指定具体类
相较于工厂模式而言 抽象工厂适用于一个系列的产品 而工厂模式只是单一产品

role:
抽象工厂:定义了一个接口用于创建相关或依赖对象的家族
具体工厂:实现了抽象工厂接口 负责创建具体的产品
抽象产品:定义了产品的接口
具体产品:实现了抽象产品接口 是具体的产品
客户端:使用抽象工厂接口来创建产品
"""

# 定义产品
class Button:
    def __init__(self, text):
        self.text = text

class Checkbox:
    def __init__(self, text):
        self.text = text

class WindowsButton(Button):
    def __init__(self, text):
        super().__init__(text)
        self.style = "Windows"

class WindowsCheckbox(Checkbox):
    def __init__(self, text):
        super().__init__(text)
        self.style = "Windows"

class MacButton(Button):
    def __init__(self, text):
        super().__init__(text)
        self.style = "Mac"

class MacCheckbox(Checkbox):
    def __init__(self, text):
        super().__init__(text)
        self.style = "Mac"

# 定义工厂
class UiStyleFactory:
    def createButton(self, text):
        pass
    
    def createCheckbox(self, text):
        pass

class WindowsUiStyleFactory(UiStyleFactory):
    def createButton(self, text):
        return WindowsButton(text)
    
    def createCheckbox(self, text):
        return WindowsCheckbox(text)

class MacUiStyleFactory(UiStyleFactory):
    def createButton(self, text):
        return MacButton(text)
    
    def createCheckbox(self, text):
        return MacCheckbox(text)

if __name__ == "__main__":
    # 切换样式时，只需要切换顶层的工厂即可
    windows_factory = WindowsUiStyleFactory()
    mac_factory = MacUiStyleFactory()
    windows_button = windows_factory.createButton("Windows按钮")
    mac_button = mac_factory.createButton("Mac按钮")
    windows_checkbox = windows_factory.createCheckbox("Windows复选框")
    mac_checkbox = mac_factory.createCheckbox("Mac复选框")  
    print(windows_button.style, windows_button.text)
    print(mac_button.style, mac_button.text)
    print(windows_checkbox.style, windows_checkbox.text)
    print(mac_checkbox.style, mac_checkbox.text)
