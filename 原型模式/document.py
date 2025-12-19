"""
原型模式主要是采用深拷贝的方式创建对象
优化掉原来的new方式
便于快速创建相似对象
"""
import copy

class DocumentPrototype:
    def __init__(self, document_type, content, metadata=None):
        self.document_type = document_type
        self.content = content
        self.metadata = metadata or {}
    
    def clone(self):
        return copy.deepcopy(self)

class WordDocument(DocumentPrototype):
    def __init__(self, content, metadata=None):
        super().__init__("Word", content, metadata)

class ExcelDocument(DocumentPrototype):
    def __init__(self, content, metadata=None):
        super().__init__("Excel", content, metadata)

class PdfDocument(DocumentPrototype):
    def __init__(self, content, metadata=None):
        super().__init__("PDF", content, metadata)

if __name__ == "__main__":
    word_template = WordDocument({"title": "报告", "body": ["段落1"]}, {"author": {"name": "Alice"}})
    excel_template = ExcelDocument({"sheets": [{"A1": "数据1"}]}, {"author": {"name": "Alice"}})
    pdf_template = PdfDocument({"pages": [1, 2, 3]}, {"author": {"name": "Alice"}})
    doc1 = word_template.clone()
    doc2 = word_template.clone()
    doc1.content["body"].append("段落2")
    doc2.metadata["author"]["name"] = "Bob"
    print(doc1 is doc2)
    print(doc1.content)
    print(doc2.metadata)


