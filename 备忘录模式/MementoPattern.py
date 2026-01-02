"""
备忘录模式：在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态。


role:
    备忘录模式包含以下几个角色：
    1. 原发器（Originator）角色：创建一个备忘录，用以记录当前时刻它的内部状态。
    2. 备忘录（Memento）角色：存储原发器的内部状态。
    3. 负责人（Caretaker）角色：负责保存备忘录，不能对备忘录的内容进行操作或检查。
"""

# 以文本编辑器为例

# 备忘录类 
class TextEditorMemento:
    def __init__(self, content):
        self.content = content

# 文档类
class Document:
    def __init__(self, content):
        self.content = content
    def save(self):
        return TextEditorMemento(self.content)
    def restore(self, memento):
        self.content = memento.content

# 历史管理类
class History:
    def __init__(self):
        self.mementos = []
        self.redo_mementos = []
    def pushMemento(self, memento):
        self.mementos.append(memento)
    def popMemento(self):
        return self.mementos.pop()
    def popRedoMemento(self):
        return self.redo_mementos.pop()

if __name__ == "__main__":
    print("--- 1. 初始化 ---")
    document = Document("初始内容")
    print(f"当前文档内容: {document.content}")
    
    history = History()
    
    print("\n--- 2. 修改内容 ---")
    # 修改前先保存当前状态
    history.pushMemento(document.save())
    document.content = "修改后的内容"
    print(f"修改后内容: {document.content}")
    print(">>> 已保存上一步状态")

    print("\n--- 3. 再次修改内容 ---")
    # 修改前先保存当前状态
    history.pushMemento(document.save())
    document.content = "再次修改后的内容"
    print(f"再次修改后内容: {document.content}")
    print(">>> 已保存上一步状态")

    print("\n--- 4. 执行恢复 (Undo) ---")
    # 恢复前，保存当前状态到 Redo 栈，以便重做
    history.redo_mementos.append(document.save())
    
    if history.mementos:
        document.restore(history.popMemento())
        print(f"恢复后内容: {document.content}")
    else:
        print("无法恢复: 历史记录为空")

    print("\n--- 5. 执行重做 (Redo) ---")
    if history.redo_mementos:
        # 重做前，保存当前状态到 Undo 栈（如果支持多次 Undo/Redo，这里逻辑会更复杂，此处仅演示简单 Redo）
        history.pushMemento(document.save()) 
        document.restore(history.popRedoMemento())
        print(f"重做后内容: {document.content}")
    else:
        print("无法重做: Redo 记录为空")