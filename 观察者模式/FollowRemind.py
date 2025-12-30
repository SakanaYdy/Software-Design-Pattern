"""
观察者模式 当一个对象状态发生变化的时候,自动通知所有依赖于它的对象,并自动更新它们

role:
    1. 抽象主题(Subject):定义了添加、删除、通知观察者的方法
    2. 具体主题(ConcreteSubject):实现了抽象主题的方法,并在状态发生变化时通知所有观察者
    3. 抽象观察者(Observer):定义了更新方法,用于接收主题的通知
    4. 具体观察者(ConcreteObserver):实现了抽象观察者的方法,用于更新自身的状态

example:
    粉丝关注之后推送更新
"""

# 观察者接口
class Follower():
    def update(self, username,postContent):
        pass

# 被观察者接口
class User():
    def addFollower(self,follower):
        pass
    def removeFollower(self,follower):
        pass
    def notifyFollowers(self,postContent):
        pass

class ConcreteFollower(Follower):

    def __init__(self,name):
        self.name = name

    def update(self, username,postContent):
        print(f"{self.name} received a new post from {username}: {postContent}")


class ConcreteUser(User):
    def __init__(self,username):
        self.username = username
        self.followers = []
    
    def addFollower(self,follower):
        self.followers.append(follower)
    
    def removeFollower(self,follower):
        self.followers.remove(follower)
    
    def notifyFollowers(self,postContent):
        for follower in self.followers:
            follower.update(self.username,postContent)
    
    def post(self,postContent):
        print(f"{self.username} posted: {postContent}")
        self.notifyFollowers(postContent)

if __name__ == "__main__":
    user1 = ConcreteUser("user1")
    user2 = ConcreteUser("user2")

    follower1 = ConcreteFollower("follower1")
    follower2 = ConcreteFollower("follower2")

    user1.addFollower(follower1)
    user1.addFollower(follower2)
    user2.addFollower(follower2)

    user1.post("Hello, followers!")
    user2.post("Hi, user1!")