"""
组合模式  用于统一管理一个对象以及一组对象
例如管理文件与管理文件夹采用同一个调用接口
"""
# 抽象组件
class FileComponent:
    def display(self):
        pass

# 叶子节点
class File (FileComponent):
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"文件: {self.name}")

# 容器节点
class Folder (FileComponent):
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def display(self):
        print(f"文件夹: {self.name}")
        for child in self.children:
            child.display()

if __name__ == "__main__":
    folder = Folder("根目录")
    folder.children.append(File("文件1"))
    folder.children.append(File("文件2"))
    folder.children.append(Folder("子目录"))
    folder.display()
