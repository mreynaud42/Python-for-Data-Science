from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    ""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        return self.eyes

    def set_eyes(self, value):
        self.eyes = value

    def get_hairs(self):
        return self.hairs

    def set_hairs(self, value):
        self.hairs = value