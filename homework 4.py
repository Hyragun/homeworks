print("-----------Best Computer-----------")
class Computer:
    def __init__(self):
        self.memory = "32GB"
        self.processor = "Intel ryzen 9 9950x3d"
        self.graphics_card = "Nvidia RTX 5090"
        self.storage = "1TB"
        self.power_supply = "2000W"


class Display:
    def __init__(self):
        self.resolution = "4k"
        self.size = "32 inch"
        self.refresh_rate = "240Hz"

        super().__init__()

class SmartPhone(Display, Computer):
    def __init__(self):
        super().__init__()

    def print_info(self):
        print("-----Display-----")
        print(self.resolution)
        print(self.size)
        print(self.refresh_rate)
        print("-----Computer-----")
        print(self.memory)
        print(self.processor)
        print(self.graphics_card)
        print(self.storage)
        print(self.power_supply)
        print("------------------")
phone = SmartPhone()
phone.print_info()