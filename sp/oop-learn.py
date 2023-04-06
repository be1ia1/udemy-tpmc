class User:
    def __init__(self, name, birthyear) -> None:
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        pass

    def age(self, current_year):
        return current_year - self.birthyear

user = User('John', 1982)
print(user.age(2023))