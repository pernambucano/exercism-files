class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.on_earth_years = self.seconds / 31557600

    def on_earth(self):
        return self.calculate_equivalent_of_earth_years(1)

    def on_mercury(self):
        return self.calculate_equivalent_of_earth_years(0.2408467)

    def on_mars(self):
        return self.calculate_equivalent_of_earth_years(1.8808158)

    def on_venus(self):
        return self.calculate_equivalent_of_earth_years(0.61519726)

    def on_jupiter(self):
        return self.calculate_equivalent_of_earth_years(11.862615)

    def on_saturn(self):
        return self.calculate_equivalent_of_earth_years(29.447498)

    def on_uranus(self):
        return self.calculate_equivalent_of_earth_years(84.016846)

    def on_neptune(self):
        return self.calculate_equivalent_of_earth_years(164.79132)

    def calculate_equivalent_of_earth_years(self, earth_year_equivalent):
        return round(self.on_earth_years / earth_year_equivalent, 2)
