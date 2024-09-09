class Human:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, {self.name}, you are {self.age} years old.')

    def __str__(self):
        return self.name


def main():
    names = ['Alice', 'Bob', 'Charlie']
    humans = [Human(name) for name in names]
    for human in humans:
        if human.name == 'Alice':
            human.age = 20
        human.say_hello()


if __name__ == '__main__':
    main()
