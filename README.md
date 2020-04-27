# The GRIM test 
_An implementation of the GRIM test, in python_

*Beta: Work in progress*

This package is based on the GRIM test first highlighted by Heathers & Brown in their 2016 paper.

The test makes use of a simple numerical property to identify if the mean of integer values has been correctly calculated.

You don't need the original integer values. You just need the mean and the number of items in the list (this is usually referred to as 'n')

### What about rounding?

This implementation supports all the rounding types currently supported in Python 3.8.
(ROUND_CEILING, ROUND_DOWN, ROUND_FLOOR¶, ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_HALF_UP, ROUND_UP, ROUND_05UP)

### Example:
```python
from grim import mean_tester
import decimal

# mean is 11.09 and n is 21
print(mean_tester.consistency_check('11.09', '21', decimal.ROUND_HALF_UP))
```
This will return `False` as the mean could not be correct given a list of 21 integers (and using ROUND_HALF_UP rounding.)

You can pass in the numbers as Strings or Decimals, this avoids floating point accuracy issues.

### How can I find out more?
James Heathers has published [articles](https://medium.com/@jamesheathers/the-grim-test-a-method-for-evaluating-published-research-9a4e5f05e870) that explain how the technique works and how he used it to expose inconsistencies in scientific papers.

