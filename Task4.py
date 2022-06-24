class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return f'{self.name} is on the move.'

    def stop(self):
        return f'{self.name} stopped.'

    def turn(self, direction):
        return f'{self.name} has turned {direction}.'

    def show_speed(self):
        return f'{self.name} current speed: {self.speed}km/h'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} exceeded the speed limit.'
        else:
            return f'current speed: {self.speed}km/h.'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'{self.name} exceeded the speed limit.'
        else:
            return f'current speed: {self.speed}km/h.'


class SportCar(Car):
    def show_speed(self):
        return f'{self.name} has no speed limit.'


class PoliceCar(Car):
    def show_speed(self):
        return f'{self.name} has no speed limit.'
