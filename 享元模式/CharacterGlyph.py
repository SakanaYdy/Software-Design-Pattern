"""
享元模式 主要用于共享相同状态的对象，减少内存占用
这里的案例采用字符渲染的场景
多个相同样式的字符会共用相同的渲染对象，避免重复创建

role:
    享元模式的角色主要包括：
    享元工厂（Flyweight Factory）：负责创建和管理享元对象。
    享元（Flyweight）：定义了共享的状态和行为。
    非享元（Unshared Concrete Flyweight）：如果有一些状态是不共享的，那么可以将这些状态独立出来，作为非享元的一部分。

"""


class Glyph:
    def render(self, x,y,color):
        pass

# 享元类 定义共享的字体等信息
class CharacterGlyph(Glyph):
    def __init__(self, symbol,font):
        self.symbol = symbol
        self.font = font

    def render(self, x,y,color):
        print(f"render {self.symbol} at ({x},{y}) with font {self.font} and color {color}")

# 享元工厂类 负责创建和管理享元对象
class CharacterGlyphFactory:
    def __init__(self):
        self.glyphs = {}

    def get_glyph(self, symbol,font):
        key = f"{symbol}{font}"
        if key not in self.glyphs:
            self.glyphs[key] = CharacterGlyph(symbol,font)
        return self.glyphs[key]

# 非享元类 包含不被共享的一些信息
class CharacterView:
    def __init__(self, glyph,x,y,color):
        self.glyph = glyph
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        self.glyph.render(self.x,self.y,self.color)


if __name__ == '__main__':
    factory = CharacterGlyphFactory()
    glyph1 = factory.get_glyph("A","font1")
    glyph2 = factory.get_glyph("A","font1")
    glyph3 = factory.get_glyph("B","font1")
    print(glyph1 is glyph2)
    print(glyph1 is glyph3)