"""
命令模式 旨在构建一个统一的任务调度管理，
将请求封装成一个对象，从而使你可用不同的请求对客户进行参数化；
对请求排队或记录请求日志，以及支持可撤销的操作。

role:
    命令模式包含以下几个角色：
    1. 命令（Command）角色：定义一个接口，用于执行请求。
    2. 具体命令（ConcreteCommand）角色：实现命令接口，将一个接收者对象绑定于一个动作。
    3. 接收者（Receiver）角色：知道如何实施与执行一个请求相关的操作。
    4. 调用者（Invoker）角色：要求命令对象执行请求。
"""
# 命令类
class Task:
    def execute(self):
        pass

# 实现具体命令
class SendEmailTask(Task):
    def execute(self):
        print("发送邮件")

class CalcTask(Task):
    def execute(self):
        print("计算")


# 任务调度器
class TaskScheduler:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)
        
    def execute_tasks(self):
        for task in self.tasks:
            task.execute()

if __name__ == "__main__":
    task_scheduler = TaskScheduler()
    task_scheduler.add_task(SendEmailTask())
    task_scheduler.add_task(CalcTask())
    task_scheduler.execute_tasks()
