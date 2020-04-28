import decimal
from decimal import Decimal


def consistency_check(raw_mean, raw_n, rounding_method=decimal.ROUND_HALF_UP):

    if isinstance(raw_mean, Decimal):
        mean = raw_mean
    else:
        mean = Decimal(raw_mean)

    if isinstance(raw_n, Decimal):
        n = raw_n
    else:
        n = Decimal(raw_n)

    if n <= Decimal('0'):
        raise ValueError("n must be greater than zero")

    if n % 1 != 0:
        raise ValueError("n must be a whole number")

    dp_of_mean = abs(mean.as_tuple().exponent)

    quotient = (mean*n)//1
    quantize_exp = f"1E-{dp_of_mean}"

    multiple_lower = (quotient-1)/n
    multiple_middle = quotient/n
    multiple_upper = (quotient+1)/n

    poss_match_lower = multiple_lower.quantize(Decimal(quantize_exp), rounding=rounding_method)
    poss_match_middle = multiple_middle.quantize(Decimal(quantize_exp), rounding=rounding_method)
    poss_match_upper = multiple_upper.quantize(Decimal(quantize_exp), rounding=rounding_method)

    if mean > poss_match_upper:
        raise Exception('Mean greater than expected high. Indicates code error.')

    if mean < poss_match_lower:
        raise Exception('Mean less than expected low. Indicates code error.')

    return mean in [poss_match_lower, poss_match_middle, poss_match_upper]
