"""
适配器模式 主要用来解决接口不兼容的问题
示例为集成实现不同类型的音乐格式播放

role:
目标接口
适配器类
适配者类
客户端
"""
class TargetInterface:
    def play(self):
        pass

class Adapter(TargetInterface):
    def __init__(self, type):
        if type == 'mp3':
            self.adaptee = MP3Adaptee()
        elif type == 'wma':
            self.adaptee = WMAAdaptee()
    
    def play(self):
        self.adaptee.play_music()

class Adaptee:
    def play_music(self):
        pass

class MP3Adaptee(Adaptee):
    def play_music(self):
        print("播放MP3音乐")

class WMAAdaptee(Adaptee):
    def play_music(self):
        print("播放WMA音乐")

if __name__ == "__main__":
    # 需要更换播放类型 只需要修改传参即可 保证后续调用逻辑保持一致
    mp3_adapter = Adapter('mp3')
    wma_adapter = Adapter('wma')

    mp3_adapter.play()
    wma_adapter.play()
