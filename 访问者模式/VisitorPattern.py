"""
访问者模式
    表示一个作用于某对象结构中的各元素的操作。它使你可以在不改变各元素的类的前提下定义作用于这些元素的新操作。

role
    1. 访问者（Visitor）
        定义一个访问操作，它作用于元素的接口。
    2. 具体访问者（Concrete Visitor）
        实现访问者接口，定义对元素的具体访问操作。
    3. 元素（Element）
        定义一个接受访问者的接口，包含一个方法来接受访问者。
    4. 具体元素（Concrete Element）
        实现元素接口，定义对访问者的具体访问操作。
    5. 对象结构（Object Structure）
        包含元素的集合，提供一个方法来遍历元素并接受访问者。

案例：
    以文档转换器为例 使用访问者去实现转换功能
"""

class DocumentVisitor:
    def visit(self,pdf):
        ...
    def visit(self,word):
        ...
    def visit(self,excel):
        ...

class Document:
    def accept(self,visitor):
        ...

class PDFDocument(Document):
    def __init__(self,content) -> None:
        self.content = content
    def accept(self,visitor):
        visitor.visit(self)
    
class WordDocument(Document):
    def __init__(self,content) -> None:
        self.content = content
    def accept(self,visitor):
        visitor.visit(self)

class ExcelDocument(Document):
    def __init__(self,content) -> None:
        self.content = content
    def accept(self,visitor):
        visitor.visit(self)


class HtmlExportVisitor(DocumentVisitor):
    def visit(self, pdf):
        print(f"Exporting PDF {pdf.content} to HTML")
    def visit(self, word):
        print(f"Exporting Word {word.content} to HTML")
    def visit(self, excel):
        print(f"Exporting Excel {excel.content} to HTML")

if __name__ == "__main__":
    pdf = PDFDocument("PDF Content")
    word = WordDocument("Word Content")
    excel = ExcelDocument("Excel Content")

    html_visitor = HtmlExportVisitor()

    pdf.accept(html_visitor)
    word.accept(html_visitor)
    excel.accept(html_visitor)

