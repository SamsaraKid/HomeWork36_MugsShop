import random


class Mug:
    def __init__(self, color, text, type):
        self.color = color
        self.text = text
        self.type = type

    # вывод кружки для таблицы со столбцами шириной 15 символов
    def showmug(self):
        print(self.color.ljust(15), self.text.ljust(15), self.type.ljust(15), sep='', end='')

    # делаем возможным сравнение разных объектов кружки с одинаковыми атрибутами
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
        self.customers = []

    # ищем кружку в каталоге. можно искать как по атрибутам, так и целый объект кружки.
    # возвращает артикул или -1 если не нашлась
    def findincat(self, color, text='', type=''):
        try:
            if isinstance(color, Mug):
                return self.catalog.index(color)
            else:
                return self.catalog.index(Mug(color, text, type))
        except:
            return -1

    # ищем кружки на складе по артикулу. возвращает количество найденных
    def findinstock(self, art):
        if self.catalog[art] in self.stock:
            return len(list(filter(lambda x: x == self.catalog[art], self.stock)))
        return 0

    # добавляем кружку в каталог. возвращает артикул добавленной кружки.
    # если уже есть, выводится сообщение и артикул
    # также генерируется цена кружки
    def add(self, color, text, type):
        art = self.findincat(color, text, type)
        if art >= 0:
            print('Такая кружка уже есть в каталоге. Артикул', art)
        else:
            self.catalog.append(Mug(color, text, type))
            self.pricelist.append(random.randint(2, 10))
            art = len(self.catalog) - 1
        return art

    # выводим каталог в виде таблицы
    def showcat(self):
        print('Вот что есть в каталоге:')
        print('------------------------------------------------------')
        print('Арт. Цвет           Текст          Тип            Цена')
        print('------------------------------------------------------')
        for i in range(len(self.catalog)):
            print(str(i).ljust(5), end='')
            self.catalog[i].showmug()
            print(self.pricelist[i])
        print('------------------------------------------------------')

    # выводим склад в виде таблицы
    def showstock(self):
        print('Вот что есть на складе:')
        print('-------------------------------------------')
        print('Арт. Цвет           Текст          Тип')
        print('-------------------------------------------')
        for m in self.stock:
            print(str(self.findincat(m)).ljust(5), end='')
            m.showmug()
            print()
        print('-------------------------------------------')

    # производство кружек по артикулу и количеству с помещением их на склад.
    # производство стоит денег, так что бюджет уменьшается
    def make(self, art, num):
        self.stock.extend([Mug(self.catalog[art].color, self.catalog[art].text, self.catalog[art].type) for i in range(num)])
        self.budget -= self.cost * num

    # продажа кружек, имеющихся в каталоге
    # если на складе не хватает, изготовляем дополнительно
    # возвращает объекты кружек со склада
    def sell(self, art, num):
        mugs = []
        n = self.findinstock(art)
        if n < num:
            self.make(art, num - n)
        for i in range(num):
            ind = self.stock.index(self.catalog[art])
            mugs.append(self.stock.pop(ind))
        self.budget += self.pricelist[art] * num
        return mugs

    # заказ кружек по атрибутам. сперва добавляется в каталог,
    # затем изготавливается нужное количество и помещается на склад
    # возвращается артикул изготовленных кружек
    def order(self, color, text, type, num):
        art = self.add(color, text, type)
        if self.findinstock(art) < num:
            self.make(art, num - self.findinstock(art))
        return art

    # добавление нового клиента
    def hello(self):
        print('Добро пожаловать в магазин кружек')
        name = input('Представьтесь, пожалуйста:\n')
        money = int(input('Внесите сумму на ваш счёт:\n'))
        self.customers.append(Customer(name, money))

    # показать перечень клиентов
    def showcustomers(self):
        print('Наши клиенты:')
        print('------------------------------------------------')
        print('№  Имя            Кол-во кружек  Баланс         ')
        print('------------------------------------------------')
        for i in range(len(self.customers)):
            print(str(i).ljust(3), end='')
            self.customers[i].showmydata()
            print()
        print('------------------------------------------------')

    # диалог с клиентом
    def workwithcustomer(self, cnum):
        print('На вашем счету', self.customers[cnum].money)
        ans = int(input('Выберите действие:\n'
                        '\t1 - Посмотреть каталог\n'
                        '\t2 - Посмотреть свои кружки\n'
                        '\t3 - Заказать из каталога\n'
                        '\t4 - Заказать не из каталога\n'
                        '\t5 - Пополнить счёт\n'
                        '\t0 - Уйти\n'))
        if ans == 1:
            market2.showcat()
        elif ans == 2:
            self.customers[cnum].showmymugs()
        elif ans == 3:
            art = int(input('Введите артикул кружки из каталога:\n'))
            num = int(input('Сколько кружек хотите?\n'))
            self.customers[cnum].buy(market2, art, num)
            print('Поздравляем с покупкой!')
            self.customers[cnum].showmymugs()
        elif ans == 4:
            color = int(input('Выберите цвет кружки:\n'
                              '\t1 - белый\n'
                              '\t2 - чёрный\n'
                              '\t3 - красный\n'
                              '\t4 - зелёный\n'
                              '\t5 - синий\n'))
            color = ['белый', 'чёрный', 'красный', 'зелёный', 'синий'][color - 1]
            text = input('Напишите текст для кружки:\n')
            type = int(input('Выберите тип надписи:\n'
                             '\t1 - текст\n'
                             '\t2 - изображение\n'))
            type = ['txt', 'img'][type - 1]
            num = int(input('Сколько кружек хотите?\n'))
            self.customers[cnum].order(market2, color, text, type, num)
            print('Поздравляем с покупкой!')
            self.customers[cnum].showmymugs()
        elif ans == 5:
            mon = int(input('Введите сумму пополнения:\n'))
            self.customers[cnum].money += mon
            print('Счёт пополнен.')
        else:
            print('Всего доброго. Ждём вас снова')
        if ans in [1, 2, 3, 4, 5]:
            self.workwithcustomer(cnum)


class Customer:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.mugs = []

    # покупка кружек из каталога
    def buy(self, market, art, num):
        if market.pricelist[art] * num > self.money:
            print('У вас недостаточно средств. Пополните счёт или измените заказ')
            return -1
        else:
            self.mugs.extend(market.sell(art, num))
            self.money -= market.pricelist[art] * num
            return num

    # заказ и покупка кружек не из каталога
    def order(self, market, color, text, type, num):
        self.buy(market, market.order(color, text, type, num), num)

    # вывод в виде таблицы имеющихся у покупателя кружек
    def showmymugs(self):
        print('Вот что есть у вас:')
        print('--------------------------------------')
        print('Цвет           Текст          Тип')
        print('--------------------------------------')
        for m in self.mugs:
            m.showmug()
            print()
        print('--------------------------------------')

    def showmydata(self):
        print(self.name.ljust(15), str(len(self.mugs)).ljust(15), str(self.money).ljust(15), sep='', end='')


market2 = Market(100)
market2.add('красный', 'БОСС', 'txt')
market2.add('чёрный', 'С ДР', 'txt')
market2.add('белый', 'Никита', 'img')
market2.hello()
market2.workwithcustomer(0)



