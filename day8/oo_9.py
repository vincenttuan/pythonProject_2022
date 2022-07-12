# Python 物件導向-繼承
# 方法覆寫
class Bird:
    def __init__(self, name):
        self.name = name

    def move(self):
        print('%s會飛' % self.name)


class Penguin(Bird):
    def __init__(self, name):
        super().__init__(name)

    def move(self):  # 覆寫了 Bird 的 move() 方法
        print('%s不會飛但是會游泳' % self.name)


if __name__ == '__main__':
    bird = Bird('白文鳥')
    bird.move()

    penguin = Penguin('國王企鵝')
    penguin.move()
