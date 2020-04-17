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

        lower_multiple = (quotient-1)*fraction
        middle_multiple = quotient*fraction
        upper_multiple = (quotient+1)*fraction

        poss_match_lower = lower_multiple.quantize(Decimal(quantize_exp), rounding=rounding_method)
        poss_match_middle = middle_multiple.quantize(Decimal(quantize_exp), rounding=rounding_method)
        poss_match_upper = upper_multiple.quantize(Decimal(quantize_exp), rounding=rounding_method)

        return mean in [poss_match_lower, poss_match_middle, poss_match_upper]
