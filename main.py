class Dog:
  def __init__(self, name):
    self.name = name

  #클래스가 문자열로 보이는 방식을 바꿀 수 있다.
  def __str__(self):
    print(super().__str__())
    return f"Dog: {self.name}"


jia = Dog("jia")
print(jia)
paul = Dog("paul")
print(paul)