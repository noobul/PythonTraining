class City:
    def __init__(self, country, city, population = 0):
        self.country = country
        self.city = city
        self.population = population

    def city_formater(self):
        co = self.country.title()
        ci = self.city.title()
        pop = self.population
        if pop > 0:
            result = f"{co}, {ci} has a population of {pop}"
        else:
            result = f"{co}, {ci}"
        return result