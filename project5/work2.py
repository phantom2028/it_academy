class Lemonade:

    def __init__(self, additives):
        if isinstance(additives, str):
            self.additives = additives
        else:
            self.additives = None

    def drink_info(self):
        if self.additives:
            return f'Лимонад с {self.additives}'
        else:
            return 'Обычная газировка'

lemonade = Lemonade('клубникой')
print(lemonade.drink_info())
