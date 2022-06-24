class Stationery:
    title = 'Title'

    def draw(self):
        return f'Запуск отрисовки.'


class Pen(Stationery):
    def draw(self):
        return f'Рисуем ручкой.'


class Pencil(Stationery):
    def draw(self):
        return f'Рисуем карандашом.'


class Handle(Stationery):
    def draw(self):
        return f'Рисуем маркером.'

