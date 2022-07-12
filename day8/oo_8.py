# Python 物件導向-多重繼承
class Employee:  # 員工
    def __init__(self, title):
        self.title = title  # 職銜
    def __str__(self):
        return "Employee's title: %s " % self.title

class Computer:  # 電腦
    def __init__(self, cpu_speed):
        self.cpu_speed = cpu_speed
    def __str__(self):
        return "Computer's cpu speed: %.1f Ghz " % self.cpu_speed

class Robot(Employee, Computer):  # 機器人繼承員工,電腦
    def __init__(self, title, cpu_speed, name):
        Employee.__init__(self, title)
        Computer.__init__(self, cpu_speed)
        self.name = name
    def __str__(self):
        return Employee.__str__(self) + Computer.__str__(self) + 'name: %s' % self.name

if __name__ == '__main__':
    robot = Robot('保全', 3.1, '門禁機器人')
    print(robot)
