"""4) Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат."""

class Car:
    # атрибуты
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # методы
    def go(self):
        return f'Машина "{self.name}" поехала'

    def stop(self):
        return f'Машина "{self.name}" остановилась'

    def turn_right(self):
        return f'Машина "{self.name}" повернула направо'

    def turn_left(self):
        return f'Машина "{self.name}" повернула налево'

    def show_speed(self):
        return f'Текущая скорость машины "{self.name}" - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость машины "{self.name}" - {self.speed}')

        if self.speed > 60:
            return f'Скорость машины "{self.name}" превышает разрешенную в городском режиме'
        else:
            return f'Скорость машины "{self.name}" допустима'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость машины "{self.name}" - {self.speed}')

        if self.speed > 110:
            return f'Скорость машины "{self.name}" превышает разрешенную на магистрале'
        elif 110 >= self.speed > 90:
            return f'Скорость машины "{self.name}" превышает разрешенную на загородной трассе, но разрешена на магистрале'
        elif 90 >= self.speed > 60:
            return f'Скорость машины "{self.name}" превышает разрешенную в городском режиме, но разрешена на загородной трассе и магистрале'
        elif 60 >= self.speed:    
             return f'Скорость машины "{self.name}" разрешена в городском режиме, на загородной трассе и магистрале, если нет других ограничений'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Эта машина "{self.name}" - ДПС'
        else:
            return f'Эта машина "{self.name}" - ППС'

ferrari = SportCar(110, 'Красная', 'Ferrari', False)
toyota = TownCar(40, 'Серая', 'Toyota', False)
ford = WorkCar(90, 'Белая', 'Ford', True)
uaz = PoliceCar(110, 'Серебристая', 'UAZ', True)
print(toyota.turn_left())
print(f'Когда {ford.turn_right()}, потом {ferrari.stop()}')
print(f'{toyota.go()} едет со скоростью {toyota.show_speed()}.')
print(f'{toyota.name} имеет цвет {toyota.color}')
print(f'{ferrari.name} полицейская машина? {ferrari.is_police}')
print(f'{uaz.name} - полицейская машина {uaz.is_police}')
print(ferrari.show_speed())
print(toyota.show_speed())
print(uaz.police())
print(uaz.show_speed())