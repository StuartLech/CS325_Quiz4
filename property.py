class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self._age = age

    @property
    def age(self) -> int:
        """The getter method for the age property."""
        return self._age

    @age.setter
    def age(self, value: int):
        """The setter method for the age property, with validation."""
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


if __name__ == "__main__":
    user = User("John Doe", 30)
    print(f"{user.name} is {user.age} years old.")


    user.age = 25
    print(f"{user.name} is now {user.age} years old.")

   
    try:
        user.age = -5
    except ValueError as e:
        print(e)
