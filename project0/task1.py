class Country:
    def __init__(self, name, population, area):
        self.__name = name
        self.__population = population
        self.__area = area

    @property
    def name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    @property
    def population(self):
        return self.__population

    def set_population(self, population):
        if isinstance(population, int):
            self.__population = population

    @property
    def area(self):
        return self.__area

    def set_territory(self, area):
        if isinstance(area, int):
            self.__area = area

    def display_info(self):
        print(f'Name: {self.__name}\n'
              f'Population: {self.__population}\n'
              f'Territory: {self.__area}\n')


kyrgyzstan= Country('Кыргызстан', 6523529, 199951)
print(kyrgyzstan.display_info())
