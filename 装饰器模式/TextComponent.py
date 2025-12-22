"""
装饰器模式:动态的给一个对象添加一些额外的职责 而不改变其结构

"""

# 装饰器与原始类都要实现的接口
class TextComponent:
    def rednder(self):
        pass

class PlainTextComponent(TextComponent):
    def __init__(self, text):
        self.text = text

    def rednder(self):
        # print(self.text)
        return self.text

# 实现加粗类额外功能
class BoldTextComponent(TextComponent):
    def __init__(self, text_component):
        self.text_component = text_component

    def rednder(self):
        print("<b>" + self.text_component.rednder() + "</b>")


if __name__ == "__main__":
    text = PlainTextComponent("hello world")
    # 如果要实现加粗功能 只需要调用加粗装饰器即可
    text = BoldTextComponent(text)
    text.rednder()
