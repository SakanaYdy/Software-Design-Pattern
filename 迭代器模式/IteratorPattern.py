"""
迭代器模式 
    提供一种方法顺序访问一个聚合对象中的各个元素，而又不暴露其内部的表示。

role
    1. 迭代器（Iterator）
        定义访问和遍历元素的接口。
    2. 具体迭代器（Concrete Iterator）
        实现迭代器接口，完成对聚合对象的遍历。
    3. 聚合（Aggregate）
        定义创建迭代器对象的接口。
    4. 具体聚合（Concrete Aggregate）
        实现聚合接口，返回一个适当的具体迭代器实例。
"""

class ProcessNode:
    def __init__(self, name):
        self.name = name
    
class Iterator:
    def has_next(self):
        pass
    
    def next(self):
        pass

class WorkflowIterator(Iterator):
    def __init__(self, process_nodes):
        self.process_nodes = process_nodes
        self.index = 0
    
    def has_next(self):
        return self.index < len(self.process_nodes)
    
    def next(self):
        if self.has_next():
            process_node = self.process_nodes[self.index]
            self.index += 1
            return process_node
        else:
            raise StopIteration

class Workflow:
    def __init__(self):
        self.process_nodes = []
    
    def add_process_node(self, process_node):
        self.process_nodes.append(process_node)
    
    def create_iterator(self):
        return WorkflowIterator(self.process_nodes)

if __name__ == '__main__':
    workflow = Workflow()
    workflow.add_process_node(ProcessNode('node1'))
    workflow.add_process_node(ProcessNode('node2'))
    workflow.add_process_node(ProcessNode('node3'))
    iterator = workflow.create_iterator()
    while iterator.has_next():
        process_node = iterator.next()
        print(process_node.name)
