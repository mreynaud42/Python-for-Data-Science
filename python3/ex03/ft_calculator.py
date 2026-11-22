class calculator:
    ""
    #your code here
    def __init__(self, vector: list):
        self.vector = vector

    def __add__(self, object) -> None:
        ""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        ""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        ""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        ""
        if object == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self.vector = [x / object for x in self.vector]
        print(self.vector)
