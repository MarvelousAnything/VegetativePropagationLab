import math


def round_sig(num, digits):
    if math.isnan(num) or num == 0:
        return num
    return round(num, digits - (1 + int(math.log10(abs(num)))))
