import inspect
from pprint import pprint


def introspection_info(obj: object) -> dict: # Возвращает информацию об получаемом объекте в виде словаря.
    type_  = type(obj)
    try:
        atributes = [atr for atr in vars(obj)]
        metods = [met for met in dir(obj) if met[0] != "_" and met not in atributes]
        module_info = inspect.getmodule(obj)
        info_ = dict(types=type_,atributes=atributes,metods=metods,module_info=module_info )
        if obj.__doc__:
            info_["doc"] = obj.__doc__
        return info_
    except TypeError:
        atr_met = [am for am in dir(obj) if am[0] != "_"]
        info_ = dict(type=type_, atributes_and_metods=atr_met, doc=obj.__doc__)

        return info_



class Car:
    """Пример класса взят у чата - GPT """
    def __init__(self, make, model, year):
        """Инициализация атрибутов автомобиля."""
        self.make = make   # Марка автомобиля
        self.model = model  # Модель автомобиля
        self.year = year    # Год выпуска
        self.engine_running = False  # Состояние двигателя (запущен/остановлен)

    def start_engine(self):
        """Метод для запуска двигателя."""
        if not self.engine_running:
            self.engine_running = True
            print(f"{self.make} {self.model} запущен.")
        else:
            print(f"{self.make} {self.model} уже работает.")

    def stop_engine(self):
        """Метод для остановки двигателя."""
        if self.engine_running:
            self.engine_running = False
            print(f"{self.make} {self.model} остановлен.")
        else:
            print(f"{self.make} {self.model} уже остановлен.")





if __name__ == "__main__":
    my_car = Car("Toyota", "Corolla", 2020)
    number = 10
    strings = "Строка"
    
    pprint(introspection_info(Car))
    print("__________________________________________________________________________________________________________")
    pprint(introspection_info(my_car))
    print("__________________________________________________________________________________________________________")
    pprint(introspection_info(number))
    print("__________________________________________________________________________________________________________")
    pprint(introspection_info(strings))
