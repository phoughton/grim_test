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

        quotient = mean//fraction
        quantize_exp = f"1E-{dp_of_mean}"

        base_multiple = quotient*fraction
        next_multiple = (quotient+1)*fraction

        poss_match_1 = base_multiple.quantize(Decimal(quantize_exp), rounding=rounding_method)
        poss_match_2 = next_multiple.quantize(Decimal(quantize_exp), rounding=rounding_method)

        return mean in [poss_match_1, poss_match_2]
