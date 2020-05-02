# The GRIM test 
_An implementation of the GRIM test, in python_

*Beta: Work in progress*

## Introduction
This package is based on the GRIM (Granularity-Related Inconsistency of Means) test first highlighted by Heathers & Brown in their 2016 paper.

The test makes use of a simple numerical property to identify if the mean of integer values has been correctly calculated.

You don't need the original integer values. You just need the _mean_ and the number (_n_) of items.

## What about rounding?

Often the _mean_ you are testing has previously been rounded. You can check if the _mean_ is consistent with a particular rounding type by including that as an argument.

This implementation supports all the rounding types currently found in Python 3.8's `decimal` [implementation](https://docs.python.org/3/library/decimal.html).

(They are: ROUND_CEILING, ROUND_DOWN, ROUND_FLOOR, ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_HALF_UP, ROUND_UP, ROUND_05UP)

If no rounding type is included then the test assumes ROUND_HALF_UP.

### Example: Is this _mean_, _n_ and rounding type consistent?
```python
from grim import mean_tester
import decimal

# mean is 11.09 and n is 21
print(mean_tester.consistency_check('11.09', '21', decimal.ROUND_HALF_UP))
```
This will return `False` as the mean could not be correct given a list of 21 integers (and using ROUND_HALF_UP rounding.)

### Example: Is this _mean_ & _n_ consistent using any rounding type?
```python
from grim import mean_tester
import decimal

# mean is 11.09 and n is 21
print(mean_tester.summary_consistency_check('11.09', '21'))
```
This will return:
```python
{'ROUND_CEILING': False, 'ROUND_DOWN': True, 'ROUND_FLOOR': True, 'ROUND_HALF_DOWN': False, 'ROUND_HALF_EVEN': False, 'ROUND_HALF_UP': False, 'ROUND_UP': False, 'ROUND_05UP': True}
```
As you can see, a given mean and n might be consistent using one form of rounding but not others.

You can pass in the numbers as Strings or Decimals, this avoids floating point accuracy issues that are more likely to occur when using a 'float'.

## Warning:

1. Beware of creating Decimals from floating point numbers as these may have floating point inaccuracies.


## How can I find out more about the GRIM test?
James Heathers has published [articles](https://medium.com/@jamesheathers/the-grim-test-a-method-for-evaluating-published-research-9a4e5f05e870) that explain how the technique works and how he used it to expose inconsistencies in scientific papers.

