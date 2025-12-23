"""
桥接模式:将抽象部分与实现部分分离 使它们都可以独立的变化

实现案例:
    消息发送器 可以发送不同的消息类型 比如短信 邮件 等
    同时消息类型也可以独立的变化 比如通知 警告 等
    每个消息类型都有不同的发送实现 但是客户端调用的时候只需要调用发送消息的方法即可
    这样就可以将消息发送的实现与调用分离 使得它们都可以独立的变化
"""
class Message():
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
    def send(self):
        pass

class NoticeMessage(Message):
    def send(self):
        print("发送通知消息")
        self.sender.send(self.content)

class WarningMessage(Message):
    def send(self):
        print("发送警告消息")
        self.sender.send(self.content)

class Sender():
    def send(self, content):
        pass

class EmailSender(Sender):
    def send(self, content):
        print(f"发送邮件: {content}")

class SmsSender(Sender):
    def send(self, content):
        print(f"发送短信: {content}")

if __name__ == "__main__":
    email_sender = EmailSender()
    sms_sender = SmsSender()
    notice_message = NoticeMessage(email_sender, "系统维护通知")
    notice_message.send()
    warning_message = WarningMessage(sms_sender, "CPU告警")
    warning_message.send()
