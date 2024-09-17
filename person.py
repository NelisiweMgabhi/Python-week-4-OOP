class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I identify as {self.gender}.")


# Creating an instance of Person class
if __name__ == "__main__":
    person_instance = Person("Nelly Gama", 30, "female")
    person_instance.introduce()
