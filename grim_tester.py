import decimal
from decimal import Decimal


def consistency_check(raw_mean, raw_n, rounding_method=decimal.ROUND_HALF_UP):

    mean = Decimal(raw_mean)
    n = Decimal(raw_n)
    fraction = 1 / n

    if rounding_method is None:

        remainder = mean % fraction
        return remainder == 0

    else:

        dp_of_mean = abs(mean.as_tuple().exponent)

        num_fractions_in_mean = mean//fraction
        quantize_exp = f"1E-{dp_of_mean}"

        possible_match = (num_fractions_in_mean*fraction).quantize(Decimal(quantize_exp), rounding=rounding_method)

        return possible_match == mean
