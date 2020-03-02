class Allergies:
    def __init__(self, score):
        self.score = score
        self.allergies_dict = {
            "eggs": 1,
            "peanuts": 2,
            "shellfish": 4,
            "strawberries": 8,
            "tomatoes": 16,
            "chocolate": 32,
            "pollen": 64,
            "cats": 128,
        }

    def allergic_to(self, item):
        if self.allergies_dict[item] & self.score:
            return True
        else:
            return False

    @property
    def lst(self):
        return [x for x in self.allergies_dict.keys() if self.allergic_to(x)]
