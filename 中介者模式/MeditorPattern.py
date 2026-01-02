"""
中介者模式 （Mediator Pattern）：定义一个中介对象来封装一系列对象之间的交互，使原有对象之间的耦合松散，且可以独立地改变它们之间的交互。

role:
    1. 中介者接口 
    2. 具体中介者类
    3. 同事类（Colleague）：定义了所有的同事类的接口，它的子类可以是具体的同事类。

"""
# 以多人聊天室转发为例

class ChatRoomMediator:
    def sendMessage(self, message, colleague):
        pass
    def registerColleague(self, colleague):
        pass

class User:
    def __init__(self, name,mediator):
        self.name = name
        self.chat_room_mediator = mediator

    def receive(self, message):
        pass
    def send(self, message):
        pass

class ChatUser(User):
    def __init__(self, name, mediator):
        super().__init__(name, mediator)

    def send(self, message):
        self.chat_room_mediator.sendMessage(message, self)
    
    def receive(self, message):
        print(f"{self.name} 收到消息: {message}")

# 定义实现中介者类
class ChatRoom(ChatRoomMediator):
    def __init__(self):
        self.colleagues = []
    def sendMessage(self, message, colleague):
        for c in self.colleagues:
            if c != colleague:
                c.receive(message)
    def registerColleague(self, colleague):
        self.colleagues.append(colleague)


if __name__ == "__main__":
    chat_room = ChatRoom()
    user1 = ChatUser("用户1", chat_room)
    user2 = ChatUser("用户2", chat_room)
    user3 = ChatUser("用户3", chat_room)
    chat_room.registerColleague(user1)
    chat_room.registerColleague(user2)
    chat_room.registerColleague(user3)
    user1.send("你好")
    # user2.send("你好")
    # user3.send("你好")