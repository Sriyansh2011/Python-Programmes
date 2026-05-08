class Robot:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce(self):
        print("Hello! My name is", self.name)
        print("My model is", self.model)
        print("My purpose is", self.purpose)

    def skill(self):
        print(self.name, "can solve problems and help humans!")

robot1 = Robot("Roboti", "RX-2026", "Helping students learn coding")

robot1.introduce()
print()
robot1.skill()