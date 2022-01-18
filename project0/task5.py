class Employee():

    def __init__(self, name, pin):
        self.name = name
        self.pin = pin

class Manager(Employee):

    def __init__(self, name, pin, salary, work_hour):
        super().__init__(name, pin)
        self.name = name
        self.pin = pin
        self.salary = salary
        self.work_hour = work_hour

    def payroll_calculation(self):
        return self.salary



class Secretary(Employee):

    def __init__(self, name, pin, salary, work_hour):
        super().__init__(name, pin)
        self.name = name
        self.pin = pin
        self.salary = salary
        self.work_hour = work_hour

    def payroll_calculation(self):
        return self.salary


class Seller(Employee):

    def __init__(self, name, pin, salary, work_hour, sell_count):
        super().__init__(name, pin)
        self.name = name
        self.pin = pin
        self.salary = salary
        self.work_hour = work_hour
        self.sell_count = sell_count

    def payroll_calculation(self):
        return self.salary + 50 * self.sell_count

class W_worker(Employee):

    def __init__(self, name, pin, work_hour):
        super().__init__(name, pin)
        self.name = name
        self.pin = pin
        self.work_hour = work_hour

    def payroll_calculation(self):
        return self.work_hour * 100


class R_secretary(Employee):

    def __init__(self, name, pin, work_hour):
        super().__init__(name, pin)
        self.name = name
        self.pin = pin
        self.work_hour = work_hour

    def payroll_calculation(self):
        return self.work_hour * 100

def all_payroll_calculation():
    print(f' {manager.name} c ID {manager.pin} начислено {manager.payroll_calculation()} сом.')
    print(f' {secretary.name} c ID {secretary.pin} начислено {secretary.payroll_calculation()} сом.')
    print(f' {seller.name} c ID {seller.pin} начислено {seller.payroll_calculation()} сом.')
    print(f' {w_worker1.name} c ID {w_worker1.pin} начислено {w_worker1.payroll_calculation()} сом.')
    print(f' {w_worker2.name} c ID {w_worker2.pin} начислено {w_worker2.payroll_calculation()} сом.')
    print(f' {r_secretary.name} c ID {r_secretary.pin} начислено {r_secretary.payroll_calculation()} сом.')
    print(f' Общий фонд заработной платы составил {manager.payroll_calculation()+secretary.payroll_calculation()+seller.payroll_calculation()+w_worker1.payroll_calculation()+w_worker2.payroll_calculation()+r_secretary.payroll_calculation()} сом')

def all_performance_evaluation():
    dic = [{'employee': 'Барсбек Канаткулов', 'work': 18*100/40 },
           {'employee': 'Алымкул Тилекбаев', 'work': 38*100/40},
           {'employee': 'Айпери Шалымбекова', 'work': 38*100/40},
           {'employee': 'Бакыт Рустамов', 'work': 25*100/40},
           {'employee': 'Алтынай Ширинбаева', 'work': 40*100/40},
           {'employee': 'Жанар Рыскулов','work': 33*100/40}]

    newlist = sorted(dic, key=lambda k: k['work'])
    for i in newlist:

        if i['work'] == 100:
            print(i['employee'] + f' продуктивный сотрудник')
        else:
            print(i['employee'] + f' очень продуктивный сотрудник')

    print(newlist[0]['employee'] + f' cамый не продуктивный сотрудник')
    print(newlist[-1]['employee'] + f' cамый продуктивный сотрудник')

manager = Manager('Барсбек Канаткулов', 1, 45000, 18)
secretary = Secretary('Алымкул Тилекбаев', 2, 20000, 38)
seller = Seller('Айпери Шалымбекова', 3, 20000, 38, 20)
w_worker1 = W_worker('Бакыт Рустамов', 4, 25)
w_worker2 = W_worker('Алтынай Ширинбаева', 5, 40)
r_secretary = R_secretary('Жанар Рыскулов', 6, 33)

all_payroll_calculation()
all_performance_evaluation()