import random


class Mug:
    def __init__(self, color, text, type):
        self.color = color
        self.text = text
        self.type = type

    def showmug(self):
        print(self.color.ljust(15), self.text.ljust(15), self.type.ljust(15), sep='', end='')

    def __eq__(self, other):
        if isinstance(other, Mug):
            return self.color == other.color and \
                   self.text == other.text and \
                   self.type == other.type
        return NotImplemented


class Market:
    def __init__(self, budget):
        self.catalog = []
        self.stock = []
        self.pricelist = []
        self.budget = budget
        self.cost = 1

    def findincat(self, color, text='', type=''):
        try:
            if isinstance(color, Mug):
                return self.catalog.index(color) + 1
            else:
                return self.catalog.index(Mug(color, text, type)) + 1
        except:
            return -1

    def findinstock(self, art):
        if self.catalog[art - 1] in self.stock:
            return len(list(filter(lambda x: x == self.catalog[art - 1], self.stock)))
        return 0

    def add(self, color, text, type):
        art = self.findincat(color, text, type)
        if art >= 0:
            print('Такая кружка уже есть в каталоге. Артикул', art)
        else:
            self.catalog.append(Mug(color, text, type))
            self.pricelist.append(random.randint(1, 10))
            art = len(self.catalog)
        return art

    def showcat(self):
        print('Вот что есть в каталоге:')
        print('------------------------------------------------------')
        print('Арт. Цвет           Текст          Тип            Цена')
        print('------------------------------------------------------')
        for i in range(len(self.catalog)):
            print(str(i + 1).ljust(5), end='')
            self.catalog[i].showmug()
            print(self.pricelist[i])
        print('------------------------------------------------------')

    def showstock(self):
        print('Вот что есть на складе:')
        print('--------------------------------------')
        print('Арт. Цвет           Текст          Тип')
        print('--------------------------------------')
        for m in self.stock:
            print(str(self.findincat(m) + 1).ljust(5), end='')
            m.showmug()
            print()
        print('---------------------------------------')

    def make(self, art, num):
        self.stock.extend([Mug(self.catalog[art - 1].color, self.catalog[art - 1].text, self.catalog[art - 1].type) for i in range(num)])
        self.budget -= self.cost * num

    def sell(self, art, num):
        mugs = []
        n = self.findinstock(art)
        if n < num:
            self.make(art, num - n)
        for i in range(num):
            ind = self.stock.index(self.catalog[art - 1])
            mugs.append(self.stock.pop(ind))
        self.budget += self.pricelist[art - 1] * num
        return mugs

    def order(self, color, text, type, num):
        art = self.add(color, text, type)
        if self.findinstock(art) < num:
            self.make(art, num - self.findinstock(art))
        return art


class Customer:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.mugs = []

    def buy(self, market, art, num):
        if market.pricelist[art - 1] * num > self.money:
            return -1
        else:
            self.mugs.extend(market.sell(art, num))
            self.money -= market.pricelist[art - 1] * num
            return num

    def order(self, market, color, text, type, num):
        self.buy(market.order(color, text, type, num))

    def showmymugs(self):
        print('Вот что есть у меня:')
        print('---------------------------------')
        print('Цвет           Текст          Тип')
        print('---------------------------------')
        for m in self.mugs:
            m.showmug()
            print()
        print('---------------------------------')
            

market1 = Market(100)
market1.add('красный', 'БОСС', 'txt')
market1.add('чёрный', 'С ДР', 'txt')
market1.add('белый', 'Никита', 'img')
market1.showcat()
market1.make(1, 2)
market1.make(3, 4)
market1.make(2, 3)
market1.showstock()

customer1 = Customer('name', 100)
customer1.buy(market1, 3, 6)
market1.showcat()
market1.showstock()
customer1.showmymugs()

print('market1.budget', market1.budget, 'customer1.money', customer1.money)
market1.order('зелёный', 'Никита', 'img', 5)
market1.showcat()
market1.showstock()

market2 = Market(100)
print('Добро пожаловать в магазин кружек')
name = input('Представьтесь, пожалуйста:\n')
money = input('Внесите сумму на ваш счёт:\n')
customer2 = Customer(name, money)
while True:
    ans = int(input('Выберите действие:\n'
                    '1 - Посмотреть каталог\n'
                    '2 - Заказать из каталога\n'
                    '3 - Заказать не из каталога\n'
                    '4 - Уйти'))
    match
    break

