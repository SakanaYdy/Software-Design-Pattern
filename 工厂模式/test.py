from message import EmailMessageFactory, SMSMessageFactory


if __name__ == "__main__":
    sender = EmailMessageFactory().getSender()
    sender.send("你好，这是一封邮件")
    # 如果需要切换 只需要修改sender即可 代码维护性较好
    sender = SMSMessageFactory().getSender()
    sender.send("你好，这是一条短信")

