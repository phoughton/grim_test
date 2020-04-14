from decimal import *


def consistency_check(raw_mean, raw_n, rounding):
    if rounding is None:
        mean = Decimal(raw_mean)
        n = Decimal(raw_n)

        fraction = 1/n

        remainder = mean % fraction

        print(raw_mean, raw_n, remainder)

        return remainder == 0

    else:
        raise Exception("Unsupported, Rounding is not yet supported.")

