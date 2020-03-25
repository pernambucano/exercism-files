import random
import math


class Cipher:
    def __init__(self, key=None):
        self.lower_letters = "abcdefghijklmnopqrstuvwxyz"
        if key != None:
            self.key = key
        else:
            self.key = "".join([random.choice(self.lower_letters) for i in range(100)])

    def encode(self, text):
        if len(text) > len(self.key):
            self.key = self.key * math.ceil(len(text) / len(self.key))
        number_steps = [ord(letter) - 97 for letter in self.key]
        encoded = [
            self.lower_letters[(self.lower_letters.index(x) + y) % 26]
            for (x, y) in zip(text, number_steps)
        ]
        return "".join(encoded)

    def decode(self, text):
        if len(text) > len(self.key):
            self.key = self.key * math.ceil(len(text) / len(self.key))
        number_steps = [ord(letter) - 97 for letter in self.key]
        decoded = [
            self.lower_letters[((self.lower_letters.index(x) - y) + 26) % 26]
            for (x, y) in zip(text, number_steps)
        ]
        return "".join(decoded)
