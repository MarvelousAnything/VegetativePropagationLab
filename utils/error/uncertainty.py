import numpy as np

from utils.math import round_sig


class Uncertainty:
    def __init__(self, num, error=0.0):
        if isinstance(num, Uncertainty):
            self.num = num.num
            self.error = round_sig(num.error, 1)
        else:
            self.num = num
            self.error = round_sig(error, 1)

    @classmethod
    def from_average(cls, values):
        return cls(np.mean(values), round_sig((max(values) - min(values)) / 2, 1))

    @property
    def absolute(self):
        return round_sig(self.error, 1)

    @absolute.setter
    def absolute(self, value):
        self.error = value

    @property
    def fractional(self):
        return self.absolute / self.num

    @fractional.setter
    def fractional(self, other):
        self.error = other / self.num

    @property
    def percent(self):
        return self.fractional * 100

    @percent.setter
    def percent(self, other):
        self.fractional = other / 100

    def __add__(self, other):
        other = Uncertainty(other)
        self.num += other.num
        self.absolute += other.absolute

    def __sub__(self, other):
        other = Uncertainty(other)
        self.num -= other.num
        self.absolute += other.absolute

    def __mul__(self, other):
        other = Uncertainty(other)
        self.num *= other.num
        self.fractional += other.fractional

    def __div__(self, other):
        other = Uncertainty(other)
        self.num /= other.num
        self.fractional += other.fractional

    def __pow__(self, power, modulo=None):
        self.absolute = (self.num ** power) * abs(power * self.fractional)
        self.num = self.num ** power

    def __str__(self):
        return f"{self.num} ± {self.absolute}"
