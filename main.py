#Python은 public / private를 지원하지 않고, type도 지정해주지 않는다.
#class 안에 있는 모든 메서드는 self를 가장 첫 번째 파라미터로 한다.
class Player:
  def __init__(self, name, xp):
    self.name = name
    self.xp = xp
  def say_hello(self):
    print(f"hello my name is {self.name}")

nico = Player('nico', 1000)
nico.say_hello()