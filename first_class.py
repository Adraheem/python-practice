class FirstClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__height = 0

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    @staticmethod
    def use_static():
        return "Hello"
