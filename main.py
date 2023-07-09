class Mug:
    def __init__(self, color, text, type):
        self.color = color
        self.text = text
        self.type = type

    def showmag(self):
        print(self.color.ljust(15), self.text.ljust(15), self.type.ljust(15), sep='', end='')


class Market:
    def __init__(self):
        self.catalog = []
        self.stock = []

    def findincat(self, color, text, type):
        mug = {'color': color, 'text': text, 'type': type}
        try:
            return list(map(lambda x: x.__dict__, self.catalog)).index(mug)
        except:
            return -1

    def findinstock(self, art):
        try:
            return list(map(lambda x: x['art'], self.stock)).index(art - 1)
        except:
            return -1

    def add(self, color, text, type):
        if self.findincat(color, text, type) >= 0:
            print('Такая кружка уже есть в каталоге')
        else:
            self.catalog.append(Mug(color, text, type))

    def showcat(self):
        print('Вот что есть в каталоге:')
        print('------------------------------------')
        print('№  Цвет           Текст          Тип')
        print('------------------------------------')
        for i in range(len(self.catalog)):
            print(str(i + 1).ljust(3), end='')
            self.catalog[i].showmag()
            print()
        print('------------------------------------')

    def showstock(self):
        print('Вот что есть на складе:')
        print('----------------------------------------------------------')
        print('№  Цвет           Текст          Тип            Количество')
        print('----------------------------------------------------------')
        for m in self.stock:
            print(str(m['art'] + 1).ljust(3), end='')
            m['mug'].showmag()
            print(str(m['num']).ljust(15))
        print('----------------------------------------------------------')

    def make(self, art, num):
        ind = self.findinstock(art)
        if ind >= 0:
            self.stock[ind]['num'] += num
        else:
            self.stock.append({'art': art - 1, 'mug': self.catalog[art - 1], 'num': num})
            

market = Market()
market.add('красный', 'БОСС', 'txt')
market.add('чёрный', 'С ДР', 'txt')
market.add('белый', 'Никита', 'img')
market.showcat()
market.make(1, 2)
market.make(3, 4)
market.showstock()
market.make(1, 10)
market.showstock()

