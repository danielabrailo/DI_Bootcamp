# Exercise 1
"""Program that prints the results of the following python built-in functions: abs(), int() and input()"""
print(dir(abs))
print(dir(int))
print(dir(input))
print(__doc__)


# Exercise 2
class Currency:
    def __init__(self, currency: str, value: int):
        self.currency = currency
        self.value = value

    def __str__(self):
        return f"{self.value} {self.currency}"

    def __int__(self):
        return self.value

    def __repr__(self):
        return f"{self.value} {self.currency}"

    def __add__(self, other):
        if isinstance(other, int):
            return Currency(self.currency, (self.value + other))
        elif isinstance(other, Currency):
            if other.currency != self.currency:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
            else:
                return Currency(self.currency, (self.value + other.value))


c1 = Currency('dollars', 5)
c2 = Currency('dollars', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))

print(c1 + 5)
print(c1 + c2)
print(c1)

c1 += 5
print(c1)

c1 += c2
print(c1)

print(c1 + c3)