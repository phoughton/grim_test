# The GRIM test 
_An implementation of the GRIM test, in python_

*Beta: Work in progress*

## Introduction
This package is based on the GRIM (Granularity-Related Inconsistency of Means) test first highlighted by Heathers & Brown in their 2016 paper.

The test makes use of a simple numerical property to identify if the mean of integer values has been correctly calculated.

You don't need the original integer values. You just need the _mean_ and the number (_n_) of items in the list.
## What about rounding?

Often the 'mean' you are testing has previously been rounded. You can check if the mean is consistent with a particular rounding type by including that as an argument.

This implementation supports all the rounding types currently found in Python 3.8's `decimal` implementation.
(They are: ROUND_CEILING, ROUND_DOWN, ROUND_FLOOR, ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_HALF_UP, ROUND_UP, ROUND_05UP)

If no rounding type is included then the test assumes the it should use ROUND_HALF_UP.

### Example:
```python
from grim import mean_tester
import decimal

# mean is 11.09 and n is 21
print(mean_tester.consistency_check('11.09', '21', decimal.ROUND_HALF_UP))
```
This will return `False` as the mean could not be correct given a list of 21 integers (and using ROUND_HALF_UP rounding.)

You can pass in the numbers as Strings or Decimals, this avoids floating point accuracy issues that are more likely to occur when using a 'float'.

## How can I find out more?
James Heathers has published [articles](https://medium.com/@jamesheathers/the-grim-test-a-method-for-evaluating-published-research-9a4e5f05e870) that explain how the technique works and how he used it to expose inconsistencies in scientific papers.

