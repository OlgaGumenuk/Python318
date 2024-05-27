class Clock:
    __DAY = 86400  # Число секунд в дне

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правыи операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правыи операнд должен быть типом Clock")
        return Clock(self.sec * other.sec)

    def __truediv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правыи операнд должен быть типом Clock")
        return Clock(self.sec / other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правыи операнд должен быть типом Clock")
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правыи операнд должен быть типом Clock")
        return Clock(self.sec % other.sec)

    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правыи операнд должен быть типом Clock")
        return self.sec < other.sec

    def __le__(self, other):
        return not self.__lt__(other)

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правыи операнд должен быть типом Clock")
        return self.sec > other.sec

    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правыи операнд должен быть типом Clock")
        return self.sec >= other.sec


c1 = Clock(700)
c2 = Clock(68400)
c3 = c1 + c2
print(c3.get_format_time())
c_mul = c1 * c2
print(c_mul.get_format_time())
# c11 = c2 / c1   # С ЭТИМ МЕТОДОМ НЕ РАБОТАЕТ
# print(c11.get_format_time())   #   С ЭТИМ МЕТОДОМ НЕ РАБОТАЕТ
c12 = c3 // c1
print(c12.get_format_time())
c13 = c2 % c1
print(c13.get_format_time())

# if c2 < c2:
#     print("Время разное")
# else:
#     print("Время равно")
#
if c2 <= c2:
    print("Время разное")
else:
    print("Время равно")  # не попадает в else

if c1 > c2:
    print("Время разное")  # что-то не придумала как должно правильно считать
else:
    print("Время равно")  # что-то не придумала как должно правильно считать

if c1 >= c1:
    print("Время разное")  # что-то не придумала как должно правильно считать
else:
    print("Время равно")  # что-то не придумала как должно правильно считать

