import string
import random


class Robot:
    def __init__(self):
        self._name = self.create_random_string()

    @property
    def name(self):
        return self._name

    def reset(self):
        random.seed(random.random())
        self.__init__()

    def create_random_string(self):
        return "".join(
            [random.choice(string.ascii_uppercase) for _ in range(0, 2)]
        ) + "".join([random.choice(string.digits) for _ in range(0, 3)])


