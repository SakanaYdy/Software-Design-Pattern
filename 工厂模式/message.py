"""
工厂模式 示例说明
实现一个消息通知的工厂 适配不同的消息发送方式
"""
from typing import Protocol

class Message(Protocol):
    def send(self, message: str):
        pass

class EmailMessage(Message):
    def send(self, message: str):
        print(f"正在发送邮件: {message}")

class SMSMessage(Message):
    def send(self, message: str):
        print(f"正在发送短信: {message}")


# 实现工厂类
class MessageFactory(Protocol):
    def getSender():
        pass

class EmailMessageFactory(MessageFactory):
    def getSender(self):
        return EmailMessage()

class SMSMessageFactory(MessageFactory):
    def getSender(self):
        return SMSMessage()
