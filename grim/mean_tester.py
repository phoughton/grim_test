import decimal
from decimal import Decimal
from time import gmtime, strftime

rounding_types = ["ROUND_CEILING",
                  "ROUND_DOWN",
                  "ROUND_FLOOR",
                  "ROUND_HALF_DOWN",
                  "ROUND_HALF_EVEN",
                  "ROUND_HALF_UP",
                  "ROUND_UP",
                  "ROUND_05UP"]

def log(log_debug, msg):
    if log_debug:
        print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) + " : " + str(msg))

def summary_consistency_check(raw_mean, raw_n, log_status=False):
    """
    Returns a summary of whether a given mean and and n value is consistent across a range
    of rounding types.

    :param raw_mean: A string or decimal value for the mean

    :param raw_n: A string or decimal value for n (the number integer values/sample size)

    :param log_status: Optional, Defaults to False, outputs extra info regarding matches.

    :return: A dict containing rounding types (as keys) and whether the mean is consistent.
    """
    summary = {}
    for rounding_type in rounding_types:
        summary[rounding_type] = consistency_check(raw_mean, raw_n, rounding_method=getattr(decimal, rounding_type), log_status=log_status)

    return summary


def consistency_check(raw_mean, raw_n, rounding_method=decimal.ROUND_HALF_UP, log_status=False):
    """
    Returns whether the given raw_mean is consistent with the n value and rounding type provided.
    Details of the technique: https://en.wikipedia.org/wiki/GRIM_test

    :param raw_mean: A string or decimal value for the mean

    :param raw_n: A string or decimal value for n (the number integer values/sample size)

    :param rounding_method: Optional, defaults to ROUND_HALF_UP, One of the several rounding types supported by decimal, 

    :param log_status: Optional, Defaults to False, outputs extra info regarding matches.

    :return: A boolean indicating if the above values are consistent.
    """

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

    match_status = mean in [poss_match_lower, poss_match_middle, poss_match_upper]

    log(log_status, "Target Mean: " + str(mean) 
        + ", Decimal places: " + str(dp_of_mean)
        + ", Lower match: " + str(poss_match_lower)
        + ", Middle match: " + str(poss_match_middle)
        + ", Upper match: " + str(poss_match_upper)
        + ", Match status: " + str(match_status)
        + ", Rounding method: " + str(rounding_method))

    return match_status
