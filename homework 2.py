class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = 40

    def to_study(self):
        print("Time to study")
        self.progress += 0.5
        self.gladness -= 5
        self.money -= 4

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
        self.money -= 1

    def to_chill(self):
        print("Rest time")
        self.gladness += 2
        self.progress -= 0.1
        self.money -= 2

    def to_work(self):
        print("Time to work")
        self.money += 10
        self.gladness -= 3
        self.progress -= 0.10

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress >= 5:
            print("Passed externally…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        day = " Day " + str(day) + " of " + self.name + " life "
        print(f"{day:=^50}")
        if self.money < 3:
            self.to_work()
        else:
            if self.progress < 0:
                self.to_study()
            else:
                if self.gladness < 2:
                    self.to_sleep()
                else:
                    self.to_chill()
        self.end_of_day()
        self.is_alive()
nick = Student(name="Nick")

for days in range(365):
    if not nick.alive:
        break
    nick.live(days+1)